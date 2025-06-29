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


def is_low_value_chunk(text: str) -> bool:
    """Check if a chunk contains only low-value content like image captions,
    isolated author names, or other metadata that is not useful on its own.

    Returns:
        True if the chunk is considered low-value, False otherwise.
    """
    text = text.strip()

    # Patterns that often indicate low-value chunks
    patterns = [
        # Image captions
        r"^\s*\[IMAGE_\d+\].*Fig\..*$",
        r"^\s*Figure \d+[\.:].*$",
        r"^\s*Fig\. \d+[\.:].*$",
        r"^\s*Table \d+[\.:].*$",
        # Author information
        r"^\s*\*?Corresponding author.*$",
        r"^\s*Email address:.*$",
        r"^[\w\s,\.]+@[\w\.-]+\.\w+$",  # Simple email
        # Single affiliations
        r"^\s*\d*\s*Department of.*$",
        r"^\s*\d*\s*University of.*$",
        r"^\s*\d*\s*[A-Z][a-z]+ Institute of.*$",
    ]

    # Check if the chunk matches any low-value pattern and is short
    if count_tokens(text) < 100:
        for pattern in patterns:
            if re.match(pattern, text, re.MULTILINE | re.DOTALL):
                return True

    # Very short chunks are usually not useful alone
    if count_tokens(text) < 50:
        return True

    return False


def merge_small_chunks(chunks: list[str], min_tokens: int = 100) -> list[str]:
    """Merge chunks that are too small with the previous chunk.

    Special handling for the beginning of documents where title, authors, and
    affiliations are often split into separate chunks.
    """
    if not chunks:
        return chunks

    merged = [chunks[0]]
    current_chunk = chunks[0]
    current_tokens = count_tokens(current_chunk)

    for chunk in chunks[1:]:
        chunk_tokens = count_tokens(chunk)

        # Check if we should merge
        should_merge = False

        # Case 1: Current chunk is too small
        if current_tokens < min_tokens:
            should_merge = True

        # Case 2: Both chunks are small (likely metadata at start of document)
        elif current_tokens < min_tokens * 1.5 and chunk_tokens < min_tokens * 1.5:
            should_merge = True

        # Case 3: Next chunk is very small (likely a continuation)
        elif chunk_tokens < min_tokens * 0.5:
            should_merge = True

        if should_merge:
            # Merge with previous chunk
            current_chunk = f"{current_chunk}\n{chunk}"
            current_tokens = count_tokens(current_chunk)
            merged[-1] = current_chunk
        else:
            # Start a new chunk
            merged.append(chunk)
            current_chunk = chunk
            current_tokens = chunk_tokens

    return merged


def split_large_chunks(chunks: list[str], max_tokens: int = 600) -> list[str]:
    """Split chunks that are too large on sentence boundaries."""
    result = []
    for chunk in chunks:
        if count_tokens(chunk) <= max_tokens:
            result.append(chunk)
            continue

        # Split on sentence boundaries
        sentences = re.split(r"(?<=[.!?])\s+", chunk)
        current_chunk = ""

        for sentence in sentences:
            if count_tokens(current_chunk + sentence) <= max_tokens:
                current_chunk += sentence + " "
            else:
                if current_chunk:
                    result.append(current_chunk.strip())
                current_chunk = sentence + " "

        if current_chunk:
            result.append(current_chunk.strip())

    return result


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


