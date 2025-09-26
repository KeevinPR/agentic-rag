"""
Phase 1: Chainlit application using LangGraph's create_react_agent.
This is a side-by-side implementation to migrate from custom graph approach.

THIS SCRIPT ENABLES TOKEN-BY-TOKEN STREAMING.
"""

import logging
from typing import Optional, List, Dict, Any, Union
import chainlit as cl
from langchain_core.messages import HumanMessage, AIMessage
import base64
import re
import time

# Import existing modular components (reusing existing structure)
from config import LOGGING_CONFIG, DB_CONNECTION, DEMO_CONFIG
from tools import hybrid_search_tool, paper_database_tool, web_search_tool
from toolsv2 import enhanced_hybrid_search_tool, enhanced_web_search_tool
from utils import init_llm, get_config, close_pg_pool
from auth_demo import demo_auth
from warmup import get_warmup_manager, stop_warmup_manager
from cache import get_response_cache, is_cacheable_query, clear_response_cache

# from tools import create_tools_with_llm
from prompts import (
    # SYSTEM_MESSAGE_CONTENT,
    # TEST_SYSTEM_MESSAGE_CONTENT,
    GEMINI_EDA_PROMPT,
    GEMINI_EDA_PROMPT_V2,  # Simple e5
    GEMINI_EDA_PROMPT_FINAL,
    GEMINI_EDA_PROMPT_ENHANCED,  # BEST ONE
    GEMINI_EDA_PROMPT_ENHANCED_V2,  # BEST ONE
    GEMINI_EDA_PROMPT_REACT_AGENT,  # NEW: For create_react_agent
    GEMINI_EDA_PROMPT_ULTIMATE,  # ULTIMATE: Best hybrid prompt
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V2,  # OPTIMIZED: For create_react_agent
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V4,
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_THINK,
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V6,
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V7,
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V8,
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V8_EFFICIENT,
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_FINAL,
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_FINAL_TEST,
)  # Use the updated system prompt

# NEW: Import LangGraph's prebuilt agent
from langgraph.prebuilt import create_react_agent

# Use the production-ready hybrid checkpointer
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOGGING_CONFIG["level"]), format=LOGGING_CONFIG["format"]
)
logger = logging.getLogger(__name__)

# Initialize LLM
llm = init_llm()

# Create LLM-enabled tools (reusing existing factory)
tools = [
    # hybrid_search_tool,
    # web_search_tool,
    paper_database_tool,
    enhanced_hybrid_search_tool,
    enhanced_web_search_tool,
]


@cl.password_auth_callback
def auth_callback(username: str, password: str):
    """Authentication callback for temporary demo"""
    
    # Get client IP from Nginx headers
    import os
    client_ip = 'unknown'
    try:
        # Try to get the real IP from headers passed by Nginx
        if hasattr(cl.context, 'request'):
            headers = getattr(cl.context.request, 'headers', {})
            client_ip = (
                headers.get('X-Real-IP') or 
                headers.get('X-Forwarded-For', '').split(',')[0].strip() or
                headers.get('X-Client-IP') or
                getattr(cl.context.request, 'client', {}).get('host', 'unknown')
            )
    except Exception as e:
        logger.debug(f"Could not get client IP: {e}")
        client_ip = 'unknown'
    
    # Authenticate with demo manager
    session_data = demo_auth.authenticate(username, password, client_ip)
    
    if session_data:
        logger.info(f"✅ Demo user authenticated: {username} from IP: {client_ip}")
        
        return cl.User(
            identifier=session_data["user_id"],
            metadata={
                "session_id": session_data["session_id"],
                "role": session_data["role"],
                "permissions": session_data["permissions"],
                "rate_limit": session_data["rate_limit"]
            }
        )
    else:
        logger.warning(f"❌ Failed login attempt: {username} from IP: {client_ip}")
        return None


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session with create_react_agent"""
    
    # Validate authenticated user
    user = cl.user_session.get("user")
    if not user:
        await cl.Message(
            content="❌ Authentication error. Please log in again.",
            author="System"
        ).send()
        return
    
    # Validate active session
    session_id = user.metadata.get("session_id")
    if session_id:
        session_data = demo_auth.validate_session(session_id)
        if not session_data:
            await cl.Message(
                content="⏰ Your session has expired. Please log in again.",
                author="System"
            ).send()
            return
    
    # Show demo session information
    role = user.metadata.get("role", "unknown")
    rate_limit = user.metadata.get("rate_limit", 0)
    
    await cl.Message(
        content=f"""🎯 **Active Demo Session**
        
