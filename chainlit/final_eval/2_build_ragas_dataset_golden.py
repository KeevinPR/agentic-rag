import os
import json
import glob
import argparse
import logging
from typing import List, Dict, Any, Union
import re

from ragas.dataset_schema import SingleTurnSample, EvaluationDataset

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extract_contexts_from_data(contexts_data: Dict[str, Any]) -> List[str]:
    """
    Extract all context strings from the contexts dictionary.
    Combines contexts from hybrid_search, paper_database, and web_search.
    """
    all_contexts = []

    # Extract from hybrid_search
    hybrid_contexts = contexts_data.get("hybrid_search", [])
    if isinstance(hybrid_contexts, list):
        all_contexts.extend([str(ctx) for ctx in hybrid_contexts if ctx])

    # Extract from paper_database
    paper_contexts = contexts_data.get("paper_database", [])
    if isinstance(paper_contexts, list):
        all_contexts.extend([str(ctx) for ctx in paper_contexts if ctx])

    # Extract from web_search
    web_contexts = contexts_data.get("web_search", [])
    if isinstance(web_contexts, list):
        all_contexts.extend([str(ctx) for ctx in web_contexts if ctx])

    return all_contexts


def validate_json_file(filepath: str) -> bool:
    """
    Validate that the JSON file can be parsed successfully.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            json.load(f)
        return True
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {filepath}: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Error reading {filepath}: {str(e)}")
        return False


def process_single_file(filepath: str) -> SingleTurnSample:
    """
    Process a single JSON file into a SingleTurnSample.

    Expected JSON structure:
    {
        "question": "string",
        "ground_truth": "string",
        "final_answer": "string",
        "reference": "string",
        "chunks": [{}],
        "contexts": {
            "hybrid_search": ["string"],
            "paper_database": [],
            "web_search": []
        },
        "tool_calls": [{"name": "string", "args": {}}],
        "error": "boolean",
        "timestamp": "string"
    }
    """
    if not validate_json_file(filepath):
        raise ValueError(f"Invalid JSON file: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Extract required fields
    question = data.get("question", "")
    if not question:
        logger.warning(f"No question found in {filepath}")
        question = "No question provided"

    final_answer = data.get("final_answer", "")
    if not final_answer:
        logger.warning(f"No final_answer found in {filepath}")
        final_answer = "No answer provided"

    ground_truth = data.get("ground_truth", "")

    reference = data.get("reference", "")

    if isinstance(reference, list):
        reference_contexts = reference
    elif isinstance(reference, str) and reference.strip():
        reference_contexts = [reference]
    else:
        reference_contexts = []

    # Extract contexts
    contexts_data = data.get("contexts", {})
    retrieved_contexts = extract_contexts_from_data(contexts_data)

    if not retrieved_contexts:
        logger.warning(f"No contexts found in {filepath}")
        retrieved_contexts = []

    # Log some stats for debugging
    logger.debug(f"File: {os.path.basename(filepath)}")
    logger.debug(f"  Question length: {len(question)}")
    logger.debug(f"  Answer length: {len(final_answer)}")
    logger.debug(f"  Ground truth length: {len(ground_truth)}")
    logger.debug(f"  Retrieved contexts: {len(retrieved_contexts)}")

    # Create SingleTurnSample
    sample = SingleTurnSample(
        user_input=question,
        response=final_answer,
        retrieved_contexts=retrieved_contexts,
        reference_contexts=reference_contexts,
        reference=ground_truth if ground_truth else None,
    )

    return sample


def natural_sort_key(s):
    """
    Key for natural sorting (alphanumeric sorting) of strings.
    Handles numbers within strings correctly.
    """
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split("([0-9]+)", s)
    ]


def build_dataset_from_folder(input_folder: str, output_folder: str):
    """
    Build a Ragas dataset from a folder of JSON files.
    """
    pattern = os.path.join(input_folder, "*.json")
    files = sorted(
        glob.glob(pattern), key=natural_sort_key
    )  # Sort files to ensure consistent order

    if not files:
        logger.error(f"No JSON files found in {input_folder}")
        return

    logger.info(f"Found {len(files)} JSON files to process")

    samples: List[SingleTurnSample] = []
    failed_files = []

    for fp in files:
        logger.info(f"→ Processing {os.path.basename(fp)}...")
        try:
            sample = process_single_file(fp)
            samples.append(sample)
            logger.info(f"✅ Successfully processed {os.path.basename(fp)}")
        except Exception as e:
            logger.error(f"❌ Failed processing {fp}: {e}")
            failed_files.append(fp)

    if not samples:
        logger.error("No samples were successfully processed!")
        return

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create and save the dataset
    dataset = EvaluationDataset(samples=samples)
    output_path = os.path.join(output_folder, "dataset.jsonl")
    dataset.to_jsonl(output_path)

    # Print summary
    logger.info(f"✅ Successfully processed {len(samples)} samples")
    if failed_files:
        logger.warning(f"⚠️  Failed to process {len(failed_files)} files:")
        for fp in failed_files:
            logger.warning(f"   - {os.path.basename(fp)}")

    logger.info(f"📁 Saved Ragas dataset to: {output_path}")

    # Save a summary report
    summary = {
        "total_files": len(files),
        "successful_samples": len(samples),
        "failed_files": len(failed_files),
        "failed_file_names": [os.path.basename(fp) for fp in failed_files],
        "output_path": output_path,
    }

    summary_path = os.path.join(output_folder, "processing_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    logger.info(f"📊 Processing summary saved to: {summary_path}")


def load_and_validate_dataset(dataset_path: str) -> EvaluationDataset:
    """
    Load and validate a Ragas dataset from JSONL file.
    """
    try:
        dataset = EvaluationDataset.from_jsonl(dataset_path)
        logger.info(f"✅ Loaded dataset with {len(dataset.samples)} samples")

        # Validate first few samples
        for i, sample in enumerate(dataset.samples[:3]):
            logger.info(f"Sample {i + 1}:")
            logger.info(f"  User input: {sample.user_input[:100]}...")
            logger.info(f"  Response: {sample.response[:100]}...")
            logger.info(f"  Retrieved contexts: {len(sample.retrieved_contexts)}")
            if sample.reference:
                logger.info(f"  Reference: {sample.reference[:100]}...")

        return dataset
    except Exception as e:
        logger.error(f"Failed to load dataset from {dataset_path}: {e}")
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Build a Ragas SingleTurnSample dataset from a folder of JSON files."
    )
    parser.add_argument(
        "--input_folder",
        type=str,
        default="final-v2-100/logs/",
        help="Path to the folder containing JSON files with the specified schema",
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        default="ragas_dataset_final-v2-100",
        help="Where to write the Ragas dataset (JSONL format)",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate the created dataset by loading it back",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging",
    )

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    # Build the dataset
    build_dataset_from_folder(args.input_folder, args.output_folder)

    # Optionally validate the created dataset
    if args.validate:
        dataset_path = os.path.join(args.output_folder, "dataset.jsonl")
        if os.path.exists(dataset_path):
            logger.info("🔍 Validating created dataset...")
            load_and_validate_dataset(dataset_path)
        else:
            logger.warning("Dataset file not found for validation")