def process_chunks(
    chunks: list[str], min_tokens: int = 250, max_tokens: int = 800
) -> list[str]:
    """Process chunks to ensure they're within the desired token range while preserving math content.

    Args:
        chunks: List of text chunks
        min_tokens: Minimum tokens allowed in a chunk
        max_tokens: Maximum tokens allowed in a chunk

    Returns:
        List of processed chunks with sizes between min and max tokens
    """
    if not chunks:
        return chunks

    # Initial pass: clean and validate chunks
    current_processed_chunks = []
    for chunk_text in chunks:
        stripped_chunk = chunk_text.strip()
        if stripped_chunk:  # Only keep non-empty chunks
            current_processed_chunks.append(stripped_chunk)

    if not current_processed_chunks:
        return []

    # Use a simplified merging approach that focuses solely on token counts
    final_chunks = []
    current_chunk = current_processed_chunks[0]
    current_math, current_clean = extract_math_spans(current_chunk)
    current_tokens = count_tokens(current_clean)

    # Process each chunk by comparing it with the next one
    for i in range(1, len(current_processed_chunks)):
        next_chunk = current_processed_chunks[i]
        next_math, next_clean = extract_math_spans(next_chunk)
        next_tokens = count_tokens(next_clean)

        # Decide whether to merge based on token counts
        combined_tokens = current_tokens + next_tokens

        if current_tokens < min_tokens and combined_tokens <= max_tokens:
            # Merge with next chunk
            current_chunk = current_chunk + "\n" + next_chunk
            current_math, current_clean = extract_math_spans(current_chunk)
            current_tokens = count_tokens(current_clean)
        else:
            # Add current chunk to final list and start with next chunk
            final_chunks.append(current_chunk)
            current_chunk = next_chunk
            current_math, current_clean = next_math, next_clean
            current_tokens = next_tokens

    # Add the last chunk
    if current_chunk:
        final_chunks.append(current_chunk)

    return final_chunks


def post_process_merge(
    chunks: list[str], min_tokens: int = 400, max_tokens: int = 512
) -> list[str]:
    """Post-process chunks to ensure all chunks meet minimum size requirements.

    This is a smarter approach that merges small chunks and avoids low-value content.

    Args:
        chunks: List of text chunks
        min_tokens: Minimum tokens required per chunk
        max_tokens: Maximum tokens allowed per chunk

    Returns:
        List of merged chunks meeting size requirements
    """
    if not chunks:
        return []

    # Prepare chunks with their token counts and low-value status
    processed_chunks = []
    for i, chunk in enumerate(chunks):
        math_formulas, clean_text = extract_math_spans(chunk)
        tokens = count_tokens(clean_text)
        is_low_value = is_low_value_chunk(chunk)
        processed_chunks.append(
            {"id": i, "text": chunk, "tokens": tokens, "is_low_value": is_low_value}
        )

    print(f"Initial chunks: {len(processed_chunks)}")
    print(f"Initial token counts: {[c['tokens'] for c in processed_chunks]}")
    print(
        f"Low-value chunks: {[c['id'] for c in processed_chunks if c['is_low_value']]}"
    )

    # Forward pass: Keep merging until no more merges can be done
    merged = True
    while merged and len(processed_chunks) > 1:
        merged = False
        new_chunks = []
        i = 0

        while i < len(processed_chunks):
            # If this is the last chunk, just add it
            if i == len(processed_chunks) - 1:
                new_chunks.append(processed_chunks[i])
                break

            current = processed_chunks[i]
            next_chunk = processed_chunks[i + 1]

            # Check if we should merge based on several criteria:
            should_merge = False

            # Case 1: Current chunk is below minimum size
            if current["tokens"] < min_tokens:
                should_merge = True

            # Case 2: Current chunk is low-value (figure caption, author info, etc.)
            if current["is_low_value"]:
                should_merge = True

            # Case 3: Next chunk is low-value and merging won't exceed max size
            if (
                next_chunk["is_low_value"]
                and current["tokens"] + next_chunk["tokens"] <= max_tokens
            ):
                should_merge = True

            # Check if merging won't exceed max size
            combined_tokens = current["tokens"] + next_chunk["tokens"]
            if should_merge and combined_tokens <= max_tokens:
                # Merge chunks
                merged_text = current["text"] + "\n" + next_chunk["text"]

                # Re-extract math and calculate tokens on merged text
                math, clean = extract_math_spans(merged_text)
                merged_tokens = count_tokens(clean)

                # Check if the merged chunk is still low-value (unlikely, but possible)
                merged_is_low_value = is_low_value_chunk(merged_text)

                new_chunks.append(
                    {
                        "id": current["id"],
                        "text": merged_text,
                        "tokens": merged_tokens,
                        "is_low_value": merged_is_low_value,
                    }
                )

                print(
                    f"Merged chunk {current['id']} ({current['tokens']} tokens, low_value={current['is_low_value']}) "
                    f"with chunk {next_chunk['id']} ({next_chunk['tokens']} tokens, low_value={next_chunk['is_low_value']})"
                )
                i += 2  # Skip next chunk
                merged = True
                continue

            # If no merge happened, keep current chunk as is
            new_chunks.append(current)
            i += 1

        # Update for next iteration
        processed_chunks = new_chunks

        if merged:
            print(f"After merging: {len(processed_chunks)} chunks")
            print(f"Token counts: {[c['tokens'] for c in processed_chunks]}")

    # Backward pass: Check if the last chunk is small and can be merged with the previous one
    # This ensures acknowledgments, footnotes, and other end material aren't left as tiny chunks
    if len(processed_chunks) >= 2:
        last_chunk = processed_chunks[-1]
        prev_chunk = processed_chunks[-2]

        if last_chunk["tokens"] < min_tokens:
            combined_tokens = prev_chunk["tokens"] + last_chunk["tokens"]
            if combined_tokens <= max_tokens:
                # Merge the last two chunks
                merged_text = prev_chunk["text"] + "\n" + last_chunk["text"]

                # Re-extract math and calculate tokens on merged text
                math, clean = extract_math_spans(merged_text)
                merged_tokens = count_tokens(clean)

                # Replace the last two chunks with the merged one
                processed_chunks = processed_chunks[:-2] + [
                    {
                        "id": prev_chunk["id"],
                        "text": merged_text,
                        "tokens": merged_tokens,
                    }
                ]

                print(
                    f"Merged last chunk {last_chunk['id']} ({last_chunk['tokens']} tokens) with previous chunk {prev_chunk['id']} ({prev_chunk['tokens']} tokens)"
                )
                print(f"Final chunks: {len(processed_chunks)}")
                print(f"Final token counts: {[c['tokens'] for c in processed_chunks]}")

    # Convert back to list of strings
    return [chunk["text"] for chunk in processed_chunks]


