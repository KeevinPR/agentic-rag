# evaluate_ragas_dataset.py

import os
import json
import argparse
import logging
from typing import List, Dict, Any, Optional
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from ragas.dataset_schema import EvaluationResult
import pandas as pd
import asyncio
from langchain_ollama import ChatOllama
from ragas import evaluate
from ragas.metrics import (
    context_precision,
    context_recall,
    faithfulness,
    answer_relevancy,
    # AnswerCorrectness,
)
from ragas.dataset_schema import EvaluationDataset, SingleTurnSample
from ragas.run_config import RunConfig
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_core.callbacks import BaseCallbackHandler


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set")


class DelayCallbackHandler(BaseCallbackHandler):
    """Callback handler to introduce delays between requests."""

    def __init__(self, delay_seconds: float = 2.0):
        self.delay_seconds = delay_seconds

    async def on_llm_start(self, *args, **kwargs):
        """Add delay before each LLM request."""
        logger.info(f"Waiting {self.delay_seconds} seconds before next request...")
        await asyncio.sleep(self.delay_seconds)


class RagasConverter:
    """Converter class to create Ragas samples from various data formats."""

    @staticmethod
    def create_single_turn_sample(
        query: str,
        agent_response: str,
        reference_contexts: Optional[List[str]] = None,
        hybrid_search_contexts: Optional[List[str]] = None,
        paper_database_contexts: Optional[List[str]] = None,
        web_search_contexts: Optional[List[str]] = None,
        ground_truth: Optional[str] = None,
        rubrics: Optional[str] = None,
    ) -> SingleTurnSample:
        """
        Create a SingleTurnSample from individual components.

        Args:
            query: The user's question/input
            agent_response: The final response from the agent
            reference_contexts: Reference contexts
            hybrid_search_contexts: Contexts from hybrid search
            paper_database_contexts: Contexts from paper database
            web_search_contexts: Contexts from web search
            ground_truth: Reference answer (optional)
            rubrics: Evaluation rubrics (optional, not used in SingleTurnSample)

        Returns:
            SingleTurnSample object
        """
        # Combine all contexts
        all_contexts = []

        if hybrid_search_contexts:
            all_contexts.extend([str(ctx) for ctx in hybrid_search_contexts if ctx])

        if paper_database_contexts:
            all_contexts.extend([str(ctx) for ctx in paper_database_contexts if ctx])

        if web_search_contexts:
            all_contexts.extend([str(ctx) for ctx in web_search_contexts if ctx])

        return SingleTurnSample(
            user_input=query,
            response=agent_response,
            reference_contexts=reference_contexts,
            retrieved_contexts=all_contexts,
            reference=ground_truth,
        )


