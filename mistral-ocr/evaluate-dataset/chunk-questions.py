import json
import os
import time
import logging
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
import re
import timeout_decorator
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
from datetime import datetime
import random
from pydantic import BaseModel
from typing import List, Optional

# Load environment variables from .env.local
load_dotenv(dotenv_path="/Users/id05309/Documents/tfm/.env.local")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Define paths
CHUNKS_JSON_FILE = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-pure-semantic/all_papers_data_semantic_metadata_cleaned_ids.json"  # Update this path
OUTPUT_FILE = "/Users/id05309/Documents/tfm/mistral/evaluate-dataset/final_500_questions_semantic_v2_chunking.json"


# Add Pydantic model for structured output
class ChunkQuestionAnswer(BaseModel):
    question: str
    answer: str
    question_type: str
    complexity: str
    topics: List[str]


class QuestionDiversityController:
    """Enhanced diversity controller for chunk-based questions."""

    def __init__(self):
        self.question_patterns = set()
        self.used_keywords = set()
        self.question_types = [
            "definition",
            "comparison",
            "process",
            "advantage",
            "challenge",
            "application",
            "theory",
            "implementation",
            "evaluation",
            "relationship",
        ]
        self.complexity_levels = ["basic", "medium", "advanced"]
        self.generated_count = 0

        # Topic categories for better variety
        self.topic_categories = {
            "algorithms": [
                "optimization",
                "evolutionary",
                "genetic",
                "search",
                "heuristic",
            ],
            "theory": ["convergence", "complexity", "analysis", "proof", "bounds"],
            "applications": ["scheduling", "routing", "design", "planning", "control"],
            "methods": [
                "selection",
                "crossover",
                "mutation",
                "initialization",
                "termination",
            ],
            "evaluation": [
                "metrics",
                "benchmarks",
                "comparison",
                "performance",
                "testing",
            ],
            "modeling": [
                "representation",
                "encoding",
                "fitness",
                "objectives",
                "constraints",
            ],
        }

    def get_diverse_prompt_style(self, index):
        """Return different prompt styles for variety."""
        styles = [
            "conceptual_deep",
            "practical_application",
            "theoretical_foundation",
            "comparative_analysis",
            "implementation_focused",
            "evaluation_metrics",
            "synthesis_summary",  # New style for broader questions
        ]
        return styles[index % len(styles)]


