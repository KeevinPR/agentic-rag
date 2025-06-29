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
MARKDOWN_DIR = "/Users/id05309/Documents/tfm/mistral/mistral-markdown-no-ref-no-tables"
OUTPUT_FILE = "/Users/id05309/Documents/tfm/mistral/evaluate-dataset/final_golden_chunk_dataset_100.json"


# Add Pydantic model for structured output
class QuestionAnswer(BaseModel):
    question: str
    answer: str
    supporting_chunk: str  # The model will extract a chunk that supports the answer
    question_type: str
    complexity: str
    topics: List[str]


# Add new Pydantic model for Chroma-style multi-reference output
class MultiReferenceAnswer(BaseModel):
    question: str
    answer: str
    reference_spans: List[str]  # Multiple spans like Chroma's approach
    question_type: str
    complexity: str
    topics: List[str]
    span_sources: List[str]  # Source locations for each span


class QuestionDiversityController:
    """Enhanced diversity controller with better tracking and variety."""

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

    def get_diverse_prompt_style(self, paper_index):
        """Return different prompt styles for variety."""
        styles = [
            "conceptual_deep",
            "practical_application",
            "theoretical_foundation",
            "comparative_analysis",
            "implementation_focused",
            "evaluation_metrics",
        ]
        return styles[paper_index % len(styles)]

    # def get_question_starter(self, style, used_starters=None):
    #     """Get diverse question starters based on style."""
    #     if used_starters is None:
    #         used_starters = set()

    #     starters = {
    #         "conceptual_deep": [
    #             "What are the fundamental principles behind",
    #             "How do theoretical foundations of",
    #             "What role does",
    #             "Why is the concept of",
    #         ],
    #         "practical_application": [
    #             "How can practitioners implement",
    #             "What are the real-world applications of",
    #             "In what scenarios would you choose",
    #             "What practical considerations arise when",
    #         ],
    #         "theoretical_foundation": [
    #             "Under what mathematical conditions does",
    #             "What theoretical guarantees exist for",
    #             "How does the theoretical complexity of",
    #             "What are the convergence properties of",
    #         ],
    #         "comparative_analysis": [
    #             "How does performance compare between",
    #             "What are the trade-offs when choosing",
    #             "In what ways do different approaches to",
    #             "What distinguishes one method from another in",
    #         ],
    #         "implementation_focused": [
    #             "What are the key implementation challenges in",
    #             "How should developers approach the coding of",
    #             "What data structures are most suitable for",
    #             "What are common pitfalls when implementing",
    #         ],
    #         "evaluation_metrics": [
    #             "How should researchers evaluate the effectiveness of",
    #             "What metrics are most appropriate for measuring",
    #             "How can the quality of solutions be assessed in",
    #             "What benchmarking approaches work best for",
    #         ],
    #     }

    #     available = [s for s in starters[style] if s not in used_starters]
    #     if not available:
    #         available = starters[style]  # Reset if all used

    #     return random.choice(available)


