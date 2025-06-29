import os

# Set MPS fallback BEFORE importing PyTorch/transformers to avoid embedding_bag errors
# This prevents NotImplementedError for aten::_embedding_bag on Apple Silicon
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

from pathlib import Path
import re
import tiktoken
import json
import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer
import warnings
import difflib
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

warnings.filterwarnings("ignore")


def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    """Count the number of tokens in a text string."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def extract_math_spans(text: str) -> tuple[dict[str, str], str]:
    """Extract math spans and replace them with placeholders.

    Args:
        text: Input text containing math formulas

    Returns:
        tuple containing:
        - dict mapping placeholder IDs to original math formulas
        - text with math formulas replaced by placeholders
    """
    # Split text into alternating non-math and math segments
    parts = re.split(r"(\$\$.*?\$\$|\$[^$\n]+\$)", text, flags=re.DOTALL)

    # Store math formulas and create placeholders
    math_formulas = {}
    clean_parts = []
    formula_id = 0

    for part in parts:
        if part.startswith("$") and part.endswith("$"):
            # HEURISTIC: If a "formula" is too long or contains many words,
            # it's likely a mis-classified text block from OCR.
            # Treat it as regular text to allow it to be chunked properly.
            word_count = len(part.split())
            line_count = part.count("\n")
            is_block_formula = part.startswith("$$")

            # Block math ($$..$$) can be longer, but not paragraph-length.
            # Inline math ($...$) should be very short.
            max_words = 40 if is_block_formula else 20
            max_lines = 8 if is_block_formula else 2

            # If it exceeds limits, treat it as normal text and don't create a placeholder
            if word_count > max_words or line_count > max_lines:
                clean_parts.append(part)
                continue

            # This seems like a legitimate formula, so create a placeholder.
            placeholder = f"[FORMULA{formula_id}]"
            math_formulas[placeholder] = part
            clean_parts.append(placeholder)
            formula_id += 1
        else:
            # This is regular text
            clean_parts.append(part)

    return math_formulas, "".join(clean_parts)


def restore_math_spans(text: str, math_formulas: dict[str, str]) -> str:
    """Restore math formulas from placeholders.

    Args:
        text: Text containing placeholders
        math_formulas: Dict mapping placeholders to original formulas

    Returns:
        Text with placeholders replaced by original math formulas
    """
    for placeholder, formula in math_formulas.items():
        text = text.replace(placeholder, formula)
    return text


class CustomSemanticChunker:
    """Custom semantic chunker using sentence transformers for better control."""

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",  # Lightweight model for semantic chunking
        min_chunk_size: int = 150,
        max_chunk_size: int = 512,  # Max tokens for e5-base-v2
        similarity_threshold: float = 0.7,  # Higher threshold for smaller chunks
    ):
        """
        Initialize the semantic chunker.

        Args:
            model_name: Name of the sentence transformer model
            min_chunk_size: Minimum tokens in a chunk
            max_chunk_size: Maximum tokens in a chunk (soft limit)
            similarity_threshold: Threshold for semantic similarity (higher = more splitting)
        """
        # Use MPS if available, CPU otherwise - lightweight model works well on both
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        # Simple model loading - no special configuration needed
        self.model = SentenceTransformer(model_name, device=device)
        self.min_chunk_size = min_chunk_size
        self.max_chunk_size = max_chunk_size
        self.similarity_threshold = similarity_threshold

    def _split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences, preserving paragraph structure."""
        # Split on sentence boundaries but keep paragraph breaks
        sentences = re.split(r"(?<=[.!?])\s+", text)
        return [s.strip() for s in sentences if s.strip()]

    def _calculate_similarities(self, sentences: List[str]) -> List[float]:
        """Calculate semantic similarities between adjacent sentences."""
        if len(sentences) < 2:
            return []

        # Get embeddings for all sentences
        embeddings = self.model.encode(sentences)

        # Calculate cosine similarities between adjacent sentences
        similarities = []
        for i in range(len(embeddings) - 1):
            sim = np.dot(embeddings[i], embeddings[i + 1]) / (
                np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[i + 1])
            )
            similarities.append(sim)

        return similarities

    def chunk_text(self, text: str) -> List[str]:
        """
        Chunk text based on semantic similarity.

        Args:
            text: Input clean text (with math placeholders) to chunk

        Returns:
            List of semantically coherent chunks (with math placeholders)
        """
        # Split into sentences
        sentences = self._split_into_sentences(text)

        if len(sentences) <= 1:
            return [text] if text.strip() else []

        # Calculate semantic similarities
        similarities = self._calculate_similarities(sentences)

        # Find split points where similarity drops below threshold
        split_points = [0]  # Always start with first sentence

        for i, sim in enumerate(similarities):
            if sim < self.similarity_threshold:
                split_points.append(i + 1)

        split_points.append(len(sentences))  # Always end with last sentence

        # Create chunks based on split points
        chunks = []
        for i in range(len(split_points) - 1):
            start_idx = split_points[i]
            end_idx = split_points[i + 1]
            chunk_sentences = sentences[start_idx:end_idx]
            chunk_text = " ".join(chunk_sentences)

            if chunk_text.strip():
                chunks.append(chunk_text.strip())

        # Post-process chunks for size constraints
        processed_chunks = self._adjust_chunk_sizes(chunks)

        # ABSOLUTE FINAL VALIDATION - HARD LIMIT ENFORCEMENT
        final_chunks = []
        for chunk in processed_chunks:
            if count_tokens(chunk) > self.max_chunk_size:
                # Emergency hard split - no semantic preservation
                hard_splits = self._emergency_hard_split(chunk)
                final_chunks.extend(hard_splits)
            else:
                final_chunks.append(chunk)

        return final_chunks

    def _adjust_chunk_sizes(self, chunks: List[str]) -> List[str]:
        """Adjust chunk sizes to meet min/max constraints with a robust linear process."""
        if not chunks:
            return []

        # Step 1: Aggressively split any chunks that are initially oversized.
        split_chunks = []
        for chunk in chunks:
            if count_tokens(chunk) > self.max_chunk_size:
                # Use the most robust splitting function to guarantee compliance
                split_chunks.extend(self._emergency_hard_split(chunk))
            else:
                split_chunks.append(chunk)

        if not split_chunks:
            return []

        # Step 2: Merge small chunks together.
        merged_chunks = []
        current_chunk = ""

        for chunk in split_chunks:
            # If we don't have a chunk to build upon, start with the current one.
            if not current_chunk:
                current_chunk = chunk
                continue

            # If the current accumulated chunk is too small, try merging.
            if count_tokens(current_chunk) < self.min_chunk_size:
                combined = current_chunk + "\n\n" + chunk
                if count_tokens(combined) <= self.max_chunk_size:
                    current_chunk = combined  # Merge succeeded
                else:
                    # Merge would be too large, so finalize the previous chunk.
                    merged_chunks.append(current_chunk)
                    current_chunk = chunk  # Start a new chunk.
            else:
                # Current chunk is large enough, so finalize it.
                merged_chunks.append(current_chunk)
                current_chunk = chunk  # Start a new chunk.

        # Add the last remaining chunk to the list.
        if current_chunk:
            merged_chunks.append(current_chunk)

        # Step 3: Final validation. Merging can create new oversized chunks.
        # This pass guarantees that every single chunk adheres to the max size limit.
        final_chunks = []
        for chunk in merged_chunks:
            if count_tokens(chunk) > self.max_chunk_size:
                final_chunks.extend(self._emergency_hard_split(chunk))
            else:
                final_chunks.append(chunk)

        return final_chunks

    def _force_split_oversized_chunk(self, chunk: str) -> List[str]:
        """Aggressively split a chunk that exceeds max_chunk_size while preserving formulas."""
        if count_tokens(chunk) <= self.max_chunk_size:
            return [chunk]

        # Split into sentences first
        sentences = self._split_into_sentences(chunk)

        # If single sentence is too big, split by words (formula-safe)
        if len(sentences) == 1 and count_tokens(sentences[0]) > self.max_chunk_size:
            return self._split_by_words_safe(sentences[0])

        # Otherwise, group sentences to stay under limit
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            sentence_tokens = count_tokens(sentence)
            current_tokens = count_tokens(current_chunk) if current_chunk else 0

            # If single sentence exceeds limit, split it further
            if sentence_tokens > self.max_chunk_size:
                # Save current chunk if it exists
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = ""

                # Split the oversized sentence (formula-safe)
                word_splits = self._split_by_words_safe(sentence)
                chunks.extend(word_splits)
                continue

            # If adding this sentence would exceed limit
            if current_tokens + sentence_tokens > self.max_chunk_size:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence
            else:
                if current_chunk:
                    current_chunk += " " + sentence
                else:
                    current_chunk = sentence

        # Add remaining chunk
        if current_chunk:
            chunks.append(current_chunk.strip())

        return [c for c in chunks if c.strip()]

    def _split_by_words(self, text: str) -> List[str]:
        """Split text by words when sentence-level splitting isn't enough."""
        # Use the formula-safe version
        return self._split_by_words_safe(text)

    def _split_by_characters(self, text: str) -> List[str]:
        """Emergency splitting by characters for extremely long words/tokens."""
        chunks = []
        current_chunk = ""

        for char in text:
            test_chunk = current_chunk + char
            if count_tokens(test_chunk) > self.max_chunk_size:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = char
            else:
                current_chunk = test_chunk

        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def _emergency_hard_split(self, text: str) -> List[str]:
        """Emergency hard split that preserves formula placeholders - GUARANTEES compliance."""
        if count_tokens(text) <= self.max_chunk_size:
            return [text]

        # Use formula-safe word splitting
        return self._split_by_words_safe(text)

    def _preserve_formula_boundaries(
        self, text: str, split_points: List[int]
    ) -> List[int]:
        """Adjust split points to avoid breaking formula placeholders.

        Args:
            text: The text being split
            split_points: Proposed character positions for splits

        Returns:
            Adjusted split points that preserve formula integrity
        """
        # Find all formula placeholders in the text
        formula_pattern = r"\[FORMULA\d+\]"
        formula_matches = list(re.finditer(formula_pattern, text))

        if not formula_matches:
            return split_points

        adjusted_points = []

        for split_point in split_points:
            # Check if this split point falls within any formula placeholder
            adjusted_point = split_point

            for match in formula_matches:
                start, end = match.span()

                # If split point is inside a formula placeholder
                if start < split_point < end:
                    # Move split point to before the formula (safer than after)
                    if start > 0:
                        adjusted_point = start
                    else:
                        # If formula is at the very beginning, move to after
                        adjusted_point = end
                    break

            adjusted_points.append(adjusted_point)

        return adjusted_points

    def _split_by_words_safe(self, text: str) -> List[str]:
        """Split text by words while preserving formula placeholders."""
        chunks = []
        current_chunk = ""
        # This pattern splits by spaces but also treats formula placeholders as single, unsplittable "words".
        word_pattern = r"(\[FORMULA\d+\]|\S+)"
        words = re.findall(word_pattern, text)

        for word in words:
            separator = " " if current_chunk else ""
            test_chunk = current_chunk + separator + word

            if count_tokens(test_chunk) > self.max_chunk_size:
                # Current chunk is full. Finalize it.
                if current_chunk:
                    chunks.append(current_chunk)

                # Now, analyze the word that didn't fit.
                if count_tokens(word) > self.max_chunk_size:
                    # This single "word" is oversized. This is the critical edge case.
                    # If it's a formula, we are forced to accept it as-is to avoid corruption.
                    if re.match(r"^\[FORMULA\d+\]$", word):
                        chunks.append(word)
                        current_chunk = ""
                    else:
                        # It's a long string of text. Hard split by character.
                        chunks.extend(self._split_by_characters(word))
                        current_chunk = ""
                else:
                    # The word is not oversized on its own, so it becomes the new current_chunk.
                    current_chunk = word
            else:
                # The word fits, so add it to the current chunk.
                current_chunk = test_chunk

        # Add the last remaining chunk to the list.
        if current_chunk:
            chunks.append(current_chunk)

        return [c.strip() for c in chunks if c.strip()]


