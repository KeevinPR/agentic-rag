import logging
import os
import asyncpg
import uuid
import unicodedata
import re
from typing import List, Dict, Any, Optional
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_aws import ChatBedrockConverse
from config import CONTEXT_CONFIG
from pydantic import SecretStr
from unidecode import unidecode

logger = logging.getLogger(__name__)

# Global database pool
_pg_pool: Optional[asyncpg.Pool] = None


async def get_pg_pool() -> asyncpg.Pool:
    """
    Get or create a PostgreSQL connection pool using singleton pattern.
    The pool is created once and reused across all requests.
    """
    global _pg_pool

    if _pg_pool is None:
        logger.info("[get_pg_pool] Creating new asyncpg pool...")
        try:
            _pg_pool = await asyncpg.create_pool(
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                database=os.getenv("POSTGRES_DB"),
                host=os.getenv("DB_HOST", "localhost"),
                port=os.getenv("DB_PORT", "5432"),
                min_size=5,  # Minimum number of connections
                max_size=20,  # Maximum number of connections
                command_timeout=60,  # Command timeout in seconds
                max_inactive_connection_lifetime=300.0,  # Close inactive connections after 5 minutes
            )
            logger.info("[get_pg_pool] Pool created successfully")
        except Exception as e:
            logger.error(f"[get_pg_pool] Failed to create pool: {e}")
            raise
    else:
        logger.debug("[get_pg_pool] Using existing pool")

    return _pg_pool


async def close_pg_pool():
    """
    Close the database pool when the application shuts down.
    """
    global _pg_pool
    if _pg_pool is not None:
        logger.info("[close_pg_pool] Closing database pool...")
        await _pg_pool.close()
        _pg_pool = None
        logger.info("[close_pg_pool] Database pool closed")


async def ensure_pg_trgm_extension():
    """
    Check if pg_trgm extension is available and create trigram indexes if needed.
    Note: Extensions should be created manually by DBA.
    """
    try:
        pool = await get_pg_pool()
        async with pool.acquire() as conn:
            # Test if similarity function is available (assumes pg_trgm extension exists)
            try:
                await conn.fetchval("SELECT similarity('test', 'test');")
                logger.info("pg_trgm similarity function is available")
            except Exception as e:
                logger.warning(f"pg_trgm similarity function not available: {e}")
                logger.info(
                    "Please create extensions manually: CREATE EXTENSION IF NOT EXISTS pg_trgm;"
                )
                return False

            # Check if trigram index exists for authors
            author_index_exists = await conn.fetchval("""
                SELECT EXISTS (
                    SELECT 1 FROM pg_indexes 
                    WHERE tablename = 'papers' 
                    AND indexname = 'idx_authors_trgm'
                );
            """)

            # Check if trigram index exists for titles
            title_index_exists = await conn.fetchval("""
                SELECT EXISTS (
                    SELECT 1 FROM pg_indexes 
                    WHERE tablename = 'papers' 
                    AND indexname = 'idx_titles_trgm'
                );
            """)

            if not author_index_exists:
                logger.info("Creating trigram index for authors_normalized...")
                try:
                    await conn.execute("""
                        CREATE INDEX CONCURRENTLY idx_authors_trgm 
                        ON eda_rag_data.papers 
                        USING gin (authors_normalized gin_trgm_ops);
                    """)
                    logger.info("Authors trigram index created successfully")
                except Exception as e:
                    logger.warning(f"Could not create authors trigram index: {e}")
                    # Try without CONCURRENTLY
                    try:
                        await conn.execute("""
                            CREATE INDEX idx_authors_trgm 
                            ON eda_rag_data.papers 
                            USING gin (authors_normalized gin_trgm_ops);
                        """)
                        logger.info(
                            "Authors trigram index created successfully (without CONCURRENTLY)"
                        )
                    except Exception as e2:
                        logger.warning(
                            f"Could not create authors trigram index at all: {e2}"
                        )
                        return False
            else:
                logger.debug("Authors trigram index already exists")

            if not title_index_exists:
                logger.info("Creating trigram index for title_normalized...")
                try:
                    await conn.execute("""
                        CREATE INDEX CONCURRENTLY idx_titles_trgm 
                        ON eda_rag_data.papers 
                        USING gin (title_normalized gin_trgm_ops);
                    """)
                    logger.info("Titles trigram index created successfully")
                except Exception as e:
                    logger.warning(f"Could not create titles trigram index: {e}")
                    # Try without CONCURRENTLY
                    try:
                        await conn.execute("""
                            CREATE INDEX idx_titles_trgm 
                            ON eda_rag_data.papers 
                            USING gin (title_normalized gin_trgm_ops);
                        """)
                        logger.info(
                            "Titles trigram index created successfully (without CONCURRENTLY)"
                        )
                    except Exception as e2:
                        logger.warning(
                            f"Could not create titles trigram index at all: {e2}"
                        )
                        # Don't return False here as author matching might still work
            else:
                logger.debug("Titles trigram index already exists")

            return True

    except Exception as e:
        logger.warning(f"Could not set up pg_trgm: {e}")
        return False