def create_chunk_question_prompt(
    chunk_content, paper_info, chunk_id, diversity_controller, question_index
):
    """Create prompts specifically for chunk-based question generation."""

    style = diversity_controller.get_diverse_prompt_style(question_index)
    question_type = diversity_controller.question_types[
        question_index % len(diversity_controller.question_types)
    ]
    complexity = diversity_controller.complexity_levels[
        question_index % len(diversity_controller.complexity_levels)
    ]

    # Extract key topics from the chunk
    content_lower = chunk_content.lower()
    relevant_topics = []
    for category, topics in diversity_controller.topic_categories.items():
        for topic in topics:
            if topic in content_lower:
                relevant_topics.append(topic)

    # Ensure we have a fallback topic
    if not relevant_topics:
        relevant_topics = ["optimization", "algorithm"]

    main_topic = random.choice(relevant_topics[:3]) if relevant_topics else "algorithm"

    prompt_templates = {
        "conceptual_deep": f"""
You are an expert in {main_topic} for Estimation of Distribution Algorithms (EDAs) creating a DEEP CONCEPTUAL question about the algorithmic principles and theoretical foundations of EDAs.

Based ONLY on the provided content chunk, generate exactly ONE question-answer pair. The question must be self-contained and assume no prior knowledge of the topic beyond what is in the chunk.

The question should explore ONE of the following:
- Core algorithmic mechanisms of an EDA and their theoretical basis.
- Mathematical principles underlying an EDA's computational methods.
- Conceptual relationships between different EDA approaches mentioned.
- Fundamental properties that make a specific EDA model effective.

QUESTION STARTERS (choose the most appropriate):
- "Within the framework of Estimation of Distribution Algorithms, what mathematical principles govern..."
- "In the context of EDAs, how does the algorithmic mechanism of..."
- "From a theoretical standpoint for EDAs, what foundation explains why..."
- "For the specific EDAs mentioned, what fundamental properties distinguish..."

ANSWER REQUIREMENTS:
- Extract specific EDA names, mathematical formulas, and technical terms directly from the chunk.
- Explain the underlying mathematical or theoretical principles as described in the text.
- Use the precise technical vocabulary found in the content.
- Provide concrete algorithmic details from the chunk, not abstract generalizations.

CRITICAL CONSTRAINTS:
- The question MUST be specific to Estimation of Distribution Algorithms (EDAs).
- The question and answer must be entirely answerable using ONLY the provided chunk_content.
- NEVER reference "this paper", "the authors", "the study", or similar external-sourcing phrases.
- The question must focus on specific algorithms, models, or methods mentioned in the chunk.
- If using mathematical notation, explain it in plain English as presented in the chunk.
- Complexity level: {complexity}

<chunk_content>
{chunk_content}
</chunk_content>

Generate a JSON response with one question-answer pair.
""",
        "synthesis_summary": f"""
You are a research analyst creating a high-level SYNTHESIS question that captures the main idea or purpose of a text segment on {main_topic} for Estimation of Distribution Algorithms (EDAs).

Based ONLY on the provided content chunk, generate exactly ONE question-answer pair. The question should be self-contained and require understanding the overall point of the chunk, not just one specific detail.

The question should address ONE of the following:
- The primary goal or contribution described in the chunk.
- The main conclusion or finding presented.
- The overall methodology being proposed or analyzed.
- The key takeaway a reader should have after reading this chunk.

QUESTION STARTERS (choose the most appropriate):
- "What is the primary objective of the methodology described in the context of EDAs..."
- "Based on the text, what is the main conclusion regarding the performance of the EDA model..."
- "What is the key takeaway about the application of the specific EDA discussed..."
- "In essence, what is the overall purpose of the algorithmic approach detailed for EDAs..."

ANSWER REQUIREMENTS:
- Synthesize the core message of the chunk, not just a direct quote.
- The answer should reflect a holistic understanding of the text provided.
- Name the specific algorithms or concepts being discussed.
- Use the precise technical vocabulary found in the content.

CRITICAL CONSTRAINTS:
- The question MUST be specific to Estimation of Distribution Algorithms (EDAs).
- The question and answer must be entirely answerable using ONLY the provided chunk_content.
- NEVER reference "this paper", "the authors", "the study", or similar external-sourcing phrases.
- The question must focus on the broader implications within the chunk.
- Complexity level: {complexity}

<chunk_content>
{chunk_content}
</chunk_content>

Generate a JSON response with one question-answer pair.
""",
        "practical_application": f"""
You are a practitioner of {main_topic} for Estimation of Distribution Algorithms (EDAs) creating a PRACTICAL APPLICATION question about the implementation and usage of EDAs.

Based ONLY on the provided content chunk, generate exactly ONE question-answer pair. The question must be self-contained and assume no prior knowledge of the topic beyond what is in the chunk.

The question should address ONE of the following:
- Specific implementation steps for an EDA mentioned.
- Parameter selection and configuration guidance for an EDA.
- Scenarios where a particular EDA approach is best applied.
- Practical considerations for deploying an EDA model.

QUESTION STARTERS (choose the most appropriate):
- "For implementing an Estimation of Distribution Algorithm, how should practitioners..."
- "When configuring an EDA, what parameter settings optimize..."
- "In which practical scenarios does the EDA model X outperform..."
- "What specific implementation steps are required for the EDA named..."

ANSWER REQUIREMENTS:
- Include specific EDA names, parameter values, and implementation details from the chunk.
- Provide concrete steps, thresholds, or configuration guidelines mentioned in the text.
- Reference specific computational procedures or data structures as described.
- Give actionable technical guidance using precise terminology from the chunk.

CRITICAL CONSTRAINTS:
- The question MUST be specific to Estimation of Distribution Algorithms (EDAs).
- The question and answer must be entirely answerable using ONLY the provided chunk_content.
- NEVER reference "this paper", "the authors", "the study", or similar external-sourcing phrases.
- The question must address specific algorithms or procedures in the chunk.
- Complexity level: {complexity}

<chunk_content>
{chunk_content}
</chunk_content>

Generate a JSON response with one question-answer pair.
""",
        "theoretical_foundation": f"""
You are a theoretical computer scientist creating a MATHEMATICAL ANALYSIS question about the guarantees and complexity of {main_topic} for Estimation of Distribution Algorithms (EDAs).

Based ONLY on the provided content chunk, generate exactly ONE question-answer pair. The question must be self-contained and assume no prior knowledge of the topic beyond what is in the chunk.

The question should examine ONE of the following:
- Convergence conditions and mathematical proofs for an EDA.
- Computational complexity analysis of a specific EDA.
- Theoretical performance guarantees for an EDA model.
- Mathematical properties of an EDA's optimization method.

QUESTION STARTERS (choose the most appropriate):
- "Regarding the EDA discussed, under what mathematical conditions does..."
- "What convergence guarantees, if any, are described for the EDA model..."
- "How is the computational complexity of the specific EDA analyzed..."
- "What theoretical bounds are established for the performance of the EDA..."

ANSWER REQUIREMENTS:
- Include specific theorems, complexity notations, or proof techniques mentioned in the chunk.
- Reference the exact convergence conditions, bounds, or theoretical results provided.
- Use precise mathematical terminology and complexity measures from the content.
- Provide concrete mathematical statements, not vague claims.

CRITICAL CONSTRAINTS:
- The question MUST be specific to Estimation of Distribution Algorithms (EDAs).
- The question and answer must be entirely answerable using ONLY the provided chunk_content.
- NEVER reference "this paper", "the authors", "the study", or similar external-sourcing phrases.
- The question must address specific mathematical properties or results in the chunk.
- For every mathematical concept, include its descriptive context from the chunk.
- Complexity level: {complexity}

<chunk_content>
{chunk_content}
</chunk_content>

Generate a JSON response with one question-answer pair.
""",
        "comparative_analysis": f"""
You are an algorithmic analyst creating a COMPARATIVE EVALUATION question about different {main_topic} for Estimation of Distribution Algorithms (EDAs).

Based ONLY on the provided content chunk, generate exactly ONE question-answer pair. The question must be self-contained and assume no prior knowledge of the topic beyond what is in the chunk.

The question should compare ONE of the following:
- Performance characteristics between specific EDAs.
- Trade-offs in efficiency or accuracy between different EDA models.
- The advantages and limitations of different EDA strategies.
- Scenarios where one EDA outperforms another.

QUESTION STARTERS (choose the most appropriate):
- "How does the performance of EDA model X compare to EDA model Y, based on the metrics provided..."
- "What computational trade-offs are described between the EDA approaches of..."
- "According to the details in the chunk, what advantages does EDA method A have over method B in..."
- "Under what conditions is the EDA model X shown to outperform..."

ANSWER REQUIREMENTS:
- Name the specific EDA models being compared from the chunk.
- Include the quantitative measures, benchmarks, or performance metrics mentioned.
- Reference exact computational characteristics or results from the text.
- Provide concrete algorithmic differences, not general comparisons.

CRITICAL CONSTRAINTS:
- The question MUST be specific to Estimation of Distribution Algorithms (EDAs).
- The question and answer must be entirely answerable using ONLY the provided chunk_content.
- NEVER reference "this paper", "the authors", "the study", or similar external-sourcing phrases.
- The question must compare specific algorithms or methods mentioned in the chunk.
- Complexity level: {complexity}

<chunk_content>
{chunk_content}
</chunk_content>

Generate a JSON response with one question-answer pair.
""",
        "implementation_focused": f"""
You are a software engineer creating an IMPLEMENTATION DETAILS question about coding {main_topic} for Estimation of Distribution Algorithms (EDAs).

Based ONLY on the provided content chunk, generate exactly ONE question-answer pair. The question must be self-contained and assume no prior knowledge of the topic beyond what is in the chunk.

The question should address ONE of the following:
- Data structures required for a specific EDA.
- The sequence of algorithmic steps for an EDA.
- Programming considerations for an EDA implementation.
- The software architecture described for an EDA.

QUESTION STARTERS (choose the most appropriate):
- "To implement the specific EDA mentioned, what data structures are required..."
- "What are the precise algorithmic steps for executing the EDA model..."
- "How should a developer structure the code for the EDA, based on the description..."
- "What programming techniques are suggested to optimize the EDA's..."

ANSWER REQUIREMENTS:
- Include specific data structure names, algorithmic steps, or code patterns from the chunk.
- Reference the exact programming procedures or optimization techniques detailed in the text.
- Use precise technical terminology for implementation details found in the content.
- Provide concrete coding guidance based on the chunk's description.

CRITICAL CONSTRAINTS:
- The question MUST be specific to Estimation of Distribution Algorithms (EDAs).
- The question and answer must be entirely answerable using ONLY the provided chunk_content.
- NEVER reference "this paper", "the authors", "the study", or similar external-sourcing phrases.
- The question must address implementation aspects of algorithms mentioned in the chunk.
- Complexity level: {complexity}

<chunk_content>
{chunk_content}
</chunk_content>

Generate a JSON response with one question-answer pair.
""",
        "evaluation_metrics": f"""
You are a performance analyst creating an EVALUATION METHODOLOGY question for {main_topic} for Estimation of Distribution Algorithms (EDAs).

Based ONLY on the provided content chunk, generate exactly ONE question-answer pair. The question must be self-contained and assume no prior knowledge of the topic beyond what is in the chunk.

The question should cover ONE of the following:
- Specific metrics for evaluating an EDA's performance.
- The benchmarking procedures described for an EDA.
- Quality assessment criteria for an EDA model.
- Statistical measures used for comparing EDAs.

QUESTION STARTERS (choose the most appropriate):
- "What specific metrics are used to evaluate the effectiveness of the EDA model..."
- "How can the quality of the EDA's output be measured using the criteria of..."
- "What benchmarking approach is outlined to assess the EDA..."
- "What statistical measures are proposed to quantify the performance of the EDA..."

ANSWER REQUIREMENTS:
- Include the specific metric names, statistical measures, or evaluation procedures from the chunk.
- Reference the exact benchmarking datasets or performance indicators mentioned.
- Use precise terminology for evaluation methodologies as found in the content.
- Provide a concrete measurement approach based on the chunk's text.

CRITICAL CONSTRAINTS:
- The question MUST be specific to Estimation of Distribution Algorithms (EDAs).
- The question and answer must be entirely answerable using ONLY the provided chunk_content.
- NEVER reference "this paper", "the authors", "the study", or similar external-sourcing phrases.
- The question must address evaluation methods or metrics mentioned in the chunk.
- Complexity level: {complexity}

<chunk_content>
{chunk_content}
</chunk_content>

Generate a JSON response with one question-answer pair.
""",
    }

    base_prompt = prompt_templates[style]

    # Enhanced formatting with stronger constraints
    full_prompt = f"""{base_prompt}

    JSON FORMAT SPECIFICATION:
    {{
        "question": "Your algorithmically-focused question here",
        "answer": "Your technically precise answer with specific algorithm names and details here"
    }}

    ENHANCED QUALITY CONTROLS:
    ✓ Question must be related to EDAs
    ✓ Include specific algorithm names, mathematical terms, or technical concepts from chunk
    ✓ Use exact parameter names, complexity notations, or performance measures from content  
    ✓ Question reads as domain-expert inquiry, not paper summary request
    ✓ Answer demonstrates deep technical understanding with precise terminology
    ✓ Zero paper-reference language ("this paper", "authors", "study", "according to", etc.)
    ✓ Focus on algorithmic mechanisms, not research context
    ✓ AVOID questions with complex mathematical notation without clear explanations
    ✓ If using math symbols, always provide contextual meaning (e.g., "variable x, which represents the population size")
    ✓ Complexity level: {complexity} - adjust technical depth accordingly

    CONTEXT INFORMATION:
    Paper title: {paper_info.get("title", "Unknown")}
    Chunk ID: {chunk_id}
    Main topic: {main_topic}
    Question style: {style.replace("_", " ")}
    Question type: {question_type}
    """

    return full_prompt