def create_diverse_prompt(content, sections, diversity_controller, paper_index):
    """Create highly diverse prompts based on paper content and index."""

    style = diversity_controller.get_diverse_prompt_style(paper_index)
    question_type = diversity_controller.question_types[
        paper_index % len(diversity_controller.question_types)
    ]
    complexity = diversity_controller.complexity_levels[
        paper_index % len(diversity_controller.complexity_levels)
    ]

    # Extract key topics from the paper
    content_lower = content.lower()
    relevant_topics = []
    for category, topics in diversity_controller.topic_categories.items():
        for topic in topics:
            if topic in content_lower:
                relevant_topics.append(topic)

    # Ensure we have a fallback topic
    if not relevant_topics:
        relevant_topics = ["optimization", "algorithm"]

    main_topic = random.choice(relevant_topics[:3])  # Focus on most relevant

    prompt_templates = {
        "conceptual_deep": f"""
You are creating a DIRECT, SELF-CONTAINED question about {main_topic} for academic research evaluation.

Generate exactly ONE question-answer pair that explores fundamental concepts, theoretical underpinnings, or core principles.

CRITICAL REQUIREMENTS:
- Question MUST directly name specific algorithms, methods, techniques, or concepts mentioned in the paper
- Question MUST be answerable by someone with access to relevant literature through search
- NO contextual references like "this paper", "the study", "as presented", "according to", "in this context"
- Question should be something a researcher could ask independently

Focus on: WHY things work, WHAT makes them effective, HOW concepts relate to each other.

Question should start with: "What are the fundamental..." or "How do theoretical..." or "Why does..."

GOOD EXAMPLES:
- "What are the fundamental principles behind the Growing Neural Gas (GNG) network in Estimation of Distribution Algorithms?"
- "How do theoretical foundations of MIMIC differ from traditional genetic algorithms?"
- "Why does the competitive Hebbian learning rule contribute to model building in EDAs?"

BAD EXAMPLES (avoid these):
- "What is special about the factorization mentioned in this paper?"
- "What are the fundamental principles described in the study?"
- "How do the theoretical foundations presented here work?"

The question MUST be answerable directly from the paper content provided. The answer MUST be derived directly from the text.

IMPORTANT: You must also extract a supporting chunk from the paper (about 300 words) that contains the information needed to answer the question.

Make it {complexity} level complexity.
""",
        "practical_application": f"""
You are creating a DIRECT, SELF-CONTAINED question about {main_topic} for real-world usage scenarios.

Generate exactly ONE question-answer pair focused on implementation, usage, or practical considerations.

CRITICAL REQUIREMENTS:
- Question MUST directly name specific algorithms, methods, techniques, or approaches mentioned in the paper
- Question MUST be answerable by someone with access to relevant literature through search
- NO contextual references like "this paper", "the study", "as presented", "according to", "in this context"
- Question should be something a practitioner could ask independently

Focus on: HOW TO apply methods, WHEN to use approaches, WHERE they work best, WHAT considerations matter.

Question should start with: "How can practitioners..." or "In what scenarios..." or "What practical considerations..."

GOOD EXAMPLES:
- "How can practitioners implement the PBIL algorithm for cloud resource scheduling?"
- "In what scenarios would SCSO (Surrogate-assisted Cooperative Signal Optimization) be preferred over traditional methods?"
- "What practical considerations arise when implementing Growing Neural Gas networks for clustering?"

BAD EXAMPLES (avoid these):
- "How can practitioners implement the approach described?"
- "In what scenarios would the method presented work best?"
- "What practical considerations arise when using the techniques mentioned?"

The question MUST be answerable directly from the paper content provided. The answer MUST be derived directly from the text.

IMPORTANT: You must also extract a supporting chunk from the paper (about 300 words) that contains the information needed to answer the question.

Make it {complexity} level complexity.
""",
        "theoretical_foundation": f"""
You are creating a DIRECT, SELF-CONTAINED question about {main_topic} focusing on mathematical or algorithmic foundations.

Generate exactly ONE question-answer pair about convergence, complexity, proofs, or mathematical properties.

CRITICAL REQUIREMENTS:
- Question MUST directly name specific algorithms, methods, techniques, or mathematical concepts mentioned in the paper
- Question MUST be answerable by someone with access to relevant literature through search
- NO contextual references like "this paper", "the study", "as presented", "according to", "in this context"
- Question should be something a theoretician could ask independently

Focus on: Mathematical guarantees, complexity analysis, convergence conditions, theoretical bounds.

Question should start with: "Under what conditions..." or "What theoretical guarantees..." or "How does the complexity..."

GOOD EXAMPLES:
- "Under what conditions does the EGNA (Estimation of Gaussian Networks Algorithm) converge?"
- "What theoretical guarantees exist for UMDA (Univariate Marginal Distribution Algorithm)?"
- "How does the computational complexity of MIMIC compare to traditional genetic algorithms?"

BAD EXAMPLES (avoid these):
- "Under what conditions does the algorithm converge?"
- "What theoretical guarantees exist for the approach described?"
- "How does the complexity of the method presented compare?"

The question MUST be answerable directly from the paper content provided. The answer MUST be derived directly from the text.

IMPORTANT: You must also extract a supporting chunk from the paper (about 300 words) that contains the information needed to answer the question.

Make it {complexity} level complexity.
""",
        "comparative_analysis": f"""
You are creating a DIRECT, SELF-CONTAINED question about {main_topic} that examines differences and trade-offs.

Generate exactly ONE question-answer pair comparing approaches, methods, or techniques.

CRITICAL REQUIREMENTS:
- Question MUST directly name specific algorithms, methods, or techniques being compared
- Question MUST be answerable by someone with access to relevant literature through search
- NO contextual references like "this paper", "the study", "as presented", "according to", "in this context"
- Question should be something a researcher could ask independently

Focus on: Performance differences, trade-offs, when to choose one over another, relative strengths/weaknesses.

Question should start with: "How does performance compare..." or "What are the trade-offs..." or "What distinguishes..."

GOOD EXAMPLES:
- "How does performance compare between UMDA and BMDA for discrete optimization problems?"
- "What are the trade-offs between using MIMIC versus traditional genetic algorithms?"
- "What distinguishes the Growing Neural Gas approach from standard clustering methods in EDAs?"

BAD EXAMPLES (avoid these):
- "How does performance compare between the different approaches?"
- "What are the trade-offs when choosing the methods presented?"
- "What distinguishes one approach from another in the study?"

The question MUST be answerable directly from the paper content provided. The answer MUST be derived directly from the text.

IMPORTANT: You must also extract a supporting chunk from the paper (about 300 words) that contains the information needed to answer the question.

Make it {complexity} level complexity.
""",
        "implementation_focused": f"""
You are creating a DIRECT, SELF-CONTAINED question about {main_topic} for developers and programmers.

Generate exactly ONE question-answer pair about coding, data structures, algorithms, or technical implementation.

CRITICAL REQUIREMENTS:
- Question MUST directly name specific algorithms, data structures, or implementation techniques mentioned in the paper
- Question MUST be answerable by someone with access to relevant literature through search
- NO contextual references like "this paper", "the study", "as presented", "according to", "in this context"
- Question should be something a developer could ask independently

Focus on: Code structure, data representation, algorithmic steps, technical challenges, best practices.

Question should start with: "What are the key implementation..." or "How should developers..." or "What data structures..."

GOOD EXAMPLES:
- "What are the key implementation challenges when coding PBIL (Population-Based Incremental Learning)?"
- "How should developers structure the probability vector updates in UMDA?"
- "What data structures are most suitable for implementing Growing Neural Gas networks?"

BAD EXAMPLES (avoid these):
- "What are the key implementation challenges for the algorithm described?"
- "How should developers approach coding the method presented?"
- "What data structures work best for the approach mentioned?"

The question MUST be answerable directly from the paper content provided. The answer MUST be derived directly from the text.

IMPORTANT: You must also extract a supporting chunk from the paper (about 300 words) that contains the information needed to answer the question.

Make it {complexity} level complexity.
""",
        "evaluation_metrics": f"""
You are creating a DIRECT, SELF-CONTAINED question about {main_topic} focusing on assessment and measurement.

Generate exactly ONE question-answer pair about how to measure, evaluate, or benchmark performance.

CRITICAL REQUIREMENTS:
- Question MUST directly name specific algorithms, metrics, or evaluation methods mentioned in the paper
- Question MUST be answerable by someone with access to relevant literature through search
- NO contextual references like "this paper", "the study", "as presented", "according to", "in this context"
- Question should be something an evaluator could ask independently

Focus on: Evaluation criteria, performance metrics, benchmarking approaches, quality assessment.

Question should start with: "How should researchers evaluate..." or "What metrics are most appropriate..." or "How can quality be assessed..."

GOOD EXAMPLES:
- "What metrics are most appropriate for measuring UMDA convergence speed on NK landscapes?"
- "How should researchers evaluate the solution quality of MIMIC on discrete optimization problems?"
- "How can the interpretability of Bayesian networks be assessed in EDA contexts?"

BAD EXAMPLES (avoid these):
- "What metrics are most appropriate for measuring the approach described?"
- "How should researchers evaluate the effectiveness of the method presented?"
- "How can quality be assessed for the techniques mentioned?"

The question MUST be answerable directly from the paper content provided. The answer MUST be derived directly from the text.

IMPORTANT: You must also extract a supporting chunk from the paper (about 300 words) that contains the information needed to answer the question.

Make it {complexity} level complexity.
""",
    }

    base_prompt = prompt_templates[style]

    # Add the paper content and formatting requirements
    full_prompt = f"""{base_prompt}

CRITICAL FORMATTING REQUIREMENTS:
- Return a structured JSON response with exactly one question-answer pair
- Include a supporting_chunk field with ~300 words from the paper that substantiates your answer
- Use plain text for math (no LaTeX, no backslashes)
- Question must directly name specific algorithms/methods/concepts (extract these from the paper content below)
- Question must be self-contained and answerable through literature search
- Answer must be derived directly from the paper, not general knowledge

<paper_content>
{content[:3000]}  # Limit content to avoid token limits
</paper_content>

Paper title: {sections.get("title", "Unknown")}
Main topic focus: {main_topic}
Question style: {style.replace("_", " ")}
Complexity level: {complexity}

REMEMBER: The question must directly reference specific named algorithms, methods, or concepts from the paper content above!
"""

    return full_prompt