def is_content_rich_section(text: str) -> bool:
    """Check if a section contains substantial content worth chunking."""
    # Remove math formulas for analysis
    _, clean_text = extract_math_spans(text)

    # Check token count
    token_count = count_tokens(clean_text)
    if token_count < 50:
        return False

    # Check for patterns that indicate substantial content
    content_indicators = [
        r"\b(however|therefore|furthermore|moreover|additionally)\b",
        r"\b(analysis|results|discussion|conclusion|introduction)\b",
        r"\b(we|our|this)\s+(study|research|paper|work)\b",
        r"\b(figure|table|equation)\s+\d+\b",
    ]

    for pattern in content_indicators:
        if re.search(pattern, clean_text, re.IGNORECASE):
            return True

    # Check sentence count and average length
    sentences = re.split(r"[.!?]+", clean_text)
    valid_sentences = [s.strip() for s in sentences if len(s.strip()) > 10]

    if len(valid_sentences) >= 3:
        avg_sentence_length = sum(len(s.split()) for s in valid_sentences) / len(
            valid_sentences
        )
        if avg_sentence_length > 8:  # Reasonable sentence length
            return True

    return False


def remove_repeated_formulas(text: str) -> str:
    """Remove repeated mathematical formulas that are likely OCR errors.

    Args:
        text: Input text that may contain repeated formulas

    Returns:
        Text with repeated formulas removed
    """
    # Extract all math formulas
    math_formulas, clean_text = extract_math_spans(text)

    # Find and remove repeated formulas
    seen_formulas = set()
    unique_formulas = {}

    for placeholder, formula in math_formulas.items():
        # Normalize formula by removing extra spaces
        normalized = re.sub(r"\s+", " ", formula.strip())

        if normalized not in seen_formulas:
            seen_formulas.add(normalized)
            unique_formulas[placeholder] = formula

    # Restore only unique formulas
    result = clean_text
    for placeholder, formula in unique_formulas.items():
        result = result.replace(placeholder, formula)

    return result


