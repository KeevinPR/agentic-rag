from pathlib import Path
import re
import os
import tiktoken
from langchain.text_splitter import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)
import json


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
            # This is a math formula
            placeholder = f"[FORMULA{formula_id}]"
            math_formulas[placeholder] = part
            clean_parts.append(placeholder)
            formula_id += 1
        else:
            # This is regular text
            clean_parts.append(part)

    return math_formulas, "".join(clean_parts)


def simple_chunk_markdown_file(
    md_path: Path,
    target_chunk_size: int = 240,  # Target closer to max for better compliance
    max_chunk_size: int = 280,  # Slightly higher to allow more flexibility
    min_chunk_size: int = 180,  # Higher minimum to push chunks up
) -> dict:
    """Chunk a markdown file into smaller pieces targeting 200-250 tokens.

    Args:
        md_path: Path to markdown file
        target_chunk_size: Target chunk size in tokens
        max_chunk_size: Maximum allowed chunk size
        min_chunk_size: Minimum chunk size before merging

    Returns:
        dict containing paper metadata and chunks
    """
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    print(f"\nProcessing: {md_path.name}")

    # Extract math formulas first
    math_formulas, clean_text = extract_math_spans(text)
    print(f"Extracted {len(math_formulas)} math formulas")

    # 1. Split by headers first to respect document structure
    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")]
    )
    sections = header_splitter.split_text(clean_text)
    print(f"Split into {len(sections)} sections")

    # 2. Process each section individually with recursive chunking
    all_chunks = []

    # Use recursive chunker with NO overlap and target size
    chunker = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        model_name="gpt-4",
        chunk_size=target_chunk_size,  # Use target size, not max
        chunk_overlap=0,  # NO overlap
        separators=[
            "\n\n\n",  # Multiple paragraph breaks
            "\n\n",  # Paragraph breaks
            "```\n",  # Code block endings
            "```",  # Code block starts
            "\n- ",  # List items
            "\n* ",  # Bullet points
            "\n",  # Line breaks
            ". ",  # Sentence endings
            "! ",  # Exclamation sentences
            "? ",  # Question sentences
            ", ",  # Comma separations
            " ",  # Words (last resort)
        ],
        keep_separator=True,
    )

    for section in sections:
        # Convert Document to string if needed
        section_text = (
            section.page_content if hasattr(section, "page_content") else str(section)
        )

        if not section_text.strip():
            continue

        # Check if section is already small enough
        section_tokens = count_tokens(section_text)

        if section_tokens <= max_chunk_size:
            # Section is already the right size
            all_chunks.append(section_text.strip())
        else:
            # Split section into smaller chunks
            section_chunks = chunker.split_text(section_text)

            # Clean and filter chunks
            for chunk in section_chunks:
                chunk = chunk.strip()
                if chunk and count_tokens(chunk) >= 50:  # Ignore very small chunks
                    all_chunks.append(chunk)

    print(f"Initial chunks: {len(all_chunks)}")

    # 3. More aggressive merging to push chunks into target range
    final_chunks = []
    i = 0

    while i < len(all_chunks):
        current_chunk = all_chunks[i]
        current_tokens = count_tokens(current_chunk)

        # Try to merge if chunk is below target range OR small enough to benefit from merging
        should_try_merge = (
            current_tokens < 200  # Below target range
            or (
                current_tokens < target_chunk_size * 0.8 and i + 1 < len(all_chunks)
            )  # Small and has next chunk
        )

        if should_try_merge and i + 1 < len(all_chunks):
            next_chunk = all_chunks[i + 1]
            next_tokens = count_tokens(next_chunk)
            combined = current_chunk + "\n\n" + next_chunk
            combined_tokens = count_tokens(combined)

            # Merge if it keeps us within max size and improves the situation
            if combined_tokens <= max_chunk_size:
                final_chunks.append(combined)
                print(
                    f"Merged chunks {i} and {i + 1}: {current_tokens} + {next_tokens} = {combined_tokens} tokens"
                )
                i += 2  # Skip next chunk
                continue

        # Add chunk as-is
        final_chunks.append(current_chunk)
        i += 1

    # Calculate statistics
    token_counts = [count_tokens(chunk) for chunk in final_chunks]

    print(f"Final chunks: {len(final_chunks)}")
    print(
        f"Token counts - Min: {min(token_counts)}, Max: {max(token_counts)}, Avg: {sum(token_counts) / len(token_counts):.1f}"
    )
    print(
        f"Chunks in target range (200-250): {sum(1 for t in token_counts if 200 <= t <= 250)}/{len(token_counts)}"
    )

    # Create paper data structure
    paper_data = {
        "paper": {
            "paper_id": md_path.stem,
            "source_file": md_path.name,
            "num_chunks": len(final_chunks),
            "min_chunk_size": min(token_counts),
            "max_chunk_size": max(token_counts),
            "avg_chunk_size": sum(token_counts) / len(token_counts),
            "target_range_chunks": sum(1 for t in token_counts if 200 <= t <= 250),
        },
        "chunks": [],
    }

    # Process chunks and add to paper data
    for i, chunk in enumerate(final_chunks):
        # Find which formulas are used in this chunk
        chunk_formulas = {}
        for placeholder, formula in math_formulas.items():
            if placeholder in chunk:
                chunk_formulas[placeholder] = formula

        chunk_data = {
            "chunk_id": i + 1,
            "page_content": chunk,  # Keep the placeholders in page_content
            "metadata": {
                "contains_formula": bool(chunk_formulas),
                "formulas": chunk_formulas,
                "token_count": count_tokens(chunk),
                "contains_image": False,
                "images": {},
            },
        }
        paper_data["chunks"].append(chunk_data)

    return paper_data


