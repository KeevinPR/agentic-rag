#!/usr/bin/env python3
"""
Enhanced dataset creation following Chroma's evaluation methodology.
This script takes existing questions from final_golden_chunk_dataset_100.json
and adds multiple reference spans following Chroma's approach.
"""

import json
import os
import logging
from pathlib import Path
from datetime import datetime
import re
from typing import List, Dict, Any

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# File paths
EXISTING_DATASET_PATH = "/Users/id05309/Documents/tfm/mistral/evaluate-dataset/final_golden_chunk_dataset_100.json"
OUTPUT_PATH = "/Users/id05309/Documents/tfm/mistral/evaluate-dataset/chroma_style_multi_reference_dataset_100.json"


def extract_chroma_style_references(
    content: str, question: str, answer: str, max_refs: int = 5
) -> List[str]:
    """
    Extract references following Chroma's methodology:
    - Find all significant facts that answer the question
    - Extract exact text sections (whole sentences where possible)
    - Maximum 5 references as per Chroma guidelines
    """
    if not content or not question or not answer:
        return []

    # Clean and prepare content
    content = content.strip()

    # Split into sentences (more robust splitting)
    sentences = []
    current_sentence = ""

    for char in content:
        current_sentence += char
        if char in ".!?" and len(current_sentence.strip()) > 20:
            # Check if this is likely end of sentence (not abbreviation)
            if not re.search(r"\b[A-Z][a-z]*\.$", current_sentence.strip()):
                sentences.append(current_sentence.strip())
                current_sentence = ""

    if current_sentence.strip():
        sentences.append(current_sentence.strip())

    # Also split into paragraphs for longer coherent sections
    paragraphs = [
        p.strip() for p in content.split("\n\n") if p.strip() and len(p.strip()) > 50
    ]

    # Extract key terms from question and answer
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

    # Score all text segments
    scored_segments = []

    # Score sentences
    for sentence in sentences:
        if len(sentence) < 30:  # Skip very short sentences
            continue

        sentence_lower = sentence.lower()

        # Count key term matches
        term_matches = sum(1 for term in key_terms if term in sentence_lower)

        # Bonus for sentences that contain multiple key terms
        density_bonus = term_matches / max(len(sentence.split()), 1)

        # Bonus for sentences with technical/scientific language
        technical_indicators = [
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
        ]
        technical_bonus = (
            sum(1 for indicator in technical_indicators if indicator in sentence_lower)
            * 0.5
        )

        final_score = term_matches + density_bonus + technical_bonus

        if final_score > 1.0:  # Only consider relevant sentences
            scored_segments.append(
                {"text": sentence, "score": final_score, "type": "sentence"}
            )

    # Score paragraphs (for longer coherent sections)
    for paragraph in paragraphs:
        if (
            len(paragraph) < 100 or len(paragraph) > 800
        ):  # Skip very short or very long paragraphs
            continue

        paragraph_lower = paragraph.lower()

        # Count key term matches
        term_matches = sum(1 for term in key_terms if term in paragraph_lower)

        # Bonus for comprehensive coverage
        coverage_bonus = min(term_matches / max(len(key_terms), 1), 1.0)

        # Penalty for very long paragraphs (prefer concise references)
        length_penalty = max(0, 1 - (len(paragraph) / 400))

        final_score = term_matches + coverage_bonus + length_penalty

        if final_score > 2.0:  # Higher threshold for paragraphs
            scored_segments.append(
                {"text": paragraph, "score": final_score, "type": "paragraph"}
            )

    # Sort by relevance and select diverse references
    scored_segments.sort(key=lambda x: x["score"], reverse=True)

    selected_references = []
    used_words = set()

    for segment in scored_segments[: max_refs * 2]:  # Consider more candidates
        if len(selected_references) >= max_refs:
            break

        # Check for overlap with already selected references
        segment_words = set(segment["text"].lower().split())
        overlap_ratio = (
            len(segment_words & used_words) / len(segment_words) if segment_words else 1
        )

        # Accept if overlap is reasonable (allows some redundancy for completeness)
        if overlap_ratio < 0.6:
            # Ensure reference is not too long (Chroma style: concise but complete)
            ref_text = segment["text"]
            if len(ref_text) > 600:  # Limit length
                # Try to find a good breaking point
                sentences_in_ref = [s.strip() for s in ref_text.split(".") if s.strip()]
                if len(sentences_in_ref) > 1:
                    # Take first few sentences up to reasonable length
                    truncated = ""
                    for sent in sentences_in_ref:
                        if len(truncated + sent) < 500:
                            truncated += sent + ". "
                        else:
                            break
                    ref_text = truncated.strip()
                else:
                    ref_text = ref_text[:500] + "..."

            selected_references.append(ref_text)
            used_words.update(segment_words)

    # Ensure we have at least one reference
    if not selected_references and scored_segments:
        selected_references.append(scored_segments[0]["text"][:500])

    return selected_references