def estimate_token_count(text: str) -> int:
    """
    Improved token estimation for Gemini models.
    Uses a more accurate approximation: ~0.75 tokens per word for English text.
    """
    if not text:
        return 0

    # Count words and characters for better estimation
    words = len(text.split())
    chars = len(text)

    # Gemini tends to tokenize more efficiently than GPT models
    # Use conservative estimate: 0.75 tokens per word, with character-based fallback
    word_based = int(words * 0.75)
    char_based = int(chars / 4)  # ~4 chars per token average

    # Use the higher estimate for safety
    return max(word_based, char_based)


def get_message_token_count(msg: BaseMessage) -> int:
    """Get token count for a single message including metadata."""
    content_tokens = estimate_token_count(str(msg.content))
    # Add small overhead for message metadata (type, role, etc.)
    metadata_overhead = 10
    return content_tokens + metadata_overhead


def create_conversation_summary(messages: List[BaseMessage]) -> str:
    """
    Create a concise summary of conversation messages.
    Focus on key topics and decisions made.
    """
    if not messages:
        return "No previous conversation to summarize."

    # Extract key information from messages
    topics = []
    decisions = []

    for msg in messages:
        content = str(msg.content)
        if isinstance(msg, HumanMessage):
            # Extract questions/topics from user messages
            if len(content) > 50:  # Only summarize substantial messages
                topics.append(f"User asked about: {content[:100]}...")
        elif isinstance(msg, AIMessage):
            # Extract key decisions/answers from AI messages
            if "decision" in content.lower() or "conclusion" in content.lower():
                decisions.append(f"Assistant determined: {content[:100]}...")

    summary_parts = []
    if topics:
        summary_parts.append(f"Previous topics discussed: {'; '.join(topics[:3])}")
    if decisions:
        summary_parts.append(f"Key decisions made: {'; '.join(decisions[:2])}")

    if not summary_parts:
        return f"Previous conversation summary: {len(messages)} messages exchanged about EDA research."

    return "[CONVERSATION SUMMARY] " + " | ".join(summary_parts)


def debug_context_info(messages: List[BaseMessage]) -> str:
    """Generate debug information about the current context state"""
    if not messages:
        return "No messages in context"

    total_tokens = sum(estimate_token_count(str(msg.content)) for msg in messages)

    message_types = {}
    for msg in messages:
        msg_type = type(msg).__name__
        message_types[msg_type] = message_types.get(msg_type, 0) + 1

    return f"Context: {len(messages)} messages, ~{total_tokens} tokens, types: {message_types}"


async def get_config():
    """Returns a new LangGraph configuration object for each conversation thread."""
    return {"configurable": {"thread_id": str(uuid.uuid4())}}


def init_vector_stores():
    """Initialize vector stores"""
    from langchain_postgres import PGVector
    from config import DB_CONNECTION, SIMPLE_COLLECTION

    try:
        simple_vector_store = PGVector(
            connection=DB_CONNECTION["connection_string"],
            collection_name=SIMPLE_COLLECTION,
            embeddings=DB_CONNECTION["embedding_function"],
            use_jsonb=True,
        )
        return simple_vector_store
    except Exception as e:
        logger.error(f"Failed to initialize vector stores: {e}")
        raise