def process_directory_simple(
    input_dir: str,
    output_dir: str,
    target_chunk_size: int = 240,
    max_chunk_size: int = 280,
    min_chunk_size: int = 180,
):
    """Process all markdown files with simplified chunking strategy.

    Args:
        input_dir: Directory containing markdown files
        output_dir: Directory to save chunked files
        target_chunk_size: Target chunk size in tokens
        max_chunk_size: Maximum chunk size in tokens
        min_chunk_size: Minimum chunk size in tokens
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    # Get all markdown files
    md_files = list(input_path.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files")

    # Process all papers
    all_papers_data = {"papers": []}

    # Track statistics
    total_chunks = 0
    total_tokens = 0
    target_range_chunks = 0

    # Process each file
    for md_file in md_files:
        try:
            paper_data = simple_chunk_markdown_file(
                md_file, target_chunk_size, max_chunk_size, min_chunk_size
            )
            all_papers_data["papers"].append(paper_data)

            # Update statistics
            paper_chunks = len(paper_data["chunks"])
            paper_tokens = sum(
                chunk["metadata"]["token_count"] for chunk in paper_data["chunks"]
            )
            paper_target_range = paper_data["paper"]["target_range_chunks"]

            total_chunks += paper_chunks
            total_tokens += paper_tokens
            target_range_chunks += paper_target_range

        except Exception as e:
            print(f"Error processing {md_file}: {str(e)}")

    # Save all papers data
    output_file = output_path / "all_papers_data_simple.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_papers_data, f, indent=2, ensure_ascii=False)

    num_papers = len(all_papers_data["papers"])

    print(f"\n" + "=" * 60)
    print(f"FINAL STATISTICS")
    print(f"=" * 60)
    print(f"Processed papers: {num_papers}")
    print(f"Total chunks: {total_chunks}")
    print(f"Total tokens: {total_tokens:,}")

    if num_papers > 0:
        print(f"Average chunks per paper: {total_chunks / num_papers:.1f}")
    if total_chunks > 0:
        print(f"Average chunk size: {total_tokens / total_chunks:.1f} tokens")
        print(
            f"Chunks in target range (200-250): {target_range_chunks}/{total_chunks} ({target_range_chunks / total_chunks * 100:.1f}%)"
        )

    print(f"\nData saved to {output_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Simple chunking for markdown files targeting 200-250 tokens"
    )
    parser.add_argument(
        "--input",
        default="/Users/id05309/Documents/tfm/mistral/mistral-markdown-no-ref-no-tables",
        help="Input directory containing markdown files",
    )
    parser.add_argument(
        "--output",
        default="/Users/id05309/Documents/tfm/mistral/chunked-markdown-simple-v2",
        help="Output directory for chunked files",
    )
    parser.add_argument(
        "--target-size",
        type=int,
        default=240,
        help="Target chunk size in tokens (default: 240)",
    )
    parser.add_argument(
        "--max-size",
        type=int,
        default=280,
        help="Maximum chunk size in tokens (default: 280)",
    )
    parser.add_argument(
        "--min-size",
        type=int,
        default=180,
        help="Minimum chunk size in tokens (default: 180)",
    )

    args = parser.parse_args()

    print(f"Processing markdown files from {args.input}")
    print(f"Output will be saved to {args.output}")
    print(f"Target chunk size: {args.target_size} tokens")
    print(f"Max chunk size: {args.max_size} tokens")
    print(f"Min chunk size: {args.min_size} tokens")

    process_directory_simple(
        args.input, args.output, args.target_size, args.max_size, args.min_size
    )