def chunk_markdown_file(
    md_path: Path, out_dir: Path, max_chunk_size: int = 512, min_chunk_size: int = 200
) -> dict:
    """Chunk a markdown file into smaller pieces while respecting boundaries.

    Returns:
        dict containing paper metadata and chunks
    """
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract math formulas and replace with placeholders
    math_formulas, clean_text = extract_math_spans(text)

    # 1. Split by headers
    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")]
    )
    sections = header_splitter.split_text(clean_text)

    # 2. Split sections into chunks with respect to special blocks
    # The overlap is set as a percentage of the max size.
    chunk_overlap = int(max_chunk_size * 0.1)
    chunker = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        model_name="gpt-4",
        chunk_size=max_chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\\n\\n\\n",  # Multiple paragraph breaks (section boundaries)
            "\\n\\n",  # Paragraphs
            "```\\n",  # Code blocks end
            "```",  # Code blocks start
            "\\n- ",  # List items
            "\\n## ",  # H2 headers
            "\\n### ",  # H3 headers
            "\\n",  # Regular line breaks (last resort)
            ". ",  # Sentences
            "! ",  # Exclamation sentences
            "? ",  # Question sentences
            ", ",  # Clauses
            " ",  # Words (last resort)
        ],
        keep_separator=True,
    )

    all_chunks = []
    for section in sections:
        # Convert Document to string if needed
        section_text = (
            section.page_content if hasattr(section, "page_content") else str(section)
        )

        # Split section into chunks
        chunks = chunker.split_text(section_text)

        # Clean up chunks
        chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

        # Add chunks to list
        all_chunks.extend(chunks)

    # Apply post-processing to merge small chunks
    merged_chunks = post_process_merge(
        all_chunks, min_tokens=min_chunk_size, max_tokens=max_chunk_size
    )

    # Ensure all chunks have proper math formulas
    final_chunks = []
    for chunk in merged_chunks:
        # Find which formulas are used in this chunk
        chunk_formulas = {}
        for placeholder, formula in math_formulas.items():
            if placeholder in chunk:
                chunk_formulas[placeholder] = formula

        final_chunks.append(chunk)

    # Create paper data structure
    paper_data = {
        "paper": {
            "paper_id": md_path.stem,
            "source_file": md_path.name,
            "num_chunks": len(final_chunks),
            "min_chunk_size": min(
                count_tokens(extract_math_spans(chunk)[1]) for chunk in final_chunks
            ),
            "max_chunk_size": max(
                count_tokens(extract_math_spans(chunk)[1]) for chunk in final_chunks
            ),
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
                "token_count": count_tokens(extract_math_spans(chunk)[1]),
                "contains_image": False,
                "images": {},
            },
        }
        paper_data["chunks"].append(chunk_data)

    return paper_data