# Define a timeout exception
class GeminiTimeoutError(Exception):
    pass


@retry(
    stop=stop_after_attempt(3),  # Increased retries
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
                        response_schema=list[QuestionAnswer],
                    ),
                )

                # If successful, get parsed objects directly
                if hasattr(response, "parsed"):
                    parsed_json = response.parsed
                    logger.info(
                        f"Successfully parsed structured response using Pydantic model"
                    )
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
                logger.error(f"No JSON array found. Response: {response_text[:200]}...")
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


def get_all_markdown_files():
    """Get all markdown files from the directory structure."""
    base_path = Path(MARKDOWN_DIR)
    markdown_files = []

    for year_dir in base_path.iterdir():
        if year_dir.is_dir() and year_dir.name.isdigit():
            for md_file in year_dir.glob("*.md"):
                markdown_files.append(md_file)

    logger.info(f"Found {len(markdown_files)} markdown files")
    return markdown_files


def read_markdown_content(md_path):
    """Read and return markdown content from file with validation."""
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content.strip()) < 500:  # Increased minimum length
            logger.warning(
                f"Paper {md_path.stem} seems too short ({len(content)} chars)"
            )
            return None

        return content
    except Exception as e:
        logger.error(f"Error reading markdown file {md_path}: {str(e)}")
        return None