def detect_and_clean_repetitions(text: str, min_repetitions: int = 3) -> str:
    """Detect and clean repetitive content patterns that are likely OCR errors.

    Args:
        text: Input text that may contain repetitions
        min_repetitions: Minimum number of repetitions to consider it an error

    Returns:
        Cleaned text with repetitions removed
    """
    # Split into sentences
    sentences = re.split(r"(?<=[.!?])\s+", text)

    # Find repeating patterns
    for i in range(len(sentences)):
        if i + min_repetitions >= len(sentences):
            break

        # Check if next few sentences are similar
        current = sentences[i]
        next_sentences = sentences[i + 1 : i + min_repetitions]

        # If all next sentences are very similar to current
        if all(
            difflib.SequenceMatcher(None, current, s).ratio() > 0.8
            for s in next_sentences
        ):
            # Keep only the first occurrence
            return " ".join(sentences[: i + 1] + sentences[i + min_repetitions :])

    return text


# STRATEGY: Use lightweight model for chunking, e5-base-v2 for final embeddings
# - CustomSemanticChunker uses all-MiniLM-L6-v2 (fast, good semantic similarity)
# - HuggingFaceEmbeddings uses e5-base-v2 (strong for RAG)
model_name = "intfloat/e5-base-v2"
import torch

