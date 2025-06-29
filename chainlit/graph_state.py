"""
Graph state management and configuration for the EDA research assistant.
"""

import logging
from typing import List, Annotated
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from config import CONTEXT_CONFIG
from utils import (
    create_conversation_summary,
    get_message_token_count,
)
from prompts import (
    SYSTEM_MESSAGE_CONTENT,
    QUERY_EVALUATION_PROMPT,
    CONTEXT_AWARE_QUERY_EVALUATION_PROMPT,
)

logger = logging.getLogger(__name__)


def smart_message_reducer(
    existing_messages: List[BaseMessage], new_messages: List[BaseMessage]
) -> List[BaseMessage]:
    """
    Enhanced smart message reducer with robust token limit management.

    Strategy:
    1. Always preserve system message
    2. Calculate precise token counts
    3. Use progressive reduction strategies
    4. Maintain conversational coherence
    5. Never exceed token limits
    """
    # Combine all messages
    all_messages = (existing_messages or []) + new_messages

    if not all_messages:
        return []

    logger.info(f"Processing {len(all_messages)} total messages")

    # Separate system message and conversation messages
    system_msg = None
    conversation_msgs = []

    for msg in all_messages:
        if isinstance(msg, SystemMessage):
            system_msg = msg
        else:
            conversation_msgs.append(msg)

    # Calculate initial token counts
    system_tokens = get_message_token_count(system_msg) if system_msg else 0
    conversation_tokens = sum(get_message_token_count(msg) for msg in conversation_msgs)
    total_tokens = system_tokens + conversation_tokens

    logger.info(
        f"Token counts - System: {system_tokens}, Conversation: {conversation_tokens}, Total: {total_tokens}"
    )

    # Determine target token limit (with safety buffer)
    target_limit = CONTEXT_CONFIG["max_total_tokens"] - CONTEXT_CONFIG["safety_buffer"]

    # If we're under the limit, return all messages
    if total_tokens <= target_limit:
        result: List[BaseMessage] = [system_msg] if system_msg else []
        result.extend(conversation_msgs)
        logger.info(f"No reduction needed. Total tokens: {total_tokens}/{target_limit}")
        return result

    # We need to reduce - start with progressive strategies
    logger.info(f"Reduction needed. Current: {total_tokens}, Target: {target_limit}")

    # Strategy 1: Keep only recent messages
    max_recent = min(CONTEXT_CONFIG["max_conversation_turns"], len(conversation_msgs))

    for num_recent in range(max_recent, CONTEXT_CONFIG["min_recent_messages"] - 1, -2):
        recent_msgs = conversation_msgs[-num_recent:]
        recent_tokens = sum(get_message_token_count(msg) for msg in recent_msgs)

        if system_tokens + recent_tokens <= target_limit:
            result: List[BaseMessage] = [system_msg] if system_msg else []
            result.extend(recent_msgs)
            logger.info(
                f"Strategy 1 success: keeping {num_recent} recent messages ({recent_tokens} tokens)"
            )
            return result

    # Strategy 2: Create summary + keep minimum recent messages
    min_recent_msgs = conversation_msgs[-CONTEXT_CONFIG["min_recent_messages"] :]
    min_recent_tokens = sum(get_message_token_count(msg) for msg in min_recent_msgs)

    # Messages to summarize (exclude the minimum recent ones)
    messages_to_summarize = conversation_msgs[: -CONTEXT_CONFIG["min_recent_messages"]]

    if messages_to_summarize:
        summary_text = create_conversation_summary(messages_to_summarize)
        summary_msg = AIMessage(content=summary_text)
        summary_tokens = get_message_token_count(summary_msg)

        total_with_summary = system_tokens + summary_tokens + min_recent_tokens

        if total_with_summary <= target_limit:
            result: List[BaseMessage] = [system_msg] if system_msg else []
            result.append(summary_msg)
            result.extend(min_recent_msgs)
            logger.info(
                f"Strategy 2 success: summary + {len(min_recent_msgs)} recent messages ({total_with_summary} tokens)"
            )
            return result

    # Strategy 3: Emergency reduction - keep only the most recent messages that fit
    logger.warning("Emergency reduction triggered - keeping only messages that fit")

    result: List[BaseMessage] = [system_msg] if system_msg else []
    current_tokens = system_tokens

    # Add messages from most recent backwards until we hit the limit
    for msg in reversed(conversation_msgs):
        msg_tokens = get_message_token_count(msg)
        if current_tokens + msg_tokens <= target_limit:
            result.insert(
                -len([m for m in result if not isinstance(m, SystemMessage)])
                or len(result),
                msg,
            )
            current_tokens += msg_tokens
        else:
            break

    # Ensure we have at least one conversation message if possible
    if len(result) <= 1 and conversation_msgs:  # Only system message or empty
        # Take the most recent message even if it's large
        most_recent = conversation_msgs[-1]
        if get_message_token_count(most_recent) <= target_limit - system_tokens:
            result.append(most_recent)

    final_tokens = sum(get_message_token_count(msg) for msg in result)
    logger.info(
        f"Final reduction: {len(all_messages)} -> {len(result)} messages ({final_tokens} tokens)"
    )

    # Final safety check
    if final_tokens > CONTEXT_CONFIG["max_total_tokens"]:
        logger.error(
            f"CRITICAL: Final token count {final_tokens} exceeds absolute limit!"
        )
        # Emergency fallback - keep only system message and most recent user message
        if system_msg and conversation_msgs:
            return [system_msg, conversation_msgs[-1]]
        elif system_msg:
            return [system_msg]
        else:
            return [conversation_msgs[-1]] if conversation_msgs else []

    return result