def extract_paper_sections(content):
    """Enhanced section extraction with better parsing."""
    sections = {
        "title": "",
        "abstract": "",
        "introduction": "",
        "methods": "",
        "results": "",
        "conclusion": "",
        "key_findings": "",
        "full_content": content,
    }

    lines = content.split("\n")
    current_section = None
    title_found = False

    for i, line in enumerate(lines):
        line_lower = line.lower().strip()

        # Better title extraction
        if not title_found and line.strip() and not line.startswith("#"):
            if i < 5 and len(line.strip()) > 10:  # First few lines, reasonable length
                sections["title"] = line.strip()
                title_found = True
        elif line.startswith("# ") and not title_found:
            sections["title"] = line[2:].strip()
            title_found = True

        # Section detection
        if re.search(r"\b(abstract|summary)\b", line_lower):
            current_section = "abstract"
        elif re.search(r"\b(introduction|background)\b", line_lower):
            current_section = "introduction"
        elif re.search(r"\b(method|approach|algorithm)\b", line_lower):
            current_section = "methods"
        elif re.search(r"\b(result|experiment|evaluation)\b", line_lower):
            current_section = "results"
        elif re.search(r"\b(conclusion|discussion)\b", line_lower):
            current_section = "conclusion"
        elif current_section and line.strip() and not line.startswith("#"):
            sections[current_section] += line + "\n"

    return sections


def generate_questions_for_paper(
    content, sections, paper_id, year, file_path, diversity_controller, paper_index
):
    """Generate questions for a single paper with enhanced variety."""
    logger.info(f"Starting question generation for paper {paper_index + 1}: {paper_id}")

    max_attempts = 5  # Try multiple times for variety
    generated_questions = []

    for attempt in range(max_attempts):
        try:
            prompt = create_diverse_prompt(
                content, sections, diversity_controller, paper_index + attempt
            )
            response = get_gemini_response(prompt)
            json_str = clean_json_response(response)
            qa_pairs = json.loads(json_str)

            if not isinstance(qa_pairs, list) or len(qa_pairs) != 1:
                logger.warning(f"Unexpected response format on attempt {attempt + 1}")
                continue

            qa = qa_pairs[0]
            if (
                not isinstance(qa, dict)
                or "question" not in qa
                or "answer" not in qa
                or "supporting_chunk" not in qa
            ):
                logger.warning(f"Invalid QA structure on attempt {attempt + 1}")
                continue

            # Check for forbidden phrases - ENHANCED
            question_lower = qa["question"].lower()
            forbidden_phrases = [
                "this paper",
                "the paper",
                "in the paper",
                "the authors",
                "our approach",
                "we propose",
                "as presented",
                "according to",
                "in this context",
                "in the study",
                "the study",
                "mentioned above",
                "described here",
                "presented here",
                "in this work",
                "this research",
                "the research",
                "this method",
                "the approach described",
                "the method presented",
                "the technique mentioned",
                "as discussed",
                "as shown",
                "as described",
                "as mentioned",
                "according to the",
                "based on the information provided",
                "from the information presented",
            ]

            # Also check if question contains specific algorithm/method names
            # Extract potential algorithm names from content (simple heuristic)
            content_upper = content.upper()
            algorithm_indicators = [
                "ALGORITHM",
                "METHOD",
                "APPROACH",
                "TECHNIQUE",
                "MODEL",
                "FRAMEWORK",
                "SYSTEM",
                "STRATEGY",
                "PROCEDURE",
            ]

            has_specific_reference = False
            for line in content.split("\n")[
                :50
            ]:  # Check first 50 lines for algorithm names
                line_upper = line.upper()
                if any(indicator in line_upper for indicator in algorithm_indicators):
                    # Look for capitalized terms that might be algorithm names
                    words = line.split()
                    for i, word in enumerate(words):
                        if (word.isupper() and len(word) > 2) or (
                            word[0].isupper()
                            and any(char.isupper() for char in word[1:])
                        ):
                            if word.upper() in qa["question"].upper():
                                has_specific_reference = True
                                break

            if any(phrase in question_lower for phrase in forbidden_phrases):
                logger.warning(
                    f"Question contains forbidden contextual phrases on attempt {attempt + 1}: {qa['question'][:100]}..."
                )
                continue

            if not has_specific_reference:
                # Look for any proper nouns or technical terms in the question
                question_words = qa["question"].split()
                has_technical_terms = any(
                    word[0].isupper()
                    and len(word) > 3
                    and not word
                    in [
                        "What",
                        "How",
                        "Why",
                        "When",
                        "Where",
                        "Which",
                        "The",
                        "This",
                        "That",
                        "These",
                        "Those",
                    ]
                    for word in question_words
                )
                if not has_technical_terms:
                    logger.warning(
                        f"Question lacks specific algorithm/method references on attempt {attempt + 1}: {qa['question'][:100]}..."
                    )
                    continue

            # Check similarity to existing questions in this session
            existing_questions = [q["question"] for q in generated_questions]
            if is_question_too_similar(qa["question"], existing_questions):
                logger.warning(
                    f"Question too similar to existing ones on attempt {attempt + 1}"
                )
                continue

            # Create RAGAS item with supporting chunk from model
            ragas_item = {
                "question": qa["question"],
                "contexts": [],
                "ground_truth": qa["answer"],
                "paper_id": paper_id,
                "paper_title": sections.get(
                    "title", paper_id.replace("-", " ").title()
                ),
                "paper_year": year,
                "file_path": str(file_path),
                "question_type": qa.get("question_type", "unknown"),
                "complexity": qa.get("complexity", "medium"),
                "topics": qa.get("topics", []),
                "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "generation_style": diversity_controller.get_diverse_prompt_style(
                    paper_index + attempt
                ),
                "golden_chunk": qa.get("supporting_chunk", ""),
                "chunk_source": "model_extracted",
            }

            generated_questions.append(ragas_item)
            logger.info(
                f"Successfully generated question for paper {paper_id} on attempt {attempt + 1}"
            )
            return [ragas_item]  # Return first successful question

        except Exception as e:
            logger.warning(
                f"Attempt {attempt + 1} failed for paper {paper_id}: {str(e)}"
            )
            if attempt < max_attempts - 1:
                time.sleep(1)  # Brief pause between attempts
                continue

    logger.error(
        f"Failed to generate question for paper {paper_id} after {max_attempts} attempts"
    )
    return None