# Optimized device selection for MacBook M2
device = "mps" if torch.backends.mps.is_available() else "cpu"
model_kwargs = {"device": device}
# For e5 models, normalization is recommended
encode_kwargs = {"normalize_embeddings": True}

# Create model_kwargs with trust_remote_code for nomic models
if "nomic" in model_name.lower():
    model_kwargs_final = {**model_kwargs, "trust_remote_code": True}
else:
    model_kwargs_final = model_kwargs

hf_embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs_final,
    encode_kwargs=encode_kwargs,
)


def validate_and_fix_formula_placeholders(
    chunk_text: str, global_math_formulas: dict
) -> tuple[str, dict]:
    """Validate and fix any broken formula placeholders in chunk text.

    Args:
        chunk_text: The chunk text that may contain broken placeholders
        global_math_formulas: Dictionary of all available formula placeholders

    Returns:
        tuple of (fixed_chunk_text, chunk_specific_formulas)
    """
    # Find all complete formula placeholders in the chunk
    formula_pattern = r"\[FORMULA\d+\]"
    found_placeholders = re.findall(formula_pattern, chunk_text)

    # Check for broken placeholders (partial matches)
    broken_pattern = r"\[FORMULA?\d*\]?|\[FORMU[LA]*\d*\]?"
    potential_broken = re.findall(broken_pattern, chunk_text)

    # Remove complete placeholders from potential broken list
    broken_placeholders = [
        p for p in potential_broken if p not in found_placeholders and len(p) > 2
    ]

    fixed_text = chunk_text

    # Remove any broken placeholders
    for broken in broken_placeholders:
        fixed_text = fixed_text.replace(broken, "")

    # Clean up any double spaces left by removals
    fixed_text = re.sub(r"\s+", " ", fixed_text).strip()

    # Get formulas that are actually present in the fixed text
    chunk_formulas = {
        placeholder: formula
        for placeholder, formula in global_math_formulas.items()
        if placeholder in fixed_text
    }

    return fixed_text, chunk_formulas


