#!/usr/bin/env python3
"""
Enhance existing dataset with multiple reference spans following Chroma's methodology.
Takes final_golden_chunk_dataset_100.json and adds multiple reference excerpts per question.
"""

import json
import os
import logging
import re
from datetime import datetime
from typing import List, Dict, Any

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# File paths
INPUT_DATASET = "/Users/id05309/Documents/tfm/mistral/evaluate-dataset/final_golden_chunk_dataset_100.json"
OUTPUT_DATASET = "/Users/id05309/Documents/tfm/mistral/evaluate-dataset/chroma_style_multi_reference_dataset.json"


def extract_chroma_style_references(
    content: str, question: str, answer: str, max_refs: int = 5
) -> List[str]:
    """
    Extract multiple reference spans following Chroma's methodology:
    - Find all significant facts that answer the question
    - Extract exact text sections (whole sentences where possible)
    - Maximum 5 references per question
    """
    if not content or not question or not answer:
        return []

    logger.debug(f"Extracting references for question: {question[:50]}...")

    # Clean content and split into meaningful units
    content = content.strip()

    # Split into sentences (more robust approach)
    sentences = []
    for sentence in re.split(r"[.!?]+", content):
        sentence = sentence.strip()
        if len(sentence) > 30:  # Skip very short fragments
            sentences.append(sentence + ".")

    # Split into paragraphs for longer coherent sections
    paragraphs = [
        p.strip() for p in content.split("\n\n") if p.strip() and len(p.strip()) > 100
    ]

    # Extract key terms from question and answer for relevance scoring
    question_words = set(question.lower().split())
    answer_words = set(answer.lower().split())

    # Remove stop words
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
        "what",
        "how",
        "when",
        "where",
        "why",
        "which",
        "who",
    }

    key_terms = (question_words | answer_words) - stop_words

    # Score all text segments based on relevance
    scored_segments = []

    # Score sentences
    for i, sentence in enumerate(sentences):
        sentence_lower = sentence.lower()

        # Count key term matches
        term_matches = sum(1 for term in key_terms if term in sentence_lower)

        # Bonus for technical/scientific language
        technical_terms = [
            "algorithm",
            "method",
            "approach",
            "technique",
            "model",
            "framework",
            "system",
            "optimization",
            "distribution",
            "estimation",
            "genetic",
            "evolutionary",
            "population",
            "fitness",
            "selection",
        ]
        technical_bonus = (
            sum(1 for term in technical_terms if term in sentence_lower) * 0.3
        )

        # Bonus for containing numbers/results
        numbers_bonus = 0.2 if re.search(r"\d+", sentence) else 0

        final_score = term_matches + technical_bonus + numbers_bonus

        if final_score > 0.5:  # Lower threshold for sentences
            scored_segments.append(
                {"text": sentence, "score": final_score, "type": "sentence", "index": i}
            )

    # Score paragraphs for more comprehensive context
    for i, paragraph in enumerate(paragraphs):
        if (
            len(paragraph) < 150 or len(paragraph) > 1000
        ):  # Skip very short or very long
            continue

        paragraph_lower = paragraph.lower()

        # Count key term matches
        term_matches = sum(1 for term in key_terms if term in paragraph_lower)

        # Bonus for comprehensive coverage
        coverage_bonus = min(term_matches / max(len(key_terms), 1), 1.0)

        # Length normalization (prefer medium-length paragraphs)
        length_bonus = (
            1.0 - abs(len(paragraph) - 400) / 400 if len(paragraph) < 800 else 0.5
        )

        final_score = (term_matches * 1.5) + coverage_bonus + length_bonus

        if final_score > 1.5:  # Higher threshold for paragraphs
            scored_segments.append(
                {
                    "text": paragraph,
                    "score": final_score,
                    "type": "paragraph",
                    "index": i,
                }
            )

    # Sort by relevance score
    scored_segments.sort(key=lambda x: x["score"], reverse=True)

    # Select diverse references (avoid too much overlap)
    selected_references = []
    used_words = set()

    for segment in scored_segments[: max_refs * 3]:  # Consider more candidates
        if len(selected_references) >= max_refs:
            break

        segment_words = set(segment["text"].lower().split())
        overlap_ratio = (
            len(segment_words & used_words) / len(segment_words) if segment_words else 1
        )

        # Accept if overlap is reasonable (some redundancy is okay for completeness)
        if overlap_ratio < 0.6:
            # Ensure reference is appropriate length (like Chroma's ~200 tokens)
            ref_text = segment["text"]
            if len(ref_text) > 800:  # Too long, try to truncate sensibly
                # Find good breaking point
                sentences_in_ref = [s.strip() for s in ref_text.split(".") if s.strip()]
                if len(sentences_in_ref) > 1:
                    # Take first few sentences that fit
                    truncated = ""
                    for sent in sentences_in_ref:
                        if len(truncated + sent + ". ") < 600:
                            truncated += sent + ". "
                        else:
                            break
                    ref_text = truncated.strip()
                else:
                    ref_text = ref_text[:600] + "..."

            selected_references.append(ref_text)
            used_words.update(segment_words)

    # Ensure we have at least one reference
    if not selected_references and scored_segments:
        selected_references.append(scored_segments[0]["text"][:600])

    logger.debug(f"Extracted {len(selected_references)} reference spans")
    return selected_references


