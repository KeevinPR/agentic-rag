import json
from pathlib import Path
import tiktoken
import logging

# --- Configuration ---
# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Define the input file path
INPUT_FILE = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-1024/all_papers_data_metadata_cleaned_ids.json"
TOKEN_THRESHOLD = 512


def count_tokens(text: str, model: str = "cl100k_base") -> int:
    """
    Counts the number of tokens in a text string using tiktoken.
    Uses a common encoding suitable for many models.
    """
    if not isinstance(text, str):
        return 0
    try:
        # cl100k_base is the encoding used by gpt-4, gpt-3.5-turbo, and embedding models
        encoding = tiktoken.get_encoding(model)
    except KeyError:
        logger.warning(
            f"Encoding '{model}' not found. Using cl100k_base as a fallback."
        )
        encoding = tiktoken.get_encoding("cl100k_base")

    # Using disallowed_special=() is a robust way to handle all text
    return len(encoding.encode(text, disallowed_special=()))


def analyze_chunk_tokens(file_path: str):
    """
    Loads a JSON file, re-counts tokens for each chunk's page_content using
    tiktoken, and prints detailed statistics.
    """
    path = Path(file_path)
    if not path.exists():
        logger.error(f"File not found: {file_path}")
        return

    logger.info(f"Loading data from {file_path}...")
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        logger.error("Error: Invalid JSON format in the file.")
        return
    except Exception as e:
        logger.error(f"An unexpected error occurred while reading the file: {e}")
        return

    overall_total_chunks = 0
    overall_total_tokens = 0
    overall_long_chunks = 0

    papers = data.get("papers", [])
    logger.info(f"Found {len(papers)} papers to process.")

    for paper_item in papers:
        paper_meta = paper_item.get("paper", {})
        title = paper_meta.get("title", "Untitled Paper")
        chunks = paper_item.get("chunks", [])

        paper_chunk_count = len(chunks)
        paper_total_tokens = 0
        paper_long_chunks = 0

        for chunk in chunks:
            page_content = chunk.get("page_content", "")
            # Re-calculate token count using tiktoken
            token_count = count_tokens(page_content)

            paper_total_tokens += token_count
            if token_count > TOKEN_THRESHOLD:
                paper_long_chunks += 1

        avg_chunk_len = (
            paper_total_tokens / paper_chunk_count if paper_chunk_count > 0 else 0
        )

        print("-" * 60)
        print(f"Paper: {title}")
        print(f"  Total Chunks: {paper_chunk_count}")
        print(f"  Total Tokens (re-counted): {paper_total_tokens}")
        print(f"  Average Chunk Length: {avg_chunk_len:.2f} tokens")
        print(f"  Chunks > {TOKEN_THRESHOLD} tokens: {paper_long_chunks}")

        overall_total_chunks += paper_chunk_count
        overall_total_tokens += paper_total_tokens
        overall_long_chunks += paper_long_chunks

    print("=" * 60)
    print("Overall Corpus Statistics")
    print("=" * 60)
    overall_avg = (
        overall_total_tokens / overall_total_chunks if overall_total_chunks > 0 else 0
    )
    print(f"Total Papers Processed: {len(papers)}")
    print(f"Total Chunks Across All Papers: {overall_total_chunks}")
    print(f"Total Tokens Across All Papers (re-counted): {overall_total_tokens}")
    print(f"Overall Average Chunk Length: {overall_avg:.2f} tokens")
    print(f"Total Chunks > {TOKEN_THRESHOLD} tokens: {overall_long_chunks}")


if __name__ == "__main__":
    analyze_chunk_tokens(INPUT_FILE)