class RagasEvaluator:
    """Main evaluator class for Ragas evaluation with NVIDIA models."""

    def __init__(self, nvidia_api_key: Optional[str] = None):
        """
        Initialize the evaluator with NVIDIA models.

        Args:
            nvidia_api_key: NVIDIA API key (if not provided, will use env var)
        """
        self.nvidia_api_key = nvidia_api_key or os.getenv("NVIDIA_API_KEY")
        if not self.nvidia_api_key:
            raise ValueError(
                "NVIDIA_API_KEY must be provided or set as environment variable"
            )

        # Initialize NVIDIA LLM
        self.nvidia_llm = ChatNVIDIA(
            model="meta/llama-3.3-70b-instruct",
            temperature=0.1,  # Lower temperature for more consistent output
            top_p=0.9,
            max_tokens=2048,
            api_key=self.nvidia_api_key,
        )

        from langchain_google_genai import ChatGoogleGenerativeAI

        self.google_llm = LangchainLLMWrapper(
            ChatGoogleGenerativeAI(
                model="gemini-2.0-flash-001",
                temperature=0.1,
                top_p=0.9,
                max_tokens=2048,
            )
        )

        self.google_embeddings = LangchainEmbeddingsWrapper(
            GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        )

        # Initialize NVIDIA Embeddings
        self.nvidia_embeddings = NVIDIAEmbeddings(
            model="nvidia/nv-embedcode-7b-v1",
            api_key=self.nvidia_api_key,
            truncate="NONE",
        )

        self.openai_llm = LangchainLLMWrapper(
            ChatOpenAI(
                model="gpt-4o-mini",
                callbacks=[DelayCallbackHandler(delay_seconds=1.0)],
            )
        )
        self.openai_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())

        MODEL_NAME = (
            "llama3"  # Kept for potential local runs, but not used in default eval
        )
        llm = ChatOllama(
            model=MODEL_NAME,
            temperature=0.1,  # Lower temperature for more focused responses
            num_ctx=4096,  # Context window size
        )
        self.evaluator_llm = LangchainLLMWrapper(llm)

        # Initialize metrics with NVIDIA models
        self.metrics = [
            context_precision,
            context_recall,
            faithfulness,
            answer_relevancy,
        ]

    def load_dataset_from_jsonl(self, dataset_path: str) -> EvaluationDataset:
        """Load dataset from JSONL file."""
        try:
            dataset = EvaluationDataset.from_jsonl(dataset_path)
            logger.info(f"✅ Loaded dataset with {len(dataset.samples)} samples")
            return dataset
        except Exception as e:
            logger.error(f"Failed to load dataset from {dataset_path}: {e}")
            raise

    def load_dataset_from_json_files(self, input_folder: str) -> EvaluationDataset:
        """
        Load dataset from individual JSON files matching the schema.

        Expected JSON structure:
        {
            "question": "string",
            "ground_truth": "string",
            "final_answer": "string",
            "reference": "string",
            "contexts": {
                "hybrid_search": ["string"],
                "paper_database": [],
                "web_search": []
            },
            "tool_calls": [{"name": "string", "args": {}}],
            "error": "boolean"
        }
        """
        import glob

        pattern = os.path.join(input_folder, "*.json")
        files = sorted(glob.glob(pattern))

        if not files:
            raise ValueError(f"No JSON files found in {input_folder}")

        samples = []
        single_tool_samples = []
        multi_tool_samples = []

        for filepath in files:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Check number of tool calls
                tool_calls = data.get("tool_calls", [])
                num_tools = len(tool_calls)

                if num_tools > 1:
                    # Multi-tool case - skip for now as requested
                    multi_tool_samples.append(filepath)
                    logger.warning(
                        f"⚠️  Skipping multi-tool sample: {os.path.basename(filepath)} ({num_tools} tools)"
                    )
                    continue

                # Create sample using RagasConverter
                contexts_data = data.get("contexts", {})
                sample = RagasConverter.create_single_turn_sample(
                    query=data.get("question", ""),
                    agent_response=data.get("final_answer", ""),
                    reference_contexts=data.get("reference", []),
                    hybrid_search_contexts=contexts_data.get("hybrid_search", []),
                    paper_database_contexts=contexts_data.get("paper_database", []),
                    web_search_contexts=contexts_data.get("web_search", []),
                    ground_truth=data.get("ground_truth", ""),
                )

                samples.append(sample)
                single_tool_samples.append(filepath)

            except Exception as e:
                logger.error(f"Failed to process {filepath}: {e}")
                continue

        logger.info(f"✅ Processed {len(samples)} single-tool samples")
        logger.info(f"⚠️  Skipped {len(multi_tool_samples)} multi-tool samples")

        if not samples:
            raise ValueError("No valid samples found")

        return EvaluationDataset(samples=samples)

    def evaluate_dataset(self, dataset: EvaluationDataset) -> EvaluationResult:
        """
        Evaluate the dataset using Ragas metrics.

        Args:
            dataset: EvaluationDataset to evaluate

        Returns:
            Dictionary containing evaluation results
        """
        logger.info(f"🚀 Starting evaluation of {len(dataset.samples)} samples...")
        logger.info(
            "📊 Metrics: context_precision, context_recall, faithfulness, answer_relevancy"
        )

        try:
            # Configure run to limit concurrency
            run_config = RunConfig(max_workers=5)

            # Run evaluation with the fast OpenAI API model
            result = evaluate(
                dataset=dataset,
                metrics=self.metrics,
                llm=self.openai_llm,
                embeddings=self.openai_embeddings,
                run_config=run_config,
            )

            logger.info("✅ Evaluation completed successfully!")

            # Load per-question scores
            per_question_scores = result.scores  # List[Dict[str, float]]

            # Load the ordered questions file
            with open(
                "/Users/id05309/Documents/tfm/chainlit/final_eval/ragas_dataset_final-v2-100/all_question_files_content_ordered.json",
                "r",
                encoding="utf-8",
            ) as f:
                all_questions = json.load(f)["questions"]

            # Merge metrics into each question
            for q, metrics in zip(all_questions, per_question_scores):
                q["metrics"] = metrics

            # Save the updated file
            with open(
                "/Users/id05309/Documents/tfm/chainlit/final_eval/ragas_dataset_gemini-2.0-flash-001-v2-augmented-e5-v2-100/all_question_files_content_ordered_with_metrics.json",
                "w",
                encoding="utf-8",
            ) as f:
                json.dump({"questions": all_questions}, f, indent=2, ensure_ascii=False)

            return result

        except Exception as e:
            logger.error(f"❌ Evaluation failed: {e}")
            raise

    def save_results(self, result: EvaluationResult, output_path: str):
        """Save evaluation results to files."""
        os.makedirs(
            os.path.dirname(output_path) if os.path.dirname(output_path) else ".",
            exist_ok=True,
        )

        # Calculate aggregated metrics
        aggregated_metrics = {}
        if hasattr(result, "to_pandas"):
            df = result.to_pandas()
            for metric in [
                "context_precision",
                "context_recall",
                "faithfulness",
                "answer_relevancy",
                # "answer_correctness",
            ]:
                if metric in df.columns:
                    aggregated_metrics[metric] = {
                        "mean": float(df[metric].mean()),
                        "std": float(df[metric].std()),
                        "min": float(df[metric].min()),
                        "max": float(df[metric].max()),
                        "median": float(df[metric].median()),
                    }

        # Save as JSON
        json_path = (
            output_path.replace(".csv", ".json")
            if output_path.endswith(".csv")
            else f"{output_path}.json"
        )
        with open(json_path, "w", encoding="utf-8") as f:
            # Convert result to JSON-serializable format
            json_result = {
                "scores": [
                    {
                        metric: float(score)
                        if isinstance(score, (int, float))
                        else str(score)
                        for metric, score in score_dict.items()
                    }
                    for score_dict in result.scores
                ],
                "binary_columns": result.binary_columns,
                "run_id": str(result.run_id) if result.run_id else None,
                "aggregated_metrics": aggregated_metrics,
                "total_samples": len(result.scores),
            }
            json.dump(json_result, f, indent=2)

        logger.info(f"📄 Results saved to: {json_path}")

        # Save as CSV if it's a DataFrame-like result
        try:
            if hasattr(result, "to_pandas"):
                df = result.to_pandas()
                csv_path = (
                    output_path
                    if output_path.endswith(".csv")
                    else f"{output_path}.csv"
                )
                df.to_csv(csv_path, index=False)
                logger.info(f"📊 Results saved to: {csv_path}")

        except Exception as e:
            logger.warning(f"Could not save as CSV: {e}")

    def print_summary(self, result: EvaluationResult):
        """Print a summary of evaluation results."""
        logger.info("=" * 50)
        logger.info("📊 EVALUATION SUMMARY")
        logger.info("=" * 50)

        # Try to extract metric scores
        try:
            if hasattr(result, "to_pandas"):
                df = result.to_pandas()

                # Print overall statistics
                for metric in [
                    "context_precision",
                    "context_recall",
                    "faithfulness",
                    "answer_relevancy",
                    # "answer_correctness",
                ]:
                    if metric in df.columns:
                        mean_score = df[metric].mean()
                        std_score = df[metric].std()
                        logger.info(
                            f"{metric.upper()}: {mean_score:.3f} (±{std_score:.3f})"
                        )

                logger.info(f"\nTotal samples evaluated: {len(df)}")

        except Exception as e:
            logger.warning(f"Could not generate summary statistics: {e}")
            logger.info(f"Raw result keys: {list(result.scores)}")


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate Ragas dataset using NVIDIA models"
    )
    parser.add_argument(
        "--input_path",
        type=str,
        help="Path to dataset JSONL file or folder with JSON files",
        default="ragas_dataset_final-v2-100/dataset.jsonl",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="ragas_dataset_final-v2-100/new_results",
        help="Output path for results (without extension)",
    )
    parser.add_argument(
        "--nvidia_api_key",
        type=str,
        help="NVIDIA API key (if not set as environment variable)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging",
    )

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Initialize evaluator
        evaluator = RagasEvaluator(nvidia_api_key=args.nvidia_api_key)

        # Load dataset
        if os.path.isfile(args.input_path) and args.input_path.endswith(".jsonl"):
            dataset = evaluator.load_dataset_from_jsonl(args.input_path)
        elif os.path.isdir(args.input_path):
            dataset = evaluator.load_dataset_from_json_files(args.input_path)
        else:
            raise ValueError(
                "Input path must be a JSONL file or directory with JSON files"
            )

        # Run evaluation
        result = evaluator.evaluate_dataset(dataset)

        # Save and display results
        evaluator.save_results(result, args.output_path)
        evaluator.print_summary(result)

    except Exception as e:
        logger.error(f"❌ Evaluation failed: {e}")
        raise


if __name__ == "__main__":
    main()
