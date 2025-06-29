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

# Load environment variables from .env.local
load_dotenv(dotenv_path="/Users/id05309/Documents/tfm/.env.local")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Define paths
INPUT_FILE = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-semantic-hybrid-e5-base-v2/all_papers_data_semantic_metadata_cleaned_ids.json"
OUTPUT_FILE = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-semantic-hybrid-e5-base-v2/all_papers_data_semantic_metadata_cleaned_ids_context.json"
MARKDOWN_DIR = "/Users/id05309/Documents/tfm/mistral/mistral-markdown-no-ref-no-tables"


# Define a timeout exception
class GeminiTimeoutError(timeout_decorator.TimeoutError):
    pass


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((GeminiTimeoutError, ConnectionError)),
    reraise=True,
)
@timeout_decorator.timeout(30, timeout_exception=GeminiTimeoutError)
def get_gemini_response(prompt, model="gemini-2.0-flash"):
    """Get response from Gemini with timeout and retry logic"""
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a research assistant specializing in contextualizing academic content. Provide a short context on the paper and how this chunk relates to the overall document. Focus on key topics, relationships, and findings relevant to the chunk. Keep responses concise and optimized for search retrieval.",
                temperature=0.7,
                seed=42,
            ),
        )
        text = response.text
        return text.strip() if text else ""
    except Exception as e:
        if "rate limit" in str(e).lower():
            logger.warning(f"Rate limit hit: {str(e)}. Retrying...")
            # The explicit sleep is removed to allow Tenacity to handle backoff
        raise


def get_markdown_content(paper_id):
    """Get the full markdown content for a paper by searching in year subdirectories."""
    base_path = Path(MARKDOWN_DIR)

    # Search in all year subdirectories
    for year_dir in base_path.iterdir():
        if year_dir.is_dir() and year_dir.name.isdigit():  # Only check year directories
            md_path = year_dir / f"{paper_id}.md"
            if md_path.exists():
                try:
                    with open(md_path, "r", encoding="utf-8") as f:
                        return f.read()
                except Exception as e:
                    logger.error(f"Error reading markdown file {md_path}: {str(e)}")
                    return None

    logger.error(f"Could not find markdown file for {paper_id} in any year directory")
    return None


def augment_chunks_with_context():
    """Augment each chunk with contextual information from the full document."""
    print("Loading data...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Create checkpoint path
    checkpoint_dir = Path(OUTPUT_FILE).parent
    checkpoint_path = checkpoint_dir / "augmentation_checkpoint.json"

    # Load checkpoint if exists
    if checkpoint_path.exists():
        try:
            with open(checkpoint_path, "r", encoding="utf-8") as f:
                checkpoint_data = json.load(f)
                data = checkpoint_data

                # Count processed papers and chunks for logging
                processed_papers = sum(
                    all("augmented_page_content" in chunk for chunk in paper["chunks"])
                    for paper in data["papers"]
                )
                processed_chunks = sum(
                    sum(
                        1
                        for chunk in paper["chunks"]
                        if "augmented_page_content" in chunk
                    )
                    for paper in data["papers"]
                )

                logger.info(
                    f"Resumed from checkpoint with {processed_papers} fully processed papers "
                    f"and {processed_chunks} total processed chunks"
                )
        except Exception as e:
            logger.error(f"Error loading checkpoint: {str(e)}")

    total_papers = len(data["papers"])
    papers_completed = 0

    for paper_idx, paper in enumerate(data["papers"]):
        paper_id = paper["paper"]["paper_id"]
        logger.info(f"Processing paper {paper_idx + 1}/{total_papers}: {paper_id}")

        # Check if all chunks in this paper are already processed
        if all("augmented_page_content" in chunk for chunk in paper["chunks"]):
            logger.info(f"Skipping already fully processed paper: {paper_id}")
            papers_completed += 1
            continue

        start_time = time.time()

        # Get full document content
        document_content = get_markdown_content(paper_id)
        if not document_content:
            logger.error(f"Could not get document content for {paper_id}")
            continue

        chunks_processed = sum(
            1 for chunk in paper["chunks"] if "augmented_page_content" in chunk
        )
        total_chunks = len(paper["chunks"])

        for idx, chunk in enumerate(paper["chunks"]):
            # Skip already processed chunks
            if "augmented_page_content" in chunk:
                continue

            chunk_start_time = time.time()
            chunk_id = f"{paper_id}_chunk_{idx + 1}"
            chunk_content = chunk["page_content"]

            # Create the prompt using the specified template
            prompt = f"""<document>
                {document_content}
                </document>

                Here is the chunk we want to situate within the whole document
                <chunk>
                {chunk_content}
                </chunk>

                Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else."""

            try:
                contextual_phrase = get_gemini_response(prompt)

                # Prepend the contextual phrase to the chunk content
                chunk["augmented_page_content"] = f"{contextual_phrase} {chunk_content}"

                chunks_processed += 1
                processing_time = time.time() - chunk_start_time
                logger.info(
                    f"Successfully augmented chunk {chunk_id} [{chunks_processed}/{total_chunks}] in {processing_time:.2f}s"
                )

                # Save checkpoint after each chunk to be extra safe
                with open(checkpoint_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

            except GeminiTimeoutError:
                logger.error(f"Timeout while processing chunk {chunk_id}")
                # Don't set augmented_page_content so it will be retried next time
            except Exception as e:
                logger.error(f"Error augmenting chunk {chunk_id}: {str(e)}")
                # Don't set augmented_page_content so it will be retried next time

        # Check if all chunks for this paper are now processed
        if all("augmented_page_content" in chunk for chunk in paper["chunks"]):
            papers_completed += 1
            paper_processing_time = time.time() - start_time
            logger.info(f"Completed paper {paper_id} in {paper_processing_time:.2f}s")

        # Save checkpoint after each paper even if incomplete
        with open(checkpoint_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        logger.info(
            f"Progress: {papers_completed}/{total_papers} papers fully processed"
        )

    # Save final output
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    logger.info(f"Augmented chunks saved to {OUTPUT_FILE}")

    # Remove checkpoint
    if checkpoint_path.exists():
        try:
            checkpoint_path.unlink()
            logger.info("Checkpoint file removed after successful completion")
        except Exception as e:
            logger.warning(f"Could not remove checkpoint file: {str(e)}")


if __name__ == "__main__":
    augment_chunks_with_context()