def enhance_question_with_multiple_references(
    question_data: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Enhance a single question with multiple reference spans.
    """
    try:
        # Get the original document content
        file_path = question_data.get("file_path", "")
        if not file_path or not os.path.exists(file_path):
            logger.warning(f"File not found: {file_path}")
            # Use the existing golden_chunk as fallback
            golden_chunk = question_data.get("golden_chunk", "")
            enhanced_data = question_data.copy()
            enhanced_data["references"] = [golden_chunk] if golden_chunk else []
            enhanced_data["extraction_method"] = "fallback_golden_chunk"
            enhanced_data["num_references"] = len(enhanced_data["references"])
            return enhanced_data

        # Read the full document content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract multiple references using Chroma's approach
        references = extract_chroma_style_references(
            content=content,
            question=question_data["question"],
            answer=question_data["ground_truth"],
        )

        # Create enhanced question data
        enhanced_data = question_data.copy()
        enhanced_data["references"] = (
            references if references else [question_data.get("golden_chunk", "")]
        )
        enhanced_data["extraction_method"] = "chroma_style_automatic"
        enhanced_data["num_references"] = len(enhanced_data["references"])

        # Keep original data for comparison
        enhanced_data["original_golden_chunk"] = question_data.get("golden_chunk", "")

        return enhanced_data

    except Exception as e:
        logger.error(f"Error enhancing question: {str(e)}")
        # Return original data with minimal enhancement
        enhanced_data = question_data.copy()
        enhanced_data["references"] = [question_data.get("golden_chunk", "")]
        enhanced_data["extraction_method"] = "error_fallback"
        enhanced_data["num_references"] = 1
        return enhanced_data


def main():
    """
    Main function to enhance the existing dataset with Chroma-style multiple references.
    """
    logger.info("🚀 Starting Chroma-style dataset enhancement...")
    logger.info(
        "📖 Following Chroma research methodology for multiple reference extraction"
    )

    # Load existing dataset
    try:
        with open(INPUT_DATASET, "r", encoding="utf-8") as f:
            existing_dataset = json.load(f)
        logger.info(
            f"✅ Loaded existing dataset with {len(existing_dataset.get('questions', []))} questions"
        )
    except Exception as e:
        logger.error(f"❌ Failed to load existing dataset: {str(e)}")
        return

    # Create enhanced dataset structure
    enhanced_dataset = {
        "metadata": {
            "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source_dataset": "final_golden_chunk_dataset_100.json",
            "enhancement_method": "chroma_style_multi_references",
            "methodology": "Following Chroma research: multiple reference excerpts per question",
            "reference_extraction": "Automatic content-based scoring and selection",
            "total_questions": len(existing_dataset.get("questions", [])),
            "statistics": {
                "successful_enhancements": 0,
                "fallback_used": 0,
                "error_count": 0,
                "avg_references_per_question": 0,
                "total_references": 0,
            },
        },
        "questions": [],
    }

    questions = existing_dataset.get("questions", [])
    total_references = 0

    # Process each question
    for i, question_data in enumerate(questions):
        logger.info(
            f"📝 Processing question {i + 1}/{len(questions)}: {question_data.get('question', 'Unknown')[:60]}..."
        )

        enhanced_question = enhance_question_with_multiple_references(question_data)
        enhanced_dataset["questions"].append(enhanced_question)

        # Update statistics
        method = enhanced_question.get("extraction_method", "unknown")
        num_refs = enhanced_question.get("num_references", 0)
        total_references += num_refs

        if "chroma_style" in method:
            enhanced_dataset["metadata"]["statistics"]["successful_enhancements"] += 1
        elif "fallback" in method or "error" in method:
            enhanced_dataset["metadata"]["statistics"]["fallback_used"] += 1
            if "error" in method:
                enhanced_dataset["metadata"]["statistics"]["error_count"] += 1

        # Log progress every 20 questions
        if (i + 1) % 20 == 0:
            logger.info(f"✅ Processed {i + 1}/{len(questions)} questions")

    # Update final statistics
    enhanced_dataset["metadata"]["statistics"]["total_references"] = total_references
    enhanced_dataset["metadata"]["statistics"]["avg_references_per_question"] = (
        total_references / len(questions) if questions else 0
    )

    # Save enhanced dataset
    try:
        with open(OUTPUT_DATASET, "w", encoding="utf-8") as f:
            json.dump(enhanced_dataset, f, indent=2, ensure_ascii=False)
        logger.info(f"💾 Enhanced dataset saved to: {OUTPUT_DATASET}")

        # Print summary
        stats = enhanced_dataset["metadata"]["statistics"]
        logger.info("\n" + "=" * 70)
        logger.info("📊 ENHANCEMENT SUMMARY")
        logger.info("=" * 70)
        logger.info(
            f"📋 Total questions processed: {len(enhanced_dataset['questions'])}"
        )
        logger.info(
            f"✅ Successful Chroma-style extractions: {stats['successful_enhancements']}"
        )
        logger.info(f"🔄 Fallback/error cases: {stats['fallback_used']}")
        logger.info(f"📚 Total references extracted: {stats['total_references']}")
        logger.info(
            f"📈 Average references per question: {stats['avg_references_per_question']:.2f}"
        )

        # Show example of enhanced question
        if enhanced_dataset["questions"]:
            example = enhanced_dataset["questions"][0]
            logger.info(f"\n📖 EXAMPLE ENHANCED QUESTION:")
            logger.info(f"❓ Question: {example['question'][:100]}...")
            logger.info(
                f"📝 Number of references: {len(example.get('references', []))}"
            )
            logger.info(
                f"🔧 Extraction method: {example.get('extraction_method', 'unknown')}"
            )

            # Show first two references
            for j, ref in enumerate(example.get("references", [])[:2]):
                logger.info(f"\n📄 Reference {j + 1} ({len(ref)} chars):")
                logger.info(f"   {ref[:150]}{'...' if len(ref) > 150 else ''}")

        logger.info("=" * 70)
        logger.info(
            "🎉 Successfully enhanced dataset with Chroma-style multiple references!"
        )
        logger.info(f"📁 Output: {OUTPUT_DATASET}")

    except Exception as e:
        logger.error(f"❌ Failed to save enhanced dataset: {str(e)}")


if __name__ == "__main__":
    main()
