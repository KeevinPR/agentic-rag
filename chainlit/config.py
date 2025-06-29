import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

# Context Management Configuration
CONTEXT_CONFIG = {
    "max_total_tokens": 400000,  # Conservative limit (40% of 1M tokens)
    "safety_buffer": 50000,  # Buffer for safety
    "min_recent_messages": 4,  # Minimum recent messages to keep
    "max_conversation_turns": 6,  # Maximum conversation turns to consider
    "summary_trigger_ratio": 0.8,  # Trigger summary when 80% of limit reached
}

EMBEDDING_MODEL = {
    "all-mpnet-base-v2": "sentence-transformers/all-mpnet-base-v2",
    "e5-base-v2": "intfloat/e5-base-v2",
}
# Database connection parameters
DB_CONNECTION = {
    "connection_string": f"postgresql+psycopg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('POSTGRES_DB')}?options=-csearch_path%3Deda_rag_data_augmented_e5,public",
    "embedding_function": HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL["e5-base-v2"],
        encode_kwargs={"normalize_embeddings": True},
    ),
}


# Collections for vector stores
SIMPLE_COLLECTION = "chunks"

# LLM Configuration
LLM_CONFIG = {
    "provider": "anthropic",  # "anthropic" or "nvidia"
    "model": "claude-3-haiku-20240307",  # Fast and cost-effective model
    "temperature": 0.7,
    "max_tokens": 4096,
    "timeout": 60,
    "api_key_env": "ANTHROPIC_API_KEY",
}

# Alternative LLM Configuration for ChatNvidia (better rate limits)
LLM_CONFIG_NVIDIA = {
    "provider": "nvidia",
    "model": "meta/llama-3.3-70b-instruct",  # or "meta/llama-3.1-405b-instruct" for even better performance
    "temperature": 0,
    "max_tokens": 4096,
    "timeout": 60,
    "api_key_env": "NVIDIA_API_KEY",
    "base_url": "https://integrate.api.nvidia.com/v1",
}

LLM_CONFIG_DEEPSEEK = {
    "provider": "nvidia",
    "model": "deepseek-ai/deepseek-r1",  # or "meta/llama-3.1-405b-instruct" for even better performance
    "temperature": 0,
    "max_tokens": 4096,
    "timeout": 60,
    "api_key_env": "NVIDIA_API_KEY",
}

LLM_CONFIG_GOOGLE = {
    "provider": "google",
    "model": "gemini-2.0-flash",
    "temperature": 0.5,
    "max_tokens": 8192,
    "timeout": 60,
    "api_key_env": "GOOGLE_API_KEY",
}

# ChatAnthropic configuration (commented out)
# LLM_CONFIG = {
#     "model_name": "claude-3-haiku-20240307",
#     "temperature": 0,
#     "max_tokens_to_sample": 1024,
#     "timeout": None,
#     "stop": None,
# }

# Search Configuration
SEARCH_CONFIG = {
    "enable_reranking": True,
    "num_results_default": 10,
    "initial_candidates_multiplier": 2,
    "max_candidates": 20,
    "final_results_count": 5,
    "rerank_threshold": 3,
    "rrf_k": 60,
    "cross_encoder": {
        "model_name": "cross-encoder/ms-marco-MiniLM-L6-v2",
        "min_candidates": 3,  # Minimum number of candidates to trigger reranking
        "score_threshold": 0.5,  # Minimum score to consider a result relevant
    },
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
}