def generate_ragas_dataset():
    """Generate RAGAS dataset with enhanced variety and guaranteed 100 questions."""
    dataset = {
        "metadata": {
            "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_papers_processed": 0,
            "total_questions": 0,
            "statistics": {
                "total_papers": 0,
                "successful": 0,
                "failed_content": 0,
                "failed_generation": 0,
                "total_questions": 0,
            },
        },
        "questions": [],
    }

    diversity_controller = QuestionDiversityController()
    markdown_files = get_all_markdown_files()

    # Shuffle for randomness
    random.shuffle(markdown_files)

    successful_papers = 0
    failed_content = 0
    failed_generation = 0
    processed_papers = 0

    target_questions = 100

    try:
        for file_path in markdown_files:
            if len(dataset["questions"]) >= target_questions:
                break

            processed_papers += 1
            logger.info(
                f"--- Processing paper {processed_papers}: {file_path.name} ---"
            )

            paper_id = os.path.splitext(os.path.basename(file_path))[0]
            year = os.path.basename(os.path.dirname(file_path))

            content = read_markdown_content(file_path)
            if not content:
                failed_content += 1
                continue

            sections = extract_paper_sections(content)
            if not sections.get("title") and not content:
                failed_content += 1
                continue

            questions = generate_questions_for_paper(
                content,
                sections,
                paper_id,
                year,
                file_path,
                diversity_controller,
                len(dataset["questions"]),
            )

            if not questions:
                failed_generation += 1
                continue

            # Check for duplicates before adding
            existing_questions = [q["question"] for q in dataset["questions"]]
            for question in questions:
                if not is_question_too_similar(
                    question["question"], existing_questions, 0.6
                ):
                    dataset["questions"].append(question)
                    successful_papers += 1
                    logger.info(
                        f"Added question {len(dataset['questions'])}/{target_questions}"
                    )
                else:
                    logger.warning("Skipped duplicate question")

            # Save progress every 10 questions
            if len(dataset["questions"]) % 10 == 0:
                save_dataset(dataset)

    except KeyboardInterrupt:
        logger.info("Generation interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

    # Final statistics
    dataset["metadata"]["total_papers_processed"] = processed_papers
    dataset["metadata"]["total_questions"] = len(dataset["questions"])
    dataset["metadata"]["statistics"].update(
        {
            "total_papers": processed_papers,
            "successful": successful_papers,
            "failed_content": failed_content,
            "failed_generation": failed_generation,
            "total_questions": len(dataset["questions"]),
        }
    )

    save_dataset(dataset)
    logger.info(
        f"Generated {len(dataset['questions'])} unique questions from {processed_papers} papers"
    )
    return dataset


def save_dataset(dataset):
    """Save the dataset to a JSON file."""
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)
        logger.info(f"Dataset saved to {OUTPUT_FILE}")
    except Exception as e:
        logger.error(f"Error saving dataset: {str(e)}")
        raise