def chunk_markdown_file_semantic(
    md_path: Path,
    custom_chunker: CustomSemanticChunker,
) -> dict:
    """
    Chunk a markdown file using a purely semantic approach.

    Args:
        md_path: Path to the markdown file
        custom_chunker: An instance of the configured CustomSemanticChunker.

    Returns:
        dict containing paper metadata and chunks
    """
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Pre-process text
    text = remove_repeated_formulas(text)
    text = detect_and_clean_repetitions(text)

    # Extract math formulas and get clean text with placeholders
    global_math_formulas, clean_text = extract_math_spans(text)

    # Apply semantic chunking directly to the entire document's clean text
    all_chunks_clean = custom_chunker.chunk_text(clean_text)

    # Process final chunks and add metadata
    final_chunks_data = []
    for i, chunk_text_with_placeholders in enumerate(all_chunks_clean):
        # Validate and fix any broken formula placeholders
        fixed_chunk_text, chunk_math_formulas = validate_and_fix_formula_placeholders(
            chunk_text_with_placeholders, global_math_formulas
        )

        # Restore math only to get an accurate token count for metadata
        text_for_token_count = restore_math_spans(fixed_chunk_text, chunk_math_formulas)

        chunk_data = {
            "chunk_id": i + 1,
            "page_content": fixed_chunk_text,
            "metadata": {
                "contains_formula": bool(chunk_math_formulas),
                "formulas": chunk_math_formulas,
                "token_count": count_tokens(text_for_token_count),
                "contains_image": False,
                "images": {},
                "chunking_method": "hybrid_semantic_v1",
            },
        }
        final_chunks_data.append(chunk_data)

    # Create paper data structure
    paper_data = {
        "paper": {
            "paper_id": md_path.stem,
            "source_file": md_path.name,
            "num_chunks": len(final_chunks_data),
            "chunking_method": "hybrid_semantic_v1",
        },
        "chunks": final_chunks_data,
    }

    return paper_data