# Define the state with smart context management
class State(TypedDict):
    messages: Annotated[list, smart_message_reducer]


def create_graph_with_checkpointer(llm_with_tools, tools):
    """Create the LangGraph workflow with checkpointer and query evaluation using the same pattern as working app.py"""
    workflow = StateGraph(State)

    def query_evaluation_node(state: State):
        """Evaluate if the user's query is EDA-related before processing using LLM intelligence with conversation context"""
        messages = state["messages"]

        # Get the last human message
        last_human_message = None
        for msg in reversed(messages):
            if isinstance(msg, HumanMessage):
                last_human_message = msg
                break

        if not last_human_message:
            logger.warning("🚫 No human message found for evaluation")
            return {
                "messages": [
                    AIMessage(
                        content="I didn't receive a valid question. Please ask me about EDA research."
                    )
                ]
            }

        user_query = last_human_message.content
        logger.info(f"🔍 Evaluating query: {user_query}")

        # Ensure user_query is a string for processing
        if isinstance(user_query, list):
            user_query = " ".join(str(item) for item in user_query)
        elif not isinstance(user_query, str):
            user_query = str(user_query)

        # Build conversation context from recent messages (leveraging smart_message_reducer's work)
        context_messages = []
        recent_messages = messages[
            -8:
        ]  # Get recent messages (smart_message_reducer already filtered these)

        for msg in recent_messages:
            if isinstance(msg, HumanMessage):
                context_messages.append(f"User: {msg.content}")
            elif isinstance(msg, AIMessage) and msg.content:
                # Truncate long AI responses for context
                content = str(msg.content)
                if len(content) > 200:
                    content = content[:200] + "..."
                context_messages.append(f"Assistant: {content}")

        conversation_context = (
            "\n".join(context_messages[-6:])
            if context_messages
            else "No previous conversation"
        )

        # Use context-aware LLM-based evaluation
        try:
            # Enhanced evaluation prompt that includes conversation context
            evaluation_prompt = CONTEXT_AWARE_QUERY_EVALUATION_PROMPT.format(
                context=conversation_context, query=user_query
            )

            # Use a basic LLM call for evaluation (without tools)
            from langchain_core.messages import (
                SystemMessage,
                HumanMessage as LCHumanMessage,
            )

            evaluation_response = llm_with_tools.invoke(
                [
                    SystemMessage(
                        content="You are a strict academic research scope evaluator with context awareness."
                    ),
                    LCHumanMessage(content=evaluation_prompt),
                ]
            )

            response_content = evaluation_response.content.strip()
            logger.info(f"🤖 Context-aware LLM evaluation: {response_content}")

            # Extract decision from response
            is_eda_related = False
            if "DECISION: RELEVANT" in response_content:
                is_eda_related = True
                logger.info("✅ LLM judged query as EDA-relevant (with context)")
            elif "DECISION: IRRELEVANT" in response_content:
                is_eda_related = False
                logger.info("❌ LLM judged query as off-topic (with context)")
            else:
                is_eda_related = False
                logger.warning(
                    "⚠️ LLM response format unclear, defaulting to irrelevant"
                )

        except Exception as e:
            logger.error(f"Error in context-aware LLM query evaluation: {e}")
            is_eda_related = False  # Default to irrelevant on error

        # If not EDA-related, return polite rejection
        if not is_eda_related:
            rejection_message = f"""I only answer questions about EDA (Estimation of Distribution Algorithms) research. Please ask about EDAs, algorithms, or related research topics."""
            logger.info("🚫 Rejecting off-topic query")
            return {"messages": [AIMessage(content=rejection_message)]}

        # If EDA-related, proceed to agent (return current state)
        logger.info("✅ Query approved, proceeding to agent")
        return state

    def route_after_evaluation(state: State) -> str:
        """Route after query evaluation - either to agent or end"""
        last_message = state["messages"][-1]

        logger.info(f"🔀 ROUTING DECISION - Last message type: {type(last_message)}")
        logger.info(
            f"🔀 ROUTING DECISION - Last message content: {str(last_message.content)[:100]}..."
        )

        # If the last message is a rejection (from query_evaluation_node), end
        if (
            isinstance(last_message, AIMessage)
            and last_message.content
            and "I only answer questions about EDA" in last_message.content
        ):
            logger.info("🚫 Routing to END due to query rejection")
            return END

        # Otherwise, proceed to agent
        logger.info("➡️ Routing to agent")
        return "agent"

    def agent_node(state: State):
        """Process messages through the agent node with proper system message handling"""
        # The LLM invocation might return a single AIMessage or a list
        # Ensure it's always a list for add_messages
        logger.info(f"🤖 AGENT_NODE INPUT: {len(state['messages'])} messages")
        logger.debug(
            f"SYSTEM_MESSAGE_CONTENT constant in graph_state.py:\n{SYSTEM_MESSAGE_CONTENT[:500]}..."
        )

        # Ensure system message is always present and properly formatted
        messages = state["messages"]
        has_system_message = any(isinstance(msg, SystemMessage) for msg in messages)

        if not has_system_message:
            system_message = SystemMessage(content=SYSTEM_MESSAGE_CONTENT)
            messages = [system_message] + messages
            logger.info("🤖 Added system message to conversation context")
        else:
            # Ensure the system message is at the beginning
            system_msg = next(msg for msg in messages if isinstance(msg, SystemMessage))
            messages = [system_msg] + [
                msg for msg in messages if not isinstance(msg, SystemMessage)
            ]
            logger.info("🤖 Reordered messages to ensure system message is first")

        # Log the messages being sent to the LLM
        for i, msg in enumerate(messages):
            logger.info(
                f"🤖 Message {i} to LLM: {type(msg).__name__} - {str(msg.content)[:250]}..."
            )

        response = llm_with_tools.invoke(messages)
        logger.info(f"🤖 AGENT_NODE RAW LLM OUTPUT Type: {type(response)}")
        if hasattr(response, "content"):
            logger.info(
                f"🤖 AGENT_NODE RAW LLM OUTPUT Content: {str(response.content)[:500]}..."
            )
        if hasattr(response, "tool_calls") and response.tool_calls:
            logger.info(
                f"🤖 AGENT_NODE RAW LLM OUTPUT Tool Calls: {response.tool_calls}"
            )

        logger.info(
            f"🤖 AGENT_NODE OUTPUT (after processing): {type(response)} - {str(response.content)[:100]}..."
        )

        if hasattr(response, "tool_calls") and response.tool_calls:
            logger.info(f"🤖 AGENT MAKING TOOL CALLS: {len(response.tool_calls)} calls")
            for i, call in enumerate(response.tool_calls):
                logger.info(
                    f"🤖 Tool Call {i}: {call['name']} with args: {call.get('args', {})}"
                )

        return {"messages": [response] if not isinstance(response, list) else response}

    def route_tools(state: State) -> str:
        """Route to tools if the last message has tool calls, otherwise end"""
        last_message = state["messages"][-1]
        logger.info(f"🔧 TOOLS ROUTING - Message type: {type(last_message)}")
        logger.info(
            f"🔧 TOOLS ROUTING - Has tool calls: {hasattr(last_message, 'tool_calls') and bool(last_message.tool_calls)}"
        )

        if isinstance(last_message, AIMessage) and last_message.tool_calls:
            logger.info(
                f"🔧 Routing to tools for {len(last_message.tool_calls)} tool calls"
            )
            return "tools"
        logger.info("🔧 Routing to END - no tool calls")
        return END

    # Add nodes to the workflow
    workflow.add_node(
        "query_evaluation", query_evaluation_node
    )  # New query evaluation node
    workflow.add_node("agent", agent_node)  # LLM node
    workflow.add_node("tools", ToolNode(tools=tools))  # Tool node

    # Set entry point to query evaluation
    workflow.set_entry_point("query_evaluation")

    # Route from query evaluation with explicit node names
    workflow.add_conditional_edges(
        "query_evaluation",
        route_after_evaluation,
        {"agent": "agent", END: END},  # Explicit mapping
    )

    # Route from agent (same as before)
    workflow.add_conditional_edges(
        "agent",
        route_tools,  # Route to tools or END
        {"tools": "tools", END: END},  # Explicit mapping
    )

    # Simple path: tools -> agent (same as before)
    workflow.add_edge("tools", "agent")

    memory = MemorySaver()
    graph = workflow.compile(checkpointer=memory)
    return graph
