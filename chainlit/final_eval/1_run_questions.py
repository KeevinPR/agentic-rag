import asyncio
from time import sleep
import json
import os
from typing import Any, Dict, List, Tuple, Optional
import sys
from pathlib import Path
import logging
import re
import glob
import argparse
from datetime import datetime

parent_dir = str(Path(__file__).parent.parent.absolute())
sys.path.append(parent_dir)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Import your existing helper functions & configurations
from utils import init_llm, get_config, close_pg_pool
from tools import (
    init_vector_stores,
    hybrid_search_tool,
    paper_database_tool,
    web_search_tool,
)
from toolsv2 import (
    enhanced_hybrid_search_tool,
    enhanced_web_search_tool,
)
from prompts import (
    SYSTEM_MESSAGE_CONTENT,
    GEMINI_EDA_PROMPT_ENHANCED,
    GEMINI_EDA_PROMPT_ENHANCED_V2,
    GEMINI_EDA_PROMPT_AGENTIC_V3,
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V1,
    GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V2,
)
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.runnables import RunnableConfig


class QuestionProcessor:
    """Enhanced question processor with better error handling and state management"""

    def __init__(
        self,
        output_dir: str,
    ):
        self.output_dir = output_dir
        self.logs_dir = os.path.join(output_dir, "logs")
        self.agent = None
        self.llm = None
        self.tools = None
        self.config = None

    async def initialize(self):
        """Initialize all components needed for processing"""
        try:
            # 1. Initialize LLM
            self.llm = init_llm()
            logger.info("✅ LLM initialized.")

            # 2. Initialize vector stores if needed
            # await init_vector_stores()
            # logger.info("✅ Vector stores initialized.")

            # 3. Create tools with LLM
            self.tools = [
                # hybrid_search_tool,
                # web_search_tool,
                # paper_database_tool,
                enhanced_hybrid_search_tool,
                enhanced_web_search_tool,
                paper_database_tool,
            ]
            logger.info(
                f"✅ {len(self.tools)} tools created: {[t.name for t in self.tools]}"
            )

            # 4. Build the LangGraph ReAct agent
            self.agent = create_react_agent(
                model=self.llm,
                tools=self.tools,
                prompt=GEMINI_EDA_PROMPT_REACT_OPTIMIZED_V2,
                checkpointer=MemorySaver(),
                version="v2",
                debug=True,
            )
            logger.info("✅ ReAct agent created.")

            # 5. Ensure output directories exist
            os.makedirs(self.output_dir, exist_ok=True)
            os.makedirs(self.logs_dir, exist_ok=True)

        except Exception as e:
            logger.error(f"❌ Failed to initialize components: {e}")
            raise

    def parse_hybrid_search_content(self, content: Any) -> List[str]:
        """
        Parse hybrid search tool output, handling both JSON (V2) and text (V1) formats.
        """
        contexts = []
        if not isinstance(content, str):
            content = str(content)

        # Try to parse as JSON (V2 enhanced tool format) first
        try:
            data = json.loads(content)
            results = data.get("results", [])

            for result in results:
                result_content = result.get("content", "")
                if not result_content:
                    continue

                # Clean the V2 formatted content to get raw text
                lines = result_content.split("\n")
                content_start_index = 0
                if lines and lines[0].strip().startswith("**Chunk"):
                    content_start_index += 1
                if len(lines) > content_start_index and lines[
                    content_start_index
                ].strip().startswith("*Domain"):
                    content_start_index += 1

                raw_content = "\n".join(lines[content_start_index:]).strip()

                # Also remove the "passage:" prefix if it exists
                raw_content = re.sub(
                    r"^passage:\s*", "", raw_content, flags=re.IGNORECASE
                )

                if raw_content:
                    contexts.append(raw_content)

        except json.JSONDecodeError:
            # Fallback to legacy text parsing (V1 tool format)
            logger.debug("Content is not JSON, falling back to legacy text parsing.")
            chunks = re.split(r"\n\s*Chunk \d+:\s*\n", content)
            for chunk in chunks[1:]:  # Skip header/summary
                if chunk.strip():
                    clean_chunk = chunk.strip()
                    # Remove "passage:" prefix if present from older formats
                    clean_chunk = re.sub(r"^passage:\s*", "", clean_chunk)
                    contexts.append(clean_chunk)

        return contexts

    def parse_paper_database_content(self, content: Any) -> List[str]:
        """Parse paper database tool output into individual paper contexts"""
        contexts = []

        # Convert content to string if it's a list
        if isinstance(content, list):
            content = " ".join(str(item) for item in content)
        elif not isinstance(content, str):
            content = str(content)

        # Split by TITLE: markers
        papers = re.split(r"TITLE:", content)

        for paper in papers[1:]:  # Skip the header
            if paper.strip():
                # Clean up the paper entry
                clean_paper = paper.strip()
                if clean_paper:
                    # Add back the TITLE: prefix
                    contexts.append(f"TITLE:{clean_paper}")

        return contexts

    def parse_web_search_content(self, content: Any) -> List[str]:
        """
        Parse enhanced web search tool output, splitting each result into a separate context.
        This is better for Ragas evaluation.
        """
        if isinstance(content, list):
            content = " ".join(str(item) for item in content)
        elif not isinstance(content, str):
            content = str(content)

        if not content.strip():
            return []

        # Split the content by the start of each result block, which is marked by "### ".
        # The lookahead `(?=...)` ensures the delimiter is kept with the result.
        result_blocks = re.split(r"\n(?=###\s+)", content)
        contexts = []

        if not result_blocks:
            return [content] if content.strip() else []

        # Check if the first block is a header or a result itself
        first_block = result_blocks[0].strip()
        blocks_to_process = result_blocks

        if not first_block.startswith("###"):
            # This is a header block. Extract the "Key Insight" if it exists.
            insight_match = re.search(
                r"💡\s*\*\*Key Insight:\*\*(.*)", first_block, re.DOTALL
            )
            if insight_match:
                insight_text = insight_match.group(1).strip()
                if insight_text:
                    contexts.append(insight_text)
            # Process the remaining blocks
            blocks_to_process = result_blocks[1:]

        for block in blocks_to_process:
            if block.strip():
                contexts.append(block.strip())

        # Fallback to old behavior if parsing somehow fails to produce contexts
        if not contexts and content.strip():
            return [content.strip()]

        return contexts

    def process_tool_message(
        self,
        msg: ToolMessage,
        hybrid_contexts: List[str],
        paper_contexts: List[str],
        web_contexts: List[str],
    ) -> None:
        """Process individual tool messages to extract contexts"""
        if not hasattr(msg, "content") or not msg.content:
            return

        tool_name = getattr(msg, "name", "unknown")
        content = msg.content

        if tool_name in ["hybrid_search_tool", "enhanced_hybrid_search_tool"]:
            contexts = self.parse_hybrid_search_content(content)
            hybrid_contexts.extend(contexts)
            logger.debug(
                f"📝 Extracted {len(contexts)} hybrid search contexts from {tool_name}"
            )

        elif tool_name == "paper_database_tool":
            contexts = self.parse_paper_database_content(content)
            paper_contexts.extend(contexts)
            logger.debug(f"📄 Extracted {len(contexts)} paper database contexts")

        elif tool_name in ["web_search_tool", "enhanced_web_search_tool"]:
            contexts = self.parse_web_search_content(content)
            web_contexts.extend(contexts)
            logger.debug(
                f"🌐 Extracted {len(contexts)} web search contexts from {tool_name}"
            )

    def extract_tool_calls_from_message(self, msg: AIMessage) -> List[Dict[str, Any]]:
        """Extract tool calls from an AIMessage"""
        tool_calls = []

        # Check for tool_calls attribute first
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for tc in msg.tool_calls:
                if isinstance(tc, dict):
                    name = tc.get("function", {}).get("name") or tc.get("name", "")
                    if not name:  # Skip if no name found
                        continue
                    args = tc.get("function", {}).get("arguments") or tc.get("args", {})
                    if isinstance(args, str):
                        try:
                            args = json.loads(args)
                        except:
                            args = {"raw_args": args}
                    tool_calls.append({"name": name, "args": args})

        # Then check content for tool usage
        elif isinstance(msg.content, list):
            for item in msg.content:
                if isinstance(item, dict) and item.get("type") == "tool_use":
                    name = item.get("name", "")
                    if not name:
                        continue
                    args = item.get("input", {})
                    tool_calls.append({"name": name, "args": args})

        return tool_calls

    def get_last_processed_question(self) -> int:
        """Find the last processed question number from the output directory."""
        if not os.path.exists(self.logs_dir):
            return 0

        # Get all question_*.json files
        pattern = os.path.join(self.logs_dir, "question_*.json")
        files = glob.glob(pattern)

        if not files:
            return 0

        # Extract question numbers and find the highest
        question_numbers = []
        for file in files:
            match = re.match(r"question_(\d+)\.json", os.path.basename(file))
            if match:
                question_numbers.append(int(match.group(1)))

        return max(question_numbers) if question_numbers else 0

    def is_only_tool_call_response(self, msg: AIMessage) -> bool:
        """Check if the response only contains a tool call without actual answer"""
        if not hasattr(msg, "content") or not isinstance(msg.content, str):
            return False

        content = msg.content.strip()
        return (
            content.startswith("<function>") and content.endswith("</function>")
        ) or (
            content.startswith("I'll")
            and "search" in content.lower()
            and len(content) < 100
        )

    def extract_final_answer(self, messages: List[Any]) -> str:
        """Extract final answer from the last agent message"""
        if not messages:
            return ""

        last_msg = messages[-1]
        if not hasattr(last_msg, "content"):
            return ""

        if isinstance(last_msg.content, str):
            return last_msg.content
        elif isinstance(last_msg.content, list):
            # Handle case where content is a list of content blocks
            for block in last_msg.content:
                if isinstance(block, dict) and block.get("type") == "text":
                    return block.get("text", "")
                elif isinstance(block, str):
                    return block

        return ""

    def make_chunk_serializable(self, chunk: Dict[str, Any]) -> Dict[str, Any]:
        """Convert chunk to JSON-serializable format"""
        serializable_chunk: Dict[str, Any] = {}

        for k, v in chunk.items():
            if hasattr(v, "dict"):
                serializable_chunk[k] = v.dict()
            elif isinstance(v, list) and all(hasattr(x, "dict") for x in v):
                serializable_chunk[k] = [x.dict() for x in v]
            else:
                try:
                    json.dumps(v)
                    serializable_chunk[k] = v
                except (TypeError, ValueError):
                    serializable_chunk[k] = repr(v)

        return serializable_chunk

    async def process_single_question(
        self,
        question_idx: int,
        question_data: Dict[str, Any],
        max_retries: int = 3,
        retry_delay: int = 5,
    ) -> Dict[str, Any]:
        """Process a single question with enhanced error handling"""

        question_text = question_data["question"]
        reference_text = question_data.get("golden_chunk", "")
        ground_truth_text = question_data.get("ground_truth", "")
        complexity = question_data.get("complexity", "")
        question_type = question_data.get("question_type", "")
        topics = question_data.get("topics", [])
        generation_style = question_data.get("generation_style", "")
        generated_at = question_data.get("generated_at", "")
        chunk_source = question_data.get("chunk_source", "")
        paper_id = question_data.get("paper_id", "")

        logger.info(f"🔄 Processing question {question_idx}: {question_text!r}")

        # Initialize context lists for this question
        hybrid_search_contexts = []
        paper_database_contexts = []
        web_search_contexts = []
        all_tool_calls = []
        chunks: List[Dict[str, Any]] = []
        last_messages = None

        input_payload = {"messages": [("human", question_text)]}

        # Retry logic with exponential backoff
        for attempt in range(max_retries):
            try:
                if not self.agent:
                    raise RuntimeError(
                        "Agent is not initialized. Cannot process question."
                    )
                logger.info(
                    f"🚀 Starting attempt {attempt + 1}/{max_retries} for question {question_idx}"
                )

                # Reset for each attempt
                chunks_this_attempt = []

                async for chunk in self.agent.astream(
                    input_payload,
                    config=await get_config(),  # type: ignore
                ):
                    logger.debug(f"📦 Received chunk type: {type(chunk)}")

                    if isinstance(chunk, dict):
                        logger.debug(f"📦 Chunk keys: {list(chunk.keys())}")

                    chunks_this_attempt.append(chunk)

                    # Process messages from the chunk
                    if isinstance(chunk, dict):
                        # Handle agent output
                        if "agent" in chunk:
                            agent_output = chunk["agent"]
                            logger.debug(f"🤖 Agent output type: {type(agent_output)}")

                            if isinstance(agent_output, dict):
                                if "messages" in agent_output:
                                    messages = agent_output["messages"]
                                    logger.debug(
                                        f"📝 Found {len(messages)} messages in agent output"
                                    )

                                    for i, msg in enumerate(messages):
                                        logger.debug(
                                            f"📝 Message {i} type: {type(msg)}"
                                        )

                                        if isinstance(msg, AIMessage):
                                            # Extract tool calls
                                            tool_calls = (
                                                self.extract_tool_calls_from_message(
                                                    msg
                                                )
                                            )
                                            logger.debug(
                                                f"🔧 Found {len(tool_calls)} tool calls in AI message"
                                            )
                                            all_tool_calls.extend(tool_calls)
                                            last_messages = [msg]

                                        elif isinstance(msg, ToolMessage):
                                            logger.debug(
                                                f"🛠️ Tool Message name: {getattr(msg, 'name', 'unknown')}"
                                            )
                                            self.process_tool_message(
                                                msg,
                                                hybrid_search_contexts,
                                                paper_database_contexts,
                                                web_search_contexts,
                                            )

                                elif "content" in agent_output:
                                    # Handle direct content in agent output
                                    logger.debug(
                                        "🤖 Found direct content in agent output"
                                    )
                                    msg = AIMessage(content=agent_output["content"])
                                    tool_calls = self.extract_tool_calls_from_message(
                                        msg
                                    )
                                    all_tool_calls.extend(tool_calls)
                                    last_messages = [msg]

                        # Handle tools output
                        if "tools" in chunk:
                            tools_output = chunk["tools"]
                            logger.debug(f"🛠️ Tools output type: {type(tools_output)}")

                            if (
                                isinstance(tools_output, dict)
                                and "messages" in tools_output
                            ):
                                tool_messages = tools_output["messages"]
                                logger.debug(
                                    f"🛠️ Found {len(tool_messages)} tool messages"
                                )

                                for msg in tool_messages:
                                    if isinstance(msg, ToolMessage):
                                        logger.debug(
                                            f"🛠️ Processing tool message: {getattr(msg, 'name', 'unknown')}"
                                        )
                                        self.process_tool_message(
                                            msg,
                                            hybrid_search_contexts,
                                            paper_database_contexts,
                                            web_search_contexts,
                                        )

                # Check if we got a valid response
                if last_messages and len(last_messages) > 0:
                    last_msg = last_messages[0]

                    # Check if response is only a tool call (incomplete)
                    if self.is_only_tool_call_response(last_msg):
                        logger.warning(
                            f"⚠️ Incomplete response for question {question_idx} on attempt {attempt + 1}"
                        )
                        if attempt < max_retries - 1:
                            wait_time = retry_delay * (
                                2**attempt
                            )  # Exponential backoff
                            logger.info(f"Retrying after {wait_time}s delay...")
                            await asyncio.sleep(wait_time)
                            continue
                        else:
                            logger.error(
                                f"❌ All attempts failed for question {question_idx}"
                            )
                    else:
                        # Success - we have a complete response
                        chunks.extend(chunks_this_attempt)
                        break
                else:
                    logger.warning(
                        f"⚠️ No messages found for question {question_idx} on attempt {attempt + 1}"
                    )
                    if attempt < max_retries - 1:
                        wait_time = retry_delay * (2**attempt)
                        await asyncio.sleep(wait_time)
                        continue

            except Exception as e:
                logger.error(
                    f"❌ Error on question {question_idx} attempt {attempt + 1}: {e}"
                )
                if attempt < max_retries - 1:
                    wait_time = retry_delay * (2**attempt)
                    logger.info(f"Retrying after {wait_time}s delay...")
                    await asyncio.sleep(wait_time)
                else:
                    logger.error(
                        f"❌ All attempts failed for question {question_idx}: {e}"
                    )
                    # Return error result
                    return {
                        "question": question_text,
                        "ground_truth": ground_truth_text,
                        "reference": reference_text,
                        "complexity": complexity,
                        "question_type": question_type,
                        "topics": topics,
                        "generation_style": generation_style,
                        "generated_at": generated_at,
                        "chunk_source": chunk_source,
                        "paper_id": paper_id,
                        "final_answer": f"ERROR: Failed after {max_retries} attempts: {str(e)}",
                        "chunks": [],
                        "contexts": {
                            "hybrid_search": [],
                            "paper_database": [],
                            "web_search": [],
                        },
                        "tool_calls": [],
                        "error": True,
                        "timestamp": datetime.now().isoformat(),
                    }

        # Extract final answer
        final_answer = self.extract_final_answer(last_messages) if last_messages else ""

        # Build result entry
        result = {
            "question": question_text,
            "ground_truth": ground_truth_text,
            "reference": reference_text,
            "final_answer": final_answer,
            "complexity": complexity,
            "question_type": question_type,
            "topics": topics,
            "generation_style": generation_style,
            "generated_at": generated_at,
            "chunk_source": chunk_source,
            "paper_id": paper_id,
            "chunks": [],
            "contexts": {
                "hybrid_search": hybrid_search_contexts,
                "paper_database": paper_database_contexts,
                "web_search": web_search_contexts,
            },
            "tool_calls": all_tool_calls,
            "error": False,
            "timestamp": datetime.now().isoformat(),
        }

        # Process chunks for serialization
        for chunk in chunks:
            serializable_chunk = self.make_chunk_serializable(chunk)
            result["chunks"].append(serializable_chunk)

        # Save individual question result
        output_file = os.path.join(self.logs_dir, f"question_{question_idx}.json")
        logger.info(f"💾 Saving results to {output_file}")

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        logger.info(f"✅ Completed question {question_idx}")
        return result

    async def run_questions(
        self,
        questions_file: str,
        question_number: Optional[int] = None,
        delay_between_questions: int = 10,
        max_questions: Optional[int] = None,
    ):
        """Main method to run all or specific questions"""

        # Load questions
        try:
            with open(questions_file, "r", encoding="utf-8") as f:
                json_data = json.load(f)
            question_list: List[Dict[str, Any]] = json_data["questions"]
            logger.info(
                f"✅ Loaded {len(question_list)} questions from {questions_file}"
            )
        except Exception as e:
            logger.error(f"❌ Failed to load questions from {questions_file}: {e}")
            return

        # Determine which questions to process
        if question_number is not None:
            # Process only the specified question
            if 1 <= question_number <= len(question_list):
                questions_to_process = [
                    (question_number, question_list[question_number - 1])
                ]
                logger.info(f"🎯 Processing only question {question_number}")
            else:
                logger.error(
                    f"❌ Question number {question_number} is out of range (1-{len(question_list)})"
                )
                return
        else:
            # Find last processed and continue from there
            last_processed = self.get_last_processed_question()
            logger.info(f"📊 Last processed question: {last_processed}")

            remaining_questions = [
                (idx + 1, question_list[idx])
                for idx in range(last_processed, len(question_list))
            ]

            # Apply max_questions limit if specified
            if max_questions is not None:
                remaining_questions = remaining_questions[:max_questions]
                logger.info(f"📝 Limiting to {max_questions} questions")

            questions_to_process = remaining_questions
            logger.info(
                f"🔄 Processing {len(questions_to_process)} remaining questions"
            )

        # Process questions
        results = []

        for question_idx, question_data in questions_to_process:
            try:
                result = await self.process_single_question(question_idx, question_data)
                results.append(result)

                # Add delay between questions (except for the last one)
                if question_idx != questions_to_process[-1][0]:
                    logger.info(
                        f"⏱️ Waiting {delay_between_questions} seconds before next question..."
                    )
                    await asyncio.sleep(delay_between_questions)

            except Exception as e:
                logger.error(
                    f"❌ Unexpected error processing question {question_idx}: {e}"
                )
                # Continue with next question
                continue

        # Save combined results (only if processing multiple questions)
        if question_number is None and results:
            combined_file = os.path.join(self.output_dir, "agent_raw_logs.json")
            logger.info(f"💾 Saving combined results to {combined_file}")

            with open(combined_file, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)

            logger.info("✅ Saved combined agent logs")

        logger.info(f"🎉 Processing complete! Processed {len(results)} questions")

    async def cleanup(self):
        """Clean up resources"""
        try:
            await close_pg_pool()
            logger.info("✅ Closed PostgreSQL pool.")
        except Exception as e:
            logger.warning(f"⚠️ Error closing PostgreSQL pool: {e}")


async def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(description="Process questions for evaluation.")
    parser.add_argument(
        "--question", type=int, help="Process only the specified question number (1-50)"
    )
    parser.add_argument(
        "--questions-file",
        type=str,
        default="/Users/id05309/Documents/tfm/chainlit/final_eval/final-100.json",
        help="Path to the questions JSON file",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="final-v2-100",
        help="Output directory for results",
    )
    parser.add_argument(
        "--delay", type=int, default=5, help="Delay between questions in seconds"
    )
    parser.add_argument(
        "--max-questions", type=int, help="Maximum number of questions to process"
    )
    args = parser.parse_args()

    # Initialize processor
    processor = QuestionProcessor(output_dir=args.output_dir)

    try:
        # Initialize all components
        await processor.initialize()

        # Run questions
        await processor.run_questions(
            questions_file=args.questions_file,
            question_number=args.question,
            delay_between_questions=args.delay,
            max_questions=args.max_questions,
        )

    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        raise
    finally:
        # Cleanup
        await processor.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