def init_llm():
    """
    Initialize the language model - Support Anthropic Claude, ChatNvidia, Google, and AWS Bedrock
    """
    from config import LLM_CONFIG, LLM_CONFIG_NVIDIA, LLM_CONFIG_GOOGLE, LLM_CONFIG_BEDROCK
    import os

    # Determine which provider to use
    # You can set USE_NVIDIA=true, USE_GOOGLE=true, or USE_ANTHROPIC=true in environment to switch providers
    use_nvidia = os.getenv("USE_NVIDIA", "false").lower() == "true"
    use_google = os.getenv("USE_GOOGLE", "false").lower() == "true"
    use_anthropic = os.getenv("USE_ANTHROPIC", "false").lower() == "true"

    if use_anthropic:
        # Use AWS Bedrock with Claude Sonnet 4
        config = LLM_CONFIG_BEDROCK
        model_id = os.getenv("BEDROCK_MODEL_ID", config["model_id"])
        region = os.getenv("AWS_REGION", config["region"])
        max_tokens = int(os.getenv("MAX_TOKENS", str(config["max_tokens"])))
        temperature = float(os.getenv("TEMPERATURE", str(config["temperature"])))

        logger.info(f"🤖 Initializing AWS Bedrock Claude with model: {model_id} in region: {region}")
        
        llm = ChatBedrockConverse(
            model_id=model_id,
            region_name=region,
        ).bind(
            # parámetros de generación por defecto
            max_tokens=max_tokens,
            temperature=temperature,
        )

        # (OPCIONAL) razonamiento extendido (pensamiento) — COSTE extra
        if os.getenv("ENABLE_EXTENDED_THINKING", "false").lower() == "true":
            budget = int(os.getenv("THINKING_BUDGET_TOKENS", "1024"))
            # Bedrock/Anthropic: se pasa en additional_model_request_fields
            llm = llm.bind(
                additional_model_request_fields={
                    "thinking": {"type": "enabled", "budget_tokens": budget}
                }
            )
        return llm
    elif use_google:
        # Use ChatGoogleGenerativeAI
        from langchain_google_genai import ChatGoogleGenerativeAI

        config = LLM_CONFIG_GOOGLE
        api_key = os.getenv(config["api_key_env"])
        if not api_key:
            raise ValueError(
                f"Missing API key: {config['api_key_env']} environment variable not set"
            )

        logger.info(f"🤖 Initializing Google with model: {config['model']}")
        return ChatGoogleGenerativeAI(
            model=config["model"],
            temperature=config["temperature"],
            max_tokens=config["max_tokens"],
            timeout=config["timeout"],
            # api_key=api_key,
            # base_url=config["base_url"],
        )
    elif use_nvidia:
        # Use ChatNvidia Llama
        from langchain_nvidia_ai_endpoints import ChatNVIDIA

        config = LLM_CONFIG_NVIDIA
        api_key = os.getenv(config["api_key_env"])
        if not api_key:
            raise ValueError(
                f"Missing API key: {config['api_key_env']} environment variable not set"
            )

        logger.info(f"🤖 Initializing ChatNvidia with model: {config['model']}")
        return ChatNVIDIA(
            model=config["model"],
            temperature=config["temperature"],
            max_tokens=config["max_tokens"],
            timeout=config["timeout"],
            api_key=api_key,
            base_url=config["base_url"],
        )
    else:
        # Use Anthropic Claude (default)
        from langchain_anthropic import ChatAnthropic

        config = LLM_CONFIG
        api_key = os.getenv(config["api_key_env"])
        if not api_key:
            raise ValueError(
                f"Missing API key: {config['api_key_env']} environment variable not set"
            )

        logger.info(f"🤖 Initializing Claude with model: {config['model']}")
        return ChatAnthropic(
            model_name=config["model"],
            temperature=0,  # Match working app.py exactly
            max_tokens_to_sample=config["max_tokens"],
            timeout=config["timeout"],
            api_key=SecretStr(api_key),  # Wrap API key in SecretStr
            stop=None,  # Match working app.py exactly
        )


# Note: Complex entity extraction and SQL generation functions have been removed.
# The enhanced SQL_GENERATION_PROMPT now handles fuzzy matching intelligence directly
# using both ILIKE and similarity() functions within the LLM-generated SQL.