def process_directory(
    input_dir: str,
    output_dir: str,
    max_chunk_size: int = 512,
    min_chunk_size: int = 200,
):
    """Process all markdown files in a directory.

    Args:
        input_dir: Directory containing markdown files
        output_dir: Directory to save chunked files
        max_chunk_size: Target max size for each chunk in tokens
        min_chunk_size: Target min size for each chunk in tokens
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

    # Process each file
    for md_file in md_files:
        try:
            print(f"\nProcessing {md_file}")
            paper_data = chunk_markdown_file(
                md_file, output_path, max_chunk_size, min_chunk_size
            )
            all_papers_data["papers"].append(paper_data)

        except Exception as e:
            print(f"Error processing {md_file}: {str(e)}")

    # Save all papers data
    output_file = output_path / "all_papers_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_papers_data, f, indent=2, ensure_ascii=False)

    num_papers = len(all_papers_data["papers"])
    all_chunks = [
        chunk for paper in all_papers_data["papers"] for chunk in paper["chunks"]
    ]
    total_chunks = len(all_chunks)
    total_tokens = sum(chunk["metadata"]["token_count"] for chunk in all_chunks)

    print(f"\nProcessed {num_papers} papers.")
    print(f"Total chunks created: {total_chunks}")
    if num_papers > 0:
        print(f"Average chunks per paper: {total_chunks / num_papers:.2f}")
    if total_chunks > 0:
        print(f"Average chunk size (tokens): {total_tokens / total_chunks:.2f}")

    print(f"Data saved to {output_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Chunk markdown files while preserving math formulas"
    )
    parser.add_argument(
        "--input",
        default="/Users/id05309/Documents/tfm/mistral/mistral-markdown-no-ref-no-tables",
        help="Input directory containing markdown files",
    )
    parser.add_argument(
        "--output",
        default="/Users/id05309/Documents/tfm/mistral/chunked-markdown-improved-256",
        help="Output directory for chunked files",
    )
    parser.add_argument(
        "--max-chunk-size",
        type=int,
        default=512,
        help="Target maximum size for each chunk in tokens",
    )
    parser.add_argument(
        "--min-chunk-size",
        type=int,
        default=200,
        help="Target minimum size for each chunk in tokens",
    )

    args = parser.parse_args()

    # Automatically create a unique output directory based on chunk size
    base_output_dir = Path(args.output).parent
    output_dir_name = f"chunked-markdown-{args.max_chunk_size}"
    final_output_dir = base_output_dir / output_dir_name

    print(f"Processing markdown files from {args.input}")
    print(f"Output will be saved to {final_output_dir}")
    print(f"Max chunk size: {args.max_chunk_size} tokens")
    print(f"Min chunk size: {args.min_chunk_size} tokens")

    process_directory(
        args.input, str(final_output_dir), args.max_chunk_size, args.min_chunk_size
    )