**User:** {user.identifier}
**Role:** {role}
**Queries per hour:** {rate_limit}
**Valid until:** {DEMO_CONFIG['expires_at']}

Welcome to the EDA RAG system! You can ask questions about Estimation of Distribution Algorithms.""",
        author="System"
    ).send()

    logger.info("🚀 Initializing create_react_agent with PostgreSQL memory...")

    # Use your existing PostgreSQL connection string from config.py
    raw_conn_string = DB_CONNECTION["connection_string"]
    # Sanitize the connection string for langgraph checkpointer
    conn_string = raw_conn_string.replace(
        "postgresql+psycopg://", "postgresql://"
    ).split("?")[0]
    logger.info(f"Sanitized connection string for checkpointer: {conn_string}")

    # Instantiate the persistent PostgreSQL checkpointer
    # This saver is safe for async environments and supports both sync/async calls
    memory_cm = AsyncPostgresSaver.from_conn_string(conn_string)
    memory = await memory_cm.__aenter__()
    cl.user_session.set("memory_cm", memory_cm)

    # NEW: Ensure the database schema is created
    await memory.setup()

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V8_EFFICIENT,  # <-- Use the EFFICIENT prompt
        checkpointer=memory,  # <-- Use the persistent PostgreSQL memory
        version="v2",
        debug=True,
    )

    cl.user_session.set("agent", agent)

    # --- TRUE USER PERSISTENCE LOGIC ---
    # Get user identifier from the Chainlit session.
    # This creates a stable thread_id that persists across user sessions.
    user_id = cl.user_session.get("id")  # Chainlit's unique session ID
    thread_id = cl.user_session.get("thread_id")

    if thread_id is None:
        thread_id = f"thread_{user_id}"  # Create a stable ID
        cl.user_session.set("thread_id", thread_id)
        logger.info(f"🆕 New user session. Created stable thread_id: {thread_id}")
    else:
        logger.info(f"🔄 Resuming existing session with thread_id: {thread_id}")

    # Use this stable thread_id for the LangGraph configuration
    config = {"configurable": {"thread_id": thread_id}}
    cl.user_session.set("config", config)

    # ⚡ Initialize and start warmup manager for Bedrock
    warmup_manager = get_warmup_manager(llm)
    cl.user_session.set("warmup_manager", warmup_manager)
    
    # Start the warmup scheduler in the background
    import asyncio
    warmup_task = asyncio.create_task(warmup_manager.start_warmup_scheduler())
    cl.user_session.set("warmup_task", warmup_task)

    logger.info("✅ create_react_agent initialized successfully")
    logger.info(f"📊 Tools available: {[tool.name for tool in tools]}")
    logger.info("🔥 Bedrock warmup manager started")


@cl.on_chat_end
async def on_chat_end():
    """Clean up resources when the chat session ends"""
    # Close user session
    user = cl.user_session.get("user")
    if user:
        session_id = user.metadata.get("session_id")
        if session_id:
            demo_auth.logout(session_id)
            logger.info(f"User {user.identifier} disconnected")
    
    # Stop warmup manager for this session
    warmup_manager = cl.user_session.get("warmup_manager")
    if warmup_manager:
        warmup_manager.stop_warmup_scheduler()
    
    warmup_task = cl.user_session.get("warmup_task")
    if warmup_task:
        warmup_task.cancel()

    # Don't close the connection here - let it persist for the session
    logger.info(
        "Chat session ended, but keeping connection alive for potential reconnection"
    )


@cl.on_stop
async def on_stop():
    """Clean up resources when the application stops"""
    try:
        # Close the memory context manager here
        memory_cm = cl.user_session.get("memory_cm")
        if memory_cm:
            logger.info("🔌 Closing PostgreSQL memory context manager...")
            await memory_cm.__aexit__(None, None, None)
            logger.info("✅ PostgreSQL memory context manager closed successfully.")

        # Stop global warmup manager
        stop_warmup_manager()
        
        # Clear response cache
        clear_response_cache()
        
        await close_pg_pool()
        logger.info("Application shutdown complete")
    except Exception as e:
        logger.error(f"Error during shutdown: {e}")


def _clean_response_content(content: str) -> str:
    """Clean up response content by removing result tags"""
    if not content:
        return content
    return content.replace("<result>", "").replace("</result>", "")


@cl.on_message
async def on_message(message: cl.Message):
    """Handle incoming user messages using create_react_agent with proper streaming"""
    # ⏱️ TIMING: Start del request completo
    start_time = time.time()
    logger.info(f"⏱️ [TIMING] REQUEST START: {time.strftime('%H:%M:%S')} - User message: {message.content}")
    
    agent = cl.user_session.get("agent")
    config = cl.user_session.get("config")
    warmup_manager = cl.user_session.get("warmup_manager")

    if not agent or not config:
        await cl.Message(
            content="Error: Session not properly initialized. Please refresh."
        ).send()
        return
    
    # ⚡ Ensure model is warm before processing request
    if warmup_manager:
        await warmup_manager.ensure_warm()

    logger.info(f"👤 USER MESSAGE: {message.content}")

    # ⚡ Check cache for repeated queries (only for simple, cacheable queries)
    cache = get_response_cache()
    cached_response = None
    
    if is_cacheable_query(message.content):
        cached_response = cache.get(message.content)
        if cached_response:
            # Return cached response immediately
            cache_msg = cl.Message(content="")
            
            # Stream the cached response token by token for consistency
            for token in cached_response:
                await cache_msg.stream_token(token)
            
            await cache_msg.update()
            
            # ⏱️ TIMING: Cache hit
            end_time = time.time()
            total_time = end_time - start_time
            logger.info(f"⏱️ [TIMING] CACHE HIT: {total_time:.2f}s - Returned cached response")
            return

    # --- Multimodal Input Processing ---
    content_parts: List[Union[str, Dict[str, Any]]] = [
        {"type": "text", "text": message.content}
    ]

    # Check for file attachments (focusing on images)
    if message.elements:
        image_elements = [
            el for el in message.elements if el.mime and "image" in el.mime
        ]
        if image_elements:
            logger.info(f"🖼️ Found {len(image_elements)} image(s) in the message.")
            await cl.Message(
                content=f"Processing {len(image_elements)} image(s) with your message...",
                author="System",
            ).send()
            for el in image_elements:
                if el.path:
                    try:
                        with open(el.path, "rb") as image_file:
                            image_bytes = image_file.read()

                        base64_image = base64.b64encode(image_bytes).decode("utf-8")
                        content_parts.append(
                            {
                                "type": "image_url",
                                "image_url": f"data:{el.mime};base64,{base64_image}",
                            }
                        )
                        logger.info(
                            f"   - Added image '{el.name}' from path '{el.path}' to the prompt."
                        )
                    except Exception as e:
                        logger.error(
                            f"Error reading image file from path {el.path}: {e}"
                        )

    # create_react_agent expects messages in this format
    input_messages = {"messages": [HumanMessage(content=content_parts)]}

    # Use LangchainCallbackHandler for tool call visibility, but NOT for final answer streaming
    # We'll handle final answer streaming manually using cl.Message.stream_token()
    cb_handler = cl.LangchainCallbackHandler(
        stream_final_answer=False,  # We handle this manually
        _schema_format="streaming_events",
    )

    # Enhanced config for create_react_agent (with callback handler for tool visibility)
    enhanced_config = {
        **config,
        "callbacks": [cb_handler],
        "run_name": "EDA Research Agent",
        "recursion_limit": 20,
    }

    try:
        # ⏱️ TIMING: Antes de llamar al agente
        agent_start_time = time.time()
        prep_time = agent_start_time - start_time
        logger.info(f"⏱️ [TIMING] PREP COMPLETE: {prep_time:.2f}s - Starting agent processing")
        
        logger.info(f"🚀 PROCESSING with create_react_agent: {message.content}")

        # Create an empty message that we'll stream into
        msg = cl.Message(content="")

        tool_calls_count = 0
        final_response_content = ""
        first_chunk_time = None
        first_tool_time = None
        first_response_time = None

        # Stream through the agent execution
        async for chunk in agent.astream(input_messages, config=enhanced_config):
            # ⏱️ TIMING: Primer chunk recibido
            if first_chunk_time is None:
                first_chunk_time = time.time()
                time_to_first_chunk = first_chunk_time - agent_start_time
                logger.info(f"⏱️ [TIMING] FIRST CHUNK: {time_to_first_chunk:.2f}s after agent start")
            logger.info(f"📦 CHUNK RECEIVED: {list(chunk.keys())}")

            # Handle different chunk types
            if "agent" in chunk:
                agent_output = chunk["agent"]
                logger.info(f"🤖 AGENT OUTPUT: {agent_output}")

                # Check if this chunk contains messages
                if isinstance(agent_output, dict) and "messages" in agent_output:
                    messages = agent_output["messages"]
                    if messages:
                        last_message = messages[-1]
                        if (
                            hasattr(last_message, "tool_calls")
                            and last_message.tool_calls
                        ):
                            # ⏱️ TIMING: Primera tool call
                            if first_tool_time is None:
                                first_tool_time = time.time()
                                time_to_first_tool = first_tool_time - agent_start_time
                                logger.info(f"⏱️ [TIMING] FIRST TOOL CALL: {time_to_first_tool:.2f}s after agent start")
                            
                            tool_calls_count += len(last_message.tool_calls)
                            logger.info(
                                f"🔧 Tool calls: {[call['name'] for call in last_message.tool_calls]}"
                            )
                        elif (
                            hasattr(last_message, "content")
                            and isinstance(last_message.content, str)
                            and last_message.content.strip()
                            and not getattr(last_message, "tool_calls", None)
                        ):
                            # ⏱️ TIMING: Primera respuesta final
                            if first_response_time is None:
                                first_response_time = time.time()
                                time_to_first_response = first_response_time - agent_start_time
                                logger.info(f"⏱️ [TIMING] FIRST RESPONSE: {time_to_first_response:.2f}s after agent start")
                            
                            # This is the final response from agent chunk - stream it token by token
                            new_content = _clean_response_content(last_message.content)

                            # Only stream new content (avoiding duplicates)
                            if new_content != final_response_content:
                                # Calculate the difference and stream new tokens
                                if len(new_content) > len(final_response_content):
                                    new_tokens = new_content[
                                        len(final_response_content) :
                                    ]

                                    # Stream the new tokens
                                    for token in new_tokens:
                                        await msg.stream_token(token)

                                    final_response_content = new_content
                                    logger.info(
                                        f"✅ STREAMING: Added {len(new_tokens)} new tokens from agent chunk"
                                    )

            elif "messages" in chunk:
                messages = chunk["messages"]
                if messages:
                    last_message = messages[-1]
                    logger.info(f"🤖 LAST MESSAGE TYPE: {type(last_message).__name__}")

                    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
                        # ⏱️ TIMING: Primera tool call (en caso de que no se haya detectado antes)
                        if first_tool_time is None:
                            first_tool_time = time.time()
                            time_to_first_tool = first_tool_time - agent_start_time
                            logger.info(f"⏱️ [TIMING] FIRST TOOL CALL: {time_to_first_tool:.2f}s after agent start")
                        
                        tool_calls_count += len(last_message.tool_calls)
                        logger.info(
                            f"🔧 Tool calls: {[call['name'] for call in last_message.tool_calls]}"
                        )

                    elif (
                        hasattr(last_message, "content")
                        and isinstance(last_message.content, str)
                        and last_message.content.strip()
                        and not getattr(last_message, "tool_calls", None)
                    ):
                        # ⏱️ TIMING: Primera respuesta final (en caso de que no se haya detectado antes)
                        if first_response_time is None:
                            first_response_time = time.time()
                            time_to_first_response = first_response_time - agent_start_time
                            logger.info(f"⏱️ [TIMING] FIRST RESPONSE: {time_to_first_response:.2f}s after agent start")
                        
                        # This is the final response - stream it token by token
                        new_content = _clean_response_content(last_message.content)

                        # Only stream new content (avoiding duplicates)
                        if new_content != final_response_content:
                            # Calculate the difference and stream new tokens
                            if len(new_content) > len(final_response_content):
                                new_tokens = new_content[len(final_response_content) :]

                                # Stream the new tokens
                                for token in new_tokens:
                                    await msg.stream_token(token)

                                final_response_content = new_content
                                logger.info(
                                    f"✅ STREAMING: Added {len(new_tokens)} new tokens"
                                )

        # ⏱️ TIMING: Request completo terminado
        end_time = time.time()
        total_time = end_time - start_time
        agent_time = end_time - agent_start_time
        
        # Final update to the message
        if final_response_content:
            msg.content = final_response_content
            await msg.update()
            
            # ⚡ Cache the response if it's cacheable
            if is_cacheable_query(message.content) and len(final_response_content) > 50:
                cache.put(message.content, final_response_content)
            
            logger.info(
                f"✅ FINAL RESPONSE COMPLETE: {len(final_response_content)} characters streamed"
            )
        else:
            # Fallback if no final response was detected
            await msg.stream_token(
                "I apologize, but I couldn't generate a proper response. Please try again."
            )
            await msg.update()
            logger.warning("⚠️ No final response detected - sent fallback message")

        # ⏱️ TIMING: Resumen completo de tiempos
        logger.info(f"⏱️ [TIMING SUMMARY] TOTAL REQUEST: {total_time:.2f}s")
        logger.info(f"⏱️ [TIMING SUMMARY] PREP TIME: {prep_time:.2f}s")
        logger.info(f"⏱️ [TIMING SUMMARY] AGENT TIME: {agent_time:.2f}s")
        if first_chunk_time:
            logger.info(f"⏱️ [TIMING SUMMARY] TIME TO FIRST CHUNK: {first_chunk_time - agent_start_time:.2f}s")
        if first_tool_time:
            logger.info(f"⏱️ [TIMING SUMMARY] TIME TO FIRST TOOL: {first_tool_time - agent_start_time:.2f}s")
        if first_response_time:
            logger.info(f"⏱️ [TIMING SUMMARY] TIME TO FIRST RESPONSE: {first_response_time - agent_start_time:.2f}s")

        # 📊 Performance metrics
        tokens_per_second = len(final_response_content) / agent_time if agent_time > 0 else 0
        logger.info(f"📊 [METRICS] RESPONSE LENGTH: {len(final_response_content)} chars")
        logger.info(f"📊 [METRICS] THROUGHPUT: {tokens_per_second:.1f} chars/sec")
        logger.info(f"📊 [METRICS] TOOL CALLS: {tool_calls_count}")
        
        # 💾 Cache statistics
        cache_stats = cache.stats()
        logger.info(f"💾 [CACHE] Entries: {cache_stats['total_entries']}, Hits: {cache_stats['total_hits']}")

        logger.info(
            f"✅ Agent execution finished. Total tool calls made: {tool_calls_count}"
        )

    except Exception as e:
        logger.error(f"❌ Error in create_react_agent execution: {e}", exc_info=True)
        error_msg = cl.Message(content="")
        error_text = f"I apologize, but I encountered an error: {str(e)}"
        for token in error_text:
            await error_msg.stream_token(token)
        await error_msg.update()


@cl.set_starters
async def set_starters(user: Optional[cl.User] = None):
    """Set up starter prompts for new users"""
    return [
        cl.Starter(
            label="What are EDAs?",
            message="What are EDAs?",
            icon="/public/idea.svg",
        ),
        cl.Starter(
            label="Pseudocode for UMDA?",
            message="Pseudocode for UMDA?",
            icon="/public/code.svg",
        ),
        # cl.Starter(
        #     label="PBIL papers published in the last 10 years",
        #     message="How many papers on PBIL were published in the last 10 years?",
        #     icon="/public/database.svg",
        # ),
    ]


if __name__ == "__main__":
    # The app is designed to be run with: chainlit run app_react_streaming.py
    logger.info("🆕 Starting create_react_agent implementation with STREAMING ENABLED")
    pass
