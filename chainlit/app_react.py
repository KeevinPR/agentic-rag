"""
Phase 1: Chainlit application using LangGraph's create_react_agent.
This is a side-by-side implementation to migrate from custom graph approach.
"""

import logging
from typing import Optional, List, Dict, Any, Union
import chainlit as cl
from langchain_core.messages import HumanMessage, AIMessage
import base64

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
        prompt=GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V2,  # <-- Use the optimized multimodal prompt
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
    try:
        memory_cm = cl.user_session.get("memory_cm")
        if memory_cm:
            logger.info("🔌 Closing PostgreSQL memory context manager...")
            await memory_cm.__aexit__(None, None, None)
            logger.info("✅ PostgreSQL memory context manager closed successfully.")
    except Exception as e:
        logger.error(f"Error during chat end cleanup: {e}")


@cl.on_stop
async def on_stop():
    """Clean up resources when the application stops"""
    try:
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
    """Handle incoming user messages using create_react_agent"""
    agent = cl.user_session.get("agent")
    config = cl.user_session.get("config")

    if not agent or not config:
        await cl.Message(
            content="Error: Session not properly initialized. Please refresh."
        ).send()
        return

    logger.info(f"👤 USER MESSAGE: {message.content}")

    # --- NEW: Multimodal Input Processing ---
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
            # --- NEW: Send feedback message to UI ---
            await cl.Message(
                content=f"Processing {len(image_elements)} image(s) with your message...",
                author="System",
            ).send()
            for el in image_elements:
                # For user-uploaded files, Chainlit provides a path. We must read the file from this path.
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

    # create_react_agent expects messages in this format.
    # We construct a HumanMessage that can contain multiple parts (text and images).
    input_messages = {"messages": [HumanMessage(content=content_parts)]}

    # Set up callback handler for streaming (same as existing implementation)
    cb_handler = cl.LangchainCallbackHandler(
        stream_final_answer=False,
        _schema_format="streaming_events",
    )

    # Enhanced config for create_react_agent
    enhanced_config = {
        **config,
        "callbacks": [cb_handler],
        "run_name": "EDA Research Agent",
        # Optional: Add recursion limit for safety
        "recursion_limit": 20,
    }

    try:
        logger.info(f"🚀 PROCESSING with create_react_agent: {message.content}")

        final_response = None
        tool_calls_count = 0

        # Stream through the agent execution
        async for chunk in agent.astream(input_messages, config=enhanced_config):
            logger.info(f"📦 CHUNK RECEIVED: {list(chunk.keys())}")

            # Add handling for 'agent' key
            if "agent" in chunk:
                agent_output = chunk["agent"]
                logger.info(f"🤖 AGENT OUTPUT TYPE: {type(agent_output)}")
                logger.info(f"🤖 AGENT OUTPUT: {agent_output}")

                # Case 1: agent_output is an AIMessage directly
                if isinstance(agent_output, AIMessage):
                    if (
                        hasattr(agent_output, "content")
                        and isinstance(agent_output.content, str)
                        and agent_output.content.strip()
                        and not getattr(agent_output, "tool_calls", None)
                    ):
                        final_response = _clean_response_content(agent_output.content)
                        logger.info(
                            f"✅ FINAL RESPONSE FROM AGENT: {final_response[:100]}..."
                        )
                # Case 2: agent_output is a dict with 'messages'
                elif isinstance(agent_output, dict) and "messages" in agent_output:
                    messages = agent_output["messages"]
                    if messages:
                        last_message = messages[-1]
                        if (
                            hasattr(last_message, "content")
                            and isinstance(last_message.content, str)
                            and last_message.content.strip()
                            and not getattr(last_message, "tool_calls", None)
                        ):
                            final_response = _clean_response_content(
                                last_message.content
                            )
                            logger.info(
                                f"✅ FINAL RESPONSE FROM AGENT MESSAGES: {final_response[:100]}..."
                            )

            # The agent returns the full conversation state
            elif "messages" in chunk:
                messages = chunk["messages"]
                if messages:
                    last_message = messages[-1]
                    logger.info(f"🤖 LAST MESSAGE TYPE: {type(last_message).__name__}")

                    # Count tool calls
                    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
                        tool_calls_count += len(last_message.tool_calls)
                        logger.info(
                            f"🔧 Tool calls: {[call['name'] for call in last_message.tool_calls]}"
                        )

                    # Check if this is the final AI response (no tool calls)
                    elif (
                        hasattr(last_message, "content")
                        and isinstance(last_message.content, str)
                        and last_message.content.strip()
                        and not getattr(last_message, "tool_calls", None)
                    ):
                        # Always update final_response with the latest AI content
                        final_response = _clean_response_content(last_message.content)
                        logger.info(
                            f"✅ FINAL RESPONSE UPDATED: {final_response[:100]}..."
                        )

        # Send the final response
        if final_response:
            await cl.Message(content=final_response, author="Assistant").send()
            logger.info(
                f"✅ Response sent successfully. Tool calls made: {tool_calls_count}"
            )
        else:
            # Fallback: Extract the last AI message from the final chunk
            logger.warning("⚠️ No final response found - checking final chunk")
            if "messages" in chunk:
                messages = chunk["messages"]
                for msg in reversed(messages):
                    if (
                        hasattr(msg, "content")
                        and isinstance(msg.content, str)
                        and msg.content.strip()
                        and not getattr(msg, "tool_calls", None)
                    ):
                        final_response = _clean_response_content(msg.content)
                        await cl.Message(
                            content=final_response, author="Assistant"
                        ).send()
                        logger.info(
                            f"🔄 Fallback response sent: {final_response[:100]}..."
                        )
                        break
                else:
                    # Ultimate fallback
                    await cl.Message(
                        content="I processed your request but couldn't generate a proper response. Please try again.",
                        author="Assistant",
                    ).send()
                    logger.warning("⚠️ No valid response found in any message")
            else:
                await cl.Message(
                    content="I processed your request but couldn't generate a proper response. Please try again.",
                    author="Assistant",
                ).send()
                logger.warning("⚠️ No messages found in final chunk")

    except Exception as e:
        logger.error(f"❌ Error in create_react_agent execution: {e}", exc_info=True)
        await cl.Message(
            content=f"I apologize, but I encountered an error: {str(e)}",
            author="Assistant",
        ).send()


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
    # The app is designed to be run with: chainlit run app_react.py
    logger.info("🆕 Starting create_react_agent implementation (Phase 1)")
    pass