def validate_chunk_sizes(
    chunks_data: List[dict], max_allowed_tokens: int = 512
) -> dict:
    """Validate that all chunks meet size requirements.

    Args:
        chunks_data: List of chunk dictionaries with metadata
        max_allowed_tokens: Maximum allowed tokens per chunk

    Returns:
        Dictionary with validation statistics
    """
    oversized_chunks = []
    all_sizes = []

    for i, chunk in enumerate(chunks_data):
        token_count = chunk["metadata"]["token_count"]
        all_sizes.append(token_count)

        if token_count > max_allowed_tokens:
            oversized_chunks.append(
                {
                    "chunk_id": chunk["chunk_id"],
                    "token_count": token_count,
                    "excess_tokens": token_count - max_allowed_tokens,
                }
            )

    return {
        "total_chunks": len(chunks_data),
        "oversized_chunks": len(oversized_chunks),
        "oversized_details": oversized_chunks,
        "max_size": max(all_sizes) if all_sizes else 0,
        "min_size": min(all_sizes) if all_sizes else 0,
        "avg_size": sum(all_sizes) / len(all_sizes) if all_sizes else 0,
        "median_size": sorted(all_sizes)[len(all_sizes) // 2] if all_sizes else 0,
        "compliance_rate": (len(chunks_data) - len(oversized_chunks))
        / len(chunks_data)
        * 100
        if chunks_data
        else 100,
    }


def process_directory_semantic(
    input_dir: str,
    output_dir: str,
    similarity_threshold: float,
    min_chunk_size: int,
    max_chunk_size: int,
):
    """Process all markdown files in a directory using semantic chunking.
       This process is robust and resumable.

    Args:
        input_dir: Directory containing markdown files
        output_dir: Directory to save chunked files
        similarity_threshold: Threshold for semantic similarity
        min_chunk_size: Minimum tokens per chunk
        max_chunk_size: Maximum tokens per chunk
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    output_file = output_path / "all_papers_data_semantic.json"

    # Load existing data if it exists to make the script resumable
    if output_file.exists():
        with open(output_file, "r", encoding="utf-8") as f:
            all_papers_data = json.load(f)
        processed_papers = {
            paper["paper"]["paper_id"] for paper in all_papers_data["papers"]
        }
        print(f"Loaded {len(processed_papers)} already processed papers.")
    else:
        all_papers_data = {"papers": []}
        processed_papers = set()

    # Initialize the custom chunker with the given parameters
    custom_chunker = CustomSemanticChunker(
        similarity_threshold=similarity_threshold,
        min_chunk_size=min_chunk_size,
        max_chunk_size=max_chunk_size,
    )

    md_files = list(input_path.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files to process.")

    for md_file in md_files:
        paper_id = md_file.stem
        if paper_id in processed_papers:
            print(f"Skipping already processed file: {md_file.name}")
            continue

        try:
            print(f"\n{'=' * 60}")
            print(f"Processing {md_file}")
            print(f"{'=' * 60}")

            paper_data = chunk_markdown_file_semantic(
                md_file,
                custom_chunker,
            )

            # Validate chunk sizes for this paper
            validation = validate_chunk_sizes(paper_data["chunks"], max_chunk_size)

            all_papers_data["papers"].append(paper_data)

            # Save progress after each file
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(all_papers_data, f, indent=2, ensure_ascii=False)

            processed_papers.add(paper_id)

            paper_info = paper_data["paper"]
            print(f"\nPaper: {paper_info['paper_id']}")
            print(f"Chunks created: {paper_info['num_chunks']}")
            print(
                f"Size compliance: {validation['compliance_rate']:.1f}% (max: {validation['max_size']} tokens)"
            )
            if validation["oversized_chunks"] > 0:
                print(
                    f"⚠️  WARNING: {validation['oversized_chunks']} chunks exceed {max_chunk_size} tokens!"
                )
            print(f"Progress saved to {output_file.name}")

        except Exception as e:
            print(f"Error processing {md_file}: {str(e)}")
            import traceback

            traceback.print_exc()

    # Final comprehensive validation
    all_chunks = []
    for paper in all_papers_data["papers"]:
        all_chunks.extend(paper["chunks"])

    final_validation = validate_chunk_sizes(all_chunks, max_chunk_size)

    total_chunks = sum(len(paper["chunks"]) for paper in all_papers_data["papers"])
    print(f"\n{'=' * 60}")
    print("FINAL SUMMARY")
    print(f"{'=' * 60}")
    print(f"Processed {len(all_papers_data['papers'])} papers")
    print(f"Total chunks: {total_chunks}")
    print(f"\nChunk Size Analysis:")
    print(f"  Compliance rate: {final_validation['compliance_rate']:.1f}%")
    print(f"  Oversized chunks: {final_validation['oversized_chunks']}")
    print(f"  Min size: {final_validation['min_size']} tokens")
    print(f"  Max size: {final_validation['max_size']} tokens")
    print(f"  Average size: {final_validation['avg_size']:.1f} tokens")
    print(f"  Median size: {final_validation['median_size']} tokens")

    if final_validation["oversized_chunks"] > 0:
        print(
            f"\n⚠️  ATTENTION: {final_validation['oversized_chunks']} chunks still exceed {max_chunk_size} tokens!"
        )
        print("Consider lowering similarity_threshold or max_chunk_size parameters.")

        # Show worst offenders
        oversized = sorted(
            final_validation["oversized_details"],
            key=lambda x: x["token_count"],
            reverse=True,
        )[:5]
        print("\nLargest oversized chunks:")
        for chunk_info in oversized:
            print(
                f"  Chunk {chunk_info['chunk_id']}: {chunk_info['token_count']} tokens "
                f"({chunk_info['excess_tokens']} over limit)"
            )
    else:
        print(f"\n✅ All chunks comply with {max_chunk_size} token limit!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Chunk markdown files using a hybrid structural and semantic approach."
    )
    parser.add_argument(
        "--input",
        default="/Users/id05309/Documents/tfm/mistral/mistral-markdown-no-ref-no-tables",
        help="Input directory containing markdown files",
    )
    parser.add_argument(
        "--output",
        default="/Users/id05309/Documents/tfm/mistral/chunked-markdown-semantic-hybrid-e5-base-v2",
        help="Output directory for chunked files",
    )
    parser.add_argument(
        "--similarity-threshold",
        type=float,
        default=0.6,  # Lower threshold for smaller, more cohesive chunks
        help="Similarity threshold for semantic splitting (higher = more splits)",
    )
    parser.add_argument(
        "--min-chunk-size",
        type=int,
        default=100,  # Smaller minimum for more granular chunks
        help="Minimum tokens per chunk",
    )
    parser.add_argument(
        "--max-chunk-size",
        type=int,
        default=510,  # Stricter max tokens for e5-base-v2 to be safe
        help="Maximum tokens per chunk (e.g., 512 for e5-base-v2)",
    )
    args = parser.parse_args()

    print(f"Processing markdown files from {args.input}")
    print(f"Output will be saved to {args.output}")
    print(f"Chunking parameters:")
    print(f"  - Similarity Threshold: {args.similarity_threshold}")
    print(f"  - Min Chunk Size: {args.min_chunk_size} tokens")
    print(f"  - Max Chunk Size: {args.max_chunk_size} tokens")

    process_directory_semantic(
        args.input,
        args.output,
        args.similarity_threshold,
        args.min_chunk_size,
        args.max_chunk_size,
    )