def enhance_question_with_chroma_references(
    question_data: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Enhance a single question with Chroma-style multiple references.
    """
    try:
        # Load the original document content
        file_path = question_data.get("file_path", "")
        if not file_path or not os.path.exists(file_path):
            logger.warning(f"File not found: {file_path}")
            # Fallback: use existing golden_chunk as single reference
            enhanced_data = question_data.copy()
            enhanced_data["references"] = [
                question_data.get("golden_chunk", question_data.get("ground_truth", ""))
            ]
            enhanced_data["extraction_method"] = "fallback_original_chunk"
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

        # Keep original golden_chunk for comparison
        enhanced_data["original_golden_chunk"] = question_data.get("golden_chunk", "")

        return enhanced_data

    except Exception as e:
        logger.error(f"Error enhancing question: {str(e)}")
        # Return original data with minimal enhancement
        enhanced_data = question_data.copy()
        enhanced_data["references"] = [
            question_data.get("golden_chunk", question_data.get("ground_truth", ""))
        ]
        enhanced_data["extraction_method"] = "error_fallback"
        enhanced_data["num_references"] = 1
        return enhanced_data


def enhance_dataset_with_chroma_style():
    """
    Main function to enhance the existing dataset with Chroma-style multiple references.
    """
    logger.info("🚀 Starting Chroma-style dataset enhancement...")

    # Load existing dataset
    try:
        with open(EXISTING_DATASET_PATH, "r", encoding="utf-8") as f:
            existing_dataset = json.load(f)
        logger.info(
            f"✅ Loaded existing dataset with {len(existing_dataset.get('questions', []))} questions"
        )
    except Exception as e:
        logger.error(f"❌ Failed to load existing dataset: {str(e)}")
        return None

    # Create enhanced dataset structure
    enhanced_dataset = {
        "metadata": {
            "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source_dataset": "final_golden_chunk_dataset_100.json",
            "enhancement_method": "chroma_style_multi_references",
            "methodology": "Following Chroma research paper approach for multiple reference extraction",
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
            f"📝 Processing question {i + 1}/{len(questions)}: {question_data.get('question', 'Unknown')[:80]}..."
        )

        enhanced_question = enhance_question_with_chroma_references(question_data)
        enhanced_dataset["questions"].append(enhanced_question)

        # Update statistics
        method = enhanced_question.get("extraction_method", "unknown")
        num_refs = enhanced_question.get("num_references", 0)
        total_references += num_refs

        if "chroma_style" in method:
            enhanced_dataset["metadata"]["statistics"]["successful_enhancements"] += 1
        elif "fallback" in method:
            enhanced_dataset["metadata"]["statistics"]["fallback_used"] += 1
        elif "error" in method:
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
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            json.dump(enhanced_dataset, f, indent=2, ensure_ascii=False)
        logger.info(f"💾 Enhanced dataset saved to: {OUTPUT_PATH}")

        # Print summary
        stats = enhanced_dataset["metadata"]["statistics"]
        logger.info("\n" + "=" * 60)
        logger.info("📊 ENHANCEMENT SUMMARY")
        logger.info("=" * 60)
        logger.info(
            f"📋 Total questions processed: {len(enhanced_dataset['questions'])}"
        )
        logger.info(
            f"✅ Successful Chroma-style extractions: {stats['successful_enhancements']}"
        )
        logger.info(f"🔄 Fallback methods used: {stats['fallback_used']}")
        logger.info(f"❌ Errors encountered: {stats['error_count']}")
        logger.info(f"📚 Total references extracted: {stats['total_references']}")
        logger.info(
            f"📈 Average references per question: {stats['avg_references_per_question']:.2f}"
        )

        # Show example
        if enhanced_dataset["questions"]:
            example = enhanced_dataset["questions"][0]
            logger.info(f"\n📖 EXAMPLE ENHANCED QUESTION:")
            logger.info(f"❓ Question: {example['question'][:120]}...")
            logger.info(
                f"📝 Number of references: {len(example.get('references', []))}"
            )
            logger.info(
                f"🔧 Extraction method: {example.get('extraction_method', 'unknown')}"
            )

            for j, ref in enumerate(example.get("references", [])[:2]):
                logger.info(f"📄 Reference {j + 1} (first 100 chars): {ref[:100]}...")

        logger.info("=" * 60)
        return enhanced_dataset

    except Exception as e:
        logger.error(f"❌ Failed to save enhanced dataset: {str(e)}")
        return None


if __name__ == "__main__":
    result = enhance_dataset_with_chroma_style()
    if result:
        print("🎉 Successfully enhanced dataset with Chroma-style multiple references!")
        print(f"📁 Output saved to: {OUTPUT_PATH}")
    else:
        print("💥 Enhancement failed!")