def extract_multiple_reference_spans(
    content: str, question: str, answer: str, max_spans: int = 5
) -> List[str]:
    """
    Extract multiple relevant text spans from document content that support the answer.
    This follows Chroma's approach of having multiple variable-length excerpts.
    """
    if not content or not question or not answer:
        return []

    # Split content into sentences and paragraphs
    sentences = [
        s.strip() for s in content.split(".") if s.strip() and len(s.strip()) > 20
    ]
    paragraphs = [
        p.strip() for p in content.split("\n\n") if p.strip() and len(p.strip()) > 50
    ]

    # Extract key terms from question and answer for relevance scoring
    question_terms = set(question.lower().split())
    answer_terms = set(answer.lower().split())

    # Remove common stop words
    stop_words = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "of",
        "with",
        "by",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "will",
        "would",
        "could",
        "should",
        "may",
        "might",
        "can",
        "this",
        "that",
        "these",
        "those",
    }
    key_terms = (question_terms | answer_terms) - stop_words

    # Score passages based on relevance
    scored_passages = []

    # Score paragraphs (prioritize these as they're more likely to be complete thoughts)
    for i, paragraph in enumerate(paragraphs):
        if len(paragraph) < 100:  # Skip very short paragraphs
            continue

        paragraph_lower = paragraph.lower()
        score = sum(1 for term in key_terms if term in paragraph_lower)

        # Bonus for longer, more substantive paragraphs
        length_bonus = min(len(paragraph) / 500, 1.0)

        # Penalty for very long paragraphs (avoid getting entire sections)
        if len(paragraph) > 1000:
            length_bonus *= 0.5

        final_score = score + length_bonus

        if final_score > 1.0:  # Only consider paragraphs with some relevance
            scored_passages.append(
                {
                    "text": paragraph,
                    "score": final_score,
                    "type": "paragraph",
                    "source_index": i,
                }
            )

    # If we don't have enough paragraph-level matches, try sentence groups
    if len(scored_passages) < max_spans:
        for i in range(0, len(sentences) - 2, 2):  # Group sentences in pairs/triplets
            sentence_group = ". ".join(sentences[i : i + 3]) + "."
            if len(sentence_group) < 100:
                continue

            group_lower = sentence_group.lower()
            score = sum(1 for term in key_terms if term in group_lower)

            if score > 1:
                scored_passages.append(
                    {
                        "text": sentence_group,
                        "score": score,
                        "type": "sentence_group",
                        "source_index": i,
                    }
                )

    # Sort by relevance score and select top spans
    scored_passages.sort(key=lambda x: x["score"], reverse=True)

    # Select diverse spans (avoid too much overlap)
    selected_spans = []
    used_terms = set()

    for passage in scored_passages[: max_spans * 2]:  # Consider more candidates
        if len(selected_spans) >= max_spans:
            break

        # Check for overlap with already selected spans
        passage_terms = set(passage["text"].lower().split())
        overlap = (
            len(passage_terms & used_terms) / len(passage_terms) if passage_terms else 1
        )

        # Accept if overlap is not too high (allows for some redundancy but ensures diversity)
        if overlap < 0.7:
            selected_spans.append(
                passage["text"][:500]
            )  # Limit span length like Chroma (~200 tokens ≈ 500 chars)
            used_terms.update(passage_terms)

    # Ensure we have at least one span
    if not selected_spans and scored_passages:
        selected_spans.append(scored_passages[0]["text"][:500])

    return selected_spans


