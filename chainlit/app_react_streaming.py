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

# Import existing modular components (reusing existing structure)
from config import LOGGING_CONFIG, DB_CONNECTION
from tools import hybrid_search_tool, paper_database_tool, web_search_tool
from toolsv2 import enhanced_hybrid_search_tool, enhanced_web_search_tool
from utils import init_llm, get_config, close_pg_pool

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


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session with create_react_agent"""

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
        prompt=GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V8,  # <-- Use the optimized multimodal prompt
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

    logger.info("✅ create_react_agent initialized successfully")
    logger.info(f"📊 Tools available: {[tool.name for tool in tools]}")


@cl.on_chat_end
async def on_chat_end():
    """Clean up resources when the chat session ends"""
    # Don't close the connection here - let it persist for the session
    logger.info(
        "Chat session ended, but keeping connection alive for potential reconnection"
    )
    pass


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
    agent = cl.user_session.get("agent")
    config = cl.user_session.get("config")

    if not agent or not config:
        await cl.Message(
            content="Error: Session not properly initialized. Please refresh."
        ).send()
        return

    logger.info(f"👤 USER MESSAGE: {message.content}")

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
        logger.info(f"🚀 PROCESSING with create_react_agent: {message.content}")

        # Create an empty message that we'll stream into
        msg = cl.Message(content="")

        tool_calls_count = 0
        final_response_content = ""

        # Stream through the agent execution
        async for chunk in agent.astream(input_messages, config=enhanced_config):
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

        # Final update to the message
        if final_response_content:
            msg.content = final_response_content
            await msg.update()
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