# Define a timeout exception
class GeminiTimeoutError(Exception):
    pass


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(
        (GeminiTimeoutError, ConnectionError, json.JSONDecodeError)
    ),
    reraise=True,
)
@timeout_decorator.timeout(120)
def get_gemini_response(prompt, model="gemini-2.0-flash", max_retries=3):
    """Get response from Gemini with enhanced error handling and structured output."""
    for attempt in range(max_retries):
        try:
            # Try with structured output using Pydantic model
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.6,
                        top_p=0.9,
                        seed=random.randint(1, 10000),
                        max_output_tokens=2048,
                        response_mime_type="application/json",
                        response_schema=list[ChunkQuestionAnswer],
                    ),
                )

                # If successful, get parsed objects directly
                if hasattr(response, "parsed"):
                    parsed_json = response.parsed
                    logger.info(
                        f"Successfully parsed structured response using Pydantic model"
                    )
                    if parsed_json:
                        return json.dumps([qa.model_dump() for qa in parsed_json])

                # If we get here, we have a response but not parsed objects
                logger.info(
                    "Response received but not parsed as structured data, falling back to text"
                )

            except Exception as schema_error:
                logger.warning(
                    f"Structured schema failed: {str(schema_error)}. Falling back to standard format."
                )
                # Fallback to standard format without schema
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.6,
                        top_p=0.9,
                        seed=random.randint(1, 10000),
                        max_output_tokens=2048,
                    ),
                )

            if not response.text:
                raise ValueError("Empty response from Gemini")

            response_text = response.text.strip()
            logger.info(
                f"Raw response from Gemini (first 300 chars): {response_text[:300]}..."
            )

            # Clean markdown formatting
            response_text = re.sub(r"```json\s*", "", response_text)
            response_text = re.sub(r"```\s*$", "", response_text)

            # Extract JSON array
            start_idx = response_text.find("[")
            end_idx = response_text.rfind("]") + 1

            if start_idx == -1 or end_idx == 0:
                logger.error(f"No JSON array found. Response: {response_text[:500]}...")
                raise ValueError("No JSON array found in response")

            json_str = response_text[start_idx:end_idx]
            cleaned_json_str = clean_json_response(json_str)

            # Validate JSON
            parsed_json = json.loads(cleaned_json_str)
            logger.info(f"Successfully parsed JSON with {len(parsed_json)} items")
            return cleaned_json_str

        except Exception as e:
            logger.warning(f"Attempt {attempt + 1}/{max_retries} failed: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(random.uniform(2, 5))  # Random backoff
            else:
                raise GeminiTimeoutError(
                    f"Failed after {max_retries} attempts: {str(e)}"
                )


def clean_json_response(response):
    """Clean JSON response by handling LaTeX formatting and special characters."""
    json_str = response.strip()
    try:
        json.loads(json_str)
        return json_str
    except json.JSONDecodeError:
        # Fix common JSON issues
        json_str = re.sub(r'(?<!\\)\\(?!\\|"|\\/|b|f|n|r|t|u)', r"\\\\", json_str)
        return json_str


def is_question_too_similar(new_question, existing_questions, similarity_threshold=0.7):
    """Check if a new question is too similar to existing ones."""
    new_words = set(new_question.lower().split())

    for existing in existing_questions:
        existing_words = set(existing.lower().split())

        # Calculate Jaccard similarity
        intersection = len(new_words.intersection(existing_words))
        union = len(new_words.union(existing_words))

        if union > 0:
            similarity = intersection / union
            if similarity > similarity_threshold:
                return True

    return False


def load_chunks_data():
    """Load the chunks JSON file."""
    try:
        with open(CHUNKS_JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.info(f"Loaded chunks data with {len(data['papers'])} papers")
        return data
    except Exception as e:
        logger.error(f"Error loading chunks file {CHUNKS_JSON_FILE}: {str(e)}")
        return None


def select_random_chunk(chunks_data):
    """Randomly select a paper and then a chunk from it."""
    papers = chunks_data["papers"]

    # Randomly select a paper
    selected_paper = random.choice(papers)
    paper_info = selected_paper["paper"]
    chunks = selected_paper["chunks"]

    # Randomly select a chunk
    selected_chunk = random.choice(chunks)

    logger.info(f"Selected paper: {paper_info['paper_id']}")
    logger.info(f"Selected chunk: {selected_chunk['chunk_id']}")

    # Replace formula placeholders with actual formulas
    if "page_content" in selected_chunk and "metadata" in selected_chunk:
        if (
            "formulas" in selected_chunk["metadata"]
            and selected_chunk["metadata"]["contains_formula"]
        ):
            content = selected_chunk["page_content"]
            formulas = selected_chunk["metadata"]["formulas"]

            # Replace each formula placeholder with its actual formula
            for placeholder, formula in formulas.items():
                content = content.replace(placeholder, formula)

            # Update the chunk content with formulas replaced
            selected_chunk["page_content"] = content
            logger.info(
                f"Replaced {len(formulas)} formula placeholders in chunk content"
            )

    return paper_info, selected_chunk


def generate_question_from_chunk(
    paper_info, chunk_info, diversity_controller, question_index
):
    """Generate a question from a specific chunk."""
    chunk_content = chunk_info.get("page_content", chunk_info.get("page_content", ""))
    chunk_id = chunk_info["chunk_id"]
    print(f"Generating question for chunk {chunk_id}...")

    if not chunk_content:
        logger.warning(f"No content found in chunk {chunk_id}")
        return None

    if len(chunk_content.strip()) < 100:
        logger.warning(f"Chunk {chunk_id} too short ({len(chunk_content)} chars)")
        return None

    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            prompt = create_chunk_question_prompt(
                chunk_content,
                paper_info,
                chunk_id,
                diversity_controller,
                question_index + attempt,
            )
            response = get_gemini_response(prompt)
            json_str = clean_json_response(response)
            qa_pairs = json.loads(json_str)

            if not isinstance(qa_pairs, list) or len(qa_pairs) != 1:
                logger.warning(f"Unexpected response format on attempt {attempt + 1}")
                continue

            qa = qa_pairs[0]
            if not isinstance(qa, dict) or "question" not in qa or "answer" not in qa:
                logger.warning(f"Invalid QA structure on attempt {attempt + 1}")
                continue

            # Check for forbidden phrases
            question_lower = qa["question"].lower()
            forbidden_phrases = [
                "this paper",
                "the paper",
                "in the paper",
                "the authors",
                "according to the paper",
                "in the study",
                "our approach",
                "we propose",
            ]
            if any(phrase in question_lower for phrase in forbidden_phrases):
                logger.warning(
                    f"Question contains forbidden phrases on attempt {attempt + 1}: {qa['question']}"
                )
                continue

            # Create final item with chunk information
            result_item = {
                "question": qa["question"],
                "topics": qa.get("topics", []),
                "answer": qa["answer"],
                "chunk_id": chunk_id,
                "paper_id": paper_info["paper_id"],
                "paper_title": paper_info.get("title", "Unknown"),
                "paper_year": paper_info.get("year", "Unknown"),
                "chunk_content": chunk_content,
                "question_type": qa.get("question_type", "unknown"),
                "complexity": qa.get("complexity", "medium"),
                "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "generation_style": diversity_controller.get_diverse_prompt_style(
                    question_index + attempt
                ),
            }

            logger.info(f"Successfully generated question from chunk {chunk_id}")
            return result_item

        except Exception as e:
            logger.warning(
                f"Attempt {attempt + 1} failed for chunk {chunk_id}: {str(e)}"
            )
            if attempt < max_attempts - 1:
                time.sleep(1)
                continue

    logger.error(
        f"Failed to generate question from chunk {chunk_id} after {max_attempts} attempts"
    )
    return None


def generate_chunk_based_questions(target_questions=500):
    """Generate questions from randomly selected chunks until the target is reached."""
    dataset = {
        "metadata": {
            "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "target_questions": target_questions,
            "total_questions": 0,
            "generation_method": "chunk_based",
            "statistics": {
                "successful": 0,
                "failed_generation": 0,
                "duplicate_skipped": 0,
                "total_attempts": 0,
            },
        },
        "questions": [],
    }

    # Load chunks data
    chunks_data = load_chunks_data()
    if not chunks_data:
        logger.error("Failed to load chunks data")
        return dataset

    diversity_controller = QuestionDiversityController()

    failed_generation = 0
    duplicate_skipped = 0
    total_attempts = 0
    max_attempts = int(target_questions * 1.5)  # Safety break

    try:
        while (
            len(dataset["questions"]) < target_questions
            and total_attempts < max_attempts
        ):
            current_q_count = len(dataset["questions"])
            total_attempts += 1
            logger.info(
                f"--- Generating question {current_q_count + 1}/{target_questions} (Attempt #{total_attempts}) ---"
            )

            # Select random chunk
            paper_info, chunk_info = select_random_chunk(chunks_data)

            # Generate question
            question_item = generate_question_from_chunk(
                paper_info, chunk_info, diversity_controller, current_q_count
            )

            if not question_item:
                failed_generation += 1
                continue

            # Check for duplicates
            existing_questions = [q["question"] for q in dataset["questions"]]
            if not is_question_too_similar(
                question_item["question"], existing_questions, 0.6
            ):
                dataset["questions"].append(question_item)
                logger.info(
                    f"✅ Added question {len(dataset['questions'])}/{target_questions}"
                )
            else:
                logger.warning("Skipped duplicate question")
                duplicate_skipped += 1

            # Save progress every 10 questions
            if len(dataset["questions"]) % 10 == 0 and len(dataset["questions"]) > 0:
                save_dataset(dataset)

            # Add small delay to avoid rate limiting
            time.sleep(0.2)

    except KeyboardInterrupt:
        logger.info("Generation interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

    if total_attempts >= max_attempts:
        logger.warning(
            f"⚠️ Reached max attempts ({max_attempts}) before hitting target of {target_questions}."
        )

    # Final statistics
    dataset["metadata"]["total_questions"] = len(dataset["questions"])
    dataset["metadata"]["statistics"].update(
        {
            "successful": len(dataset["questions"]),
            "failed_generation": failed_generation,
            "duplicate_skipped": duplicate_skipped,
            "total_attempts": total_attempts,
        }
    )

    save_dataset(dataset)
    logger.info(f"Generated {len(dataset['questions'])} unique questions from chunks")
    return dataset


def save_dataset(dataset):
    """Save the dataset to a JSON file."""
    try:
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)
        logger.info(f"Dataset saved to {OUTPUT_FILE}")
    except Exception as e:
        logger.error(f"Error saving dataset: {str(e)}")
        raise


if __name__ == "__main__":
    # Update the CHUNKS_JSON_FILE path before running
    logger.info("Starting chunk-based question generation...")
    dataset = generate_chunk_based_questions(target_questions=500)
    logger.info(f"Final dataset contains {len(dataset['questions'])} questions")

    # Print summary for verification
    if dataset["questions"]:
        question_types = {}
        complexities = {}
        styles = {}

        for q in dataset["questions"]:
            qtype = q.get("question_type", "unknown")
            complexity = q.get("complexity", "unknown")
            style = q.get("generation_style", "unknown")

            question_types[qtype] = question_types.get(qtype, 0) + 1
            complexities[complexity] = complexities.get(complexity, 0) + 1
            styles[style] = styles.get(style, 0) + 1

        logger.info(f"Question types distribution: {question_types}")
        logger.info(f"Complexity distribution: {complexities}")
        logger.info(f"Style distribution: {styles}")