def create_chroma_style_prompt(question: str, answer: str, content: str) -> str:
    """Create a prompt to generate multiple reference spans following Chroma's methodology."""

    return f"""
You are enhancing a question-answer pair to follow Chroma's evaluation methodology.

Given a question and answer, identify multiple relevant text excerpts from the document that collectively provide evidence to answer the question.

CRITICAL REQUIREMENTS following Chroma research:
- Extract 3-5 distinct text spans from the document
- Each span should be 100-300 words (similar to Chroma's ~200 token excerpts)
- Spans should collectively cover different aspects of the answer
- Spans can come from different sections of the paper
- Each span should be independently meaningful
- Avoid redundant information between spans

QUESTION: {question}

ANSWER: {answer}

DOCUMENT CONTENT:
{content[:4000]}  # Limit to avoid token limits

Return multiple reference spans that support this answer. Each span should focus on a different aspect or provide complementary evidence.

IMPORTANT: Extract verbatim text from the document - do not rephrase or summarize!
"""


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(
        (GeminiTimeoutError, ConnectionError, json.JSONDecodeError)
    ),
    reraise=True,
)
@timeout_decorator.timeout(120)
def enhance_question_with_multi_references(question_data: dict, content: str) -> dict:
    """Enhance existing question with multiple reference spans using Chroma's approach."""

    try:
        # First, try automatic extraction
        auto_spans = extract_multiple_reference_spans(
            content, question_data["question"], question_data["ground_truth"]
        )

        # If we have good automatic spans, use them
        if len(auto_spans) >= 2:
            enhanced_data = question_data.copy()
            enhanced_data["reference_spans"] = auto_spans
            enhanced_data["span_sources"] = [
                f"auto_extracted_{i}" for i in range(len(auto_spans))
            ]
            enhanced_data["extraction_method"] = "automatic"
            return enhanced_data

        # Otherwise, use LLM to extract better spans
        prompt = create_chroma_style_prompt(
            question_data["question"], question_data["ground_truth"], content
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,  # Lower temperature for more consistent extraction
                top_p=0.9,
                max_output_tokens=2048,
                response_mime_type="application/json",
                response_schema=list[MultiReferenceAnswer],
            ),
        )

        if hasattr(response, "parsed") and response.parsed:
            parsed_result = response.parsed[0]
            enhanced_data = question_data.copy()
            enhanced_data["reference_spans"] = parsed_result.reference_spans
            enhanced_data["span_sources"] = (
                parsed_result.span_sources
                if hasattr(parsed_result, "span_sources")
                else [
                    f"llm_extracted_{i}"
                    for i in range(len(parsed_result.reference_spans))
                ]
            )
            enhanced_data["extraction_method"] = "llm_assisted"
            return enhanced_data

        # Fallback: use the original golden_chunk split into multiple parts
        original_chunk = question_data.get("golden_chunk", "")
        if original_chunk:
            # Split by sentences and group them
            sentences = [
                s.strip() + "." for s in original_chunk.split(".") if s.strip()
            ]
            spans = []
            current_span = ""

            for sentence in sentences:
                if len(current_span + sentence) < 300:
                    current_span += " " + sentence if current_span else sentence
                else:
                    if current_span:
                        spans.append(current_span.strip())
                    current_span = sentence

            if current_span:
                spans.append(current_span.strip())

            enhanced_data = question_data.copy()
            enhanced_data["reference_spans"] = (
                spans[:3] if len(spans) > 1 else [original_chunk]
            )
            enhanced_data["span_sources"] = [
                f"split_original_{i}"
                for i in range(len(enhanced_data["reference_spans"]))
            ]
            enhanced_data["extraction_method"] = "fallback_split"
            return enhanced_data

        # Last resort: return original with single span
        enhanced_data = question_data.copy()
        enhanced_data["reference_spans"] = [
            question_data.get("golden_chunk", question_data.get("ground_truth", ""))
        ]
        enhanced_data["span_sources"] = ["original_chunk"]
        enhanced_data["extraction_method"] = "original_single"
        return enhanced_data

    except Exception as e:
        logger.warning(f"Failed to enhance question with multi-references: {str(e)}")
        # Return original data as fallback
        enhanced_data = question_data.copy()
        enhanced_data["reference_spans"] = [
            question_data.get("golden_chunk", question_data.get("ground_truth", ""))
        ]
        enhanced_data["span_sources"] = ["fallback"]
        enhanced_data["extraction_method"] = "error_fallback"
        return enhanced_data


def enhance_existing_dataset_with_multi_references():
    """
    Enhance the existing final_golden_chunk_dataset_100.json with multiple reference spans
    following Chroma's methodology.
    """

    # Load existing dataset
    try:
        with open(
            "/Users/id05309/Documents/tfm/mistral/evaluate-dataset/final_golden_chunk_dataset_100.json",
            "r",
            encoding="utf-8",
        ) as f:
            existing_dataset = json.load(f)
    except Exception as e:
        logger.error(f"Failed to load existing dataset: {str(e)}")
        return None

    # Create enhanced dataset
    enhanced_dataset = {
        "metadata": {
            "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "original_dataset": "final_golden_chunk_dataset_100.json",
            "enhancement": "multi_reference_spans_chroma_style",
            "total_questions": len(existing_dataset.get("questions", [])),
            "enhancement_statistics": {
                "successful": 0,
                "failed": 0,
                "automatic_extraction": 0,
                "llm_assisted": 0,
                "fallback_used": 0,
            },
        },
        "questions": [],
    }

    questions = existing_dataset.get("questions", [])
    logger.info(
        f"Enhancing {len(questions)} questions with multiple reference spans..."
    )

    for i, question_data in enumerate(questions):
        logger.info(
            f"Processing question {i + 1}/{len(questions)}: {question_data.get('question', 'Unknown')[:100]}..."
        )

        try:
            # Load the original document content
            file_path = question_data.get("file_path", "")
            if not file_path or not os.path.exists(file_path):
                logger.warning(f"File path not found for question {i + 1}: {file_path}")
                # Use fallback enhancement
                enhanced_question = enhance_question_with_multi_references(
                    question_data, ""
                )
                enhanced_dataset["questions"].append(enhanced_question)
                enhanced_dataset["metadata"]["enhancement_statistics"][
                    "fallback_used"
                ] += 1
                continue

            # Read the full document content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Enhance the question with multiple reference spans
            enhanced_question = enhance_question_with_multi_references(
                question_data, content
            )
            enhanced_dataset["questions"].append(enhanced_question)

            # Update statistics
            method = enhanced_question.get("extraction_method", "unknown")
            if "automatic" in method:
                enhanced_dataset["metadata"]["enhancement_statistics"][
                    "automatic_extraction"
                ] += 1
            elif "llm" in method:
                enhanced_dataset["metadata"]["enhancement_statistics"][
                    "llm_assisted"
                ] += 1
            else:
                enhanced_dataset["metadata"]["enhancement_statistics"][
                    "fallback_used"
                ] += 1

            enhanced_dataset["metadata"]["enhancement_statistics"]["successful"] += 1

            # Log progress
            if (i + 1) % 20 == 0:
                logger.info(
                    f"Processed {i + 1}/{len(questions)} questions successfully"
                )

        except Exception as e:
            logger.error(f"Failed to enhance question {i + 1}: {str(e)}")
            enhanced_dataset["metadata"]["enhancement_statistics"]["failed"] += 1
            # Add original question as fallback
            enhanced_dataset["questions"].append(question_data)

    # Save enhanced dataset
    output_file = "/Users/id05309/Documents/tfm/mistral/evaluate-dataset/enhanced_multi_reference_dataset_100.json"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(enhanced_dataset, f, indent=2, ensure_ascii=False)
        logger.info(f"Enhanced dataset saved to {output_file}")

        # Print summary statistics
        stats = enhanced_dataset["metadata"]["enhancement_statistics"]
        logger.info("=== ENHANCEMENT SUMMARY ===")
        logger.info(f"Total questions processed: {len(enhanced_dataset['questions'])}")
        logger.info(f"Successful enhancements: {stats['successful']}")
        logger.info(f"Automatic extractions: {stats['automatic_extraction']}")
        logger.info(f"LLM-assisted extractions: {stats['llm_assisted']}")
        logger.info(f"Fallback methods used: {stats['fallback_used']}")
        logger.info(f"Failed enhancements: {stats['failed']}")

        # Show example of enhanced question
        if enhanced_dataset["questions"]:
            example = enhanced_dataset["questions"][0]
            logger.info(f"\n=== EXAMPLE ENHANCED QUESTION ===")
            logger.info(f"Question: {example['question'][:150]}...")
            logger.info(
                f"Number of reference spans: {len(example.get('reference_spans', []))}"
            )
            logger.info(
                f"Extraction method: {example.get('extraction_method', 'unknown')}"
            )
            for j, span in enumerate(example.get("reference_spans", [])[:2]):
                logger.info(f"Span {j + 1} (first 100 chars): {span[:100]}...")

        return enhanced_dataset

    except Exception as e:
        logger.error(f"Failed to save enhanced dataset: {str(e)}")
        return None


if __name__ == "__main__":
    import sys

    # Check if we should enhance existing dataset or generate new questions
    if len(sys.argv) > 1 and sys.argv[1] == "enhance":
        logger.info(
            "Enhancing existing dataset with multiple reference spans (Chroma-style)..."
        )
        enhanced_dataset = enhance_existing_dataset_with_multi_references()
        if enhanced_dataset:
            logger.info(
                "✅ Successfully enhanced dataset with multiple reference spans!"
            )
        else:
            logger.error("❌ Failed to enhance dataset")
    else:
        logger.info("Starting enhanced question generation with variety...")
        dataset = generate_ragas_dataset()
        logger.info(f"Final dataset contains {len(dataset['questions'])} questions")

        # Print summary of question types for verification
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

        logger.info("\n" + "=" * 50)
        logger.info(
            "💡 To enhance this dataset with Chroma-style multiple reference spans, run:"
        )
        logger.info("python question-answer.py enhance")
        logger.info("=" * 50)
