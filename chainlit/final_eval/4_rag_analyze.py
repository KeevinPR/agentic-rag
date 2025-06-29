import json
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.container import BarContainer
import seaborn as sns
from typing import Dict, List, Any, Optional
from scipy import stats


class RAGEvaluationAnalyzer:
    def __init__(self, results_file: str, questions_file: str):
        """
        Initialize the analyzer with results and questions files

        Args:
            results_file: Path to final-results.json
            questions_file: Path to 50_questions.json
        """
        self.results_file = results_file
        self.questions_file = questions_file
        self.combined_data = None
        self.analysis_report = {}

    def _calculate_stats(self, data: pd.Series) -> Dict[str, Any]:
        """Calculates mean, std, and 95% CI for a series."""
        n = len(data.dropna())
        if n < 2:  # Need at least 2 points for confidence interval
            mean = data.mean() if n == 1 else np.nan
            return {"mean": mean, "ci_lower": mean, "ci_upper": mean, "n": n}

        mean = data.mean()
        sem = data.sem()
        ci = stats.t.interval(0.95, df=n - 1, loc=mean, scale=sem)
        return {"mean": mean, "ci_lower": ci[0], "ci_upper": ci[1], "n": n}

    def load_data(self) -> pd.DataFrame:
        """Load and combine the evaluation results with questions"""
        # Load results
        with open(self.results_file, "r") as f:
            results_data = json.load(f)

        # Load questions
        with open(self.questions_file, "r") as f:
            questions_data = json.load(f)

        # Extract scores and questions
        scores = results_data["scores"]
        questions = questions_data["questions"]
        print(questions)

        # Ensure we have matching lengths
        min_length = min(len(scores), len(questions))
        scores = scores[:min_length]
        questions = questions[:min_length]

        # Combine data
        combined_records = []
        for i, (score, question) in enumerate(zip(scores, questions), start=1):
            record = {
                "question_id": i,
                "question": question.get("question", ""),
                "ground_truth": question.get("ground_truth", ""),
                "final_answer": question.get("final_answer", ""),
                "error": question.get("error", False),
                "timestamp": question.get("timestamp", ""),
                # Metrics
                "context_precision": score.get("context_precision"),
                "context_recall": score.get("context_recall"),
                "faithfulness": score.get("faithfulness"),
                "answer_relevancy": score.get("answer_relevancy"),
                # Context information
                "hybrid_search_contexts": len(
                    question.get("contexts", {}).get("hybrid_search", [])
                ),
                "paper_database_contexts": len(
                    question.get("contexts", {}).get("paper_database", [])
                ),
                "web_search_contexts": len(
                    question.get("contexts", {}).get("web_search", [])
                ),
                "total_contexts": len(
                    question.get("contexts", {}).get("hybrid_search", [])
                )
                + len(question.get("contexts", {}).get("paper_database", []))
                + len(question.get("contexts", {}).get("web_search", [])),
                # Tool usage
                "tool_calls": len(question.get("tool_calls", [])),
                "tools_used": [
                    tool.get("name", "") for tool in question.get("tool_calls", [])
                ],
                # Chunks information
                "chunks_count": len(question.get("chunks", [])),
            }
            combined_records.append(record)

        self.combined_data = pd.DataFrame(combined_records)
        return self.combined_data

    def analyze_metrics(self) -> Dict[str, Any]:
        """Perform comprehensive analysis of the metrics"""
        if self.combined_data is None:
            self.load_data()

        df = self.combined_data
        if df is None:
            return {
                "basic_stats": {},
                "problematic_questions": {},
                "context_analysis": {},
                "total_questions": 0,
            }

        # Basic statistics
        metrics = [
            "context_precision",
            "context_recall",
            "faithfulness",
            "answer_relevancy",
        ]
        stats = {}

        for metric in metrics:
            valid_values = df[metric].dropna()
            stats[metric] = {
                "mean": valid_values.mean(),
                "median": valid_values.median(),
                "std": valid_values.std(),
                "min": valid_values.min(),
                "max": valid_values.max(),
                "nan_count": df[metric].isna().sum(),
                "zero_count": (valid_values == 0).sum(),
                "valid_count": len(valid_values),
            }

        # Identify problematic questions
        problematic_questions = {
            "zero_context_precision": df[df["context_precision"] == 0.0][
                "question_id"
            ].tolist(),
            "zero_context_recall": df[df["context_recall"] == 0.0][
                "question_id"
            ].tolist(),
            "zero_faithfulness": df[df["faithfulness"] == 0.0]["question_id"].tolist(),
            "zero_answer_relevancy": df[df["answer_relevancy"] == 0.0][
                "question_id"
            ].tolist(),
            "all_nan_metrics": df[(df[metrics].isna().all(axis=1))][
                "question_id"
            ].tolist(),
            "errors": df[df["error"] == True]["question_id"].tolist(),
        }

        # Context analysis
        context_analysis = {
            "avg_total_contexts": df["total_contexts"].mean(),
            "contexts_distribution": df["total_contexts"].value_counts().to_dict(),
            "no_contexts": df[df["total_contexts"] == 0]["question_id"].tolist(),
            "context_sources": {
                "hybrid_search_avg": df["hybrid_search_contexts"].mean(),
                "paper_database_avg": df["paper_database_contexts"].mean(),
                "web_search_avg": df["web_search_contexts"].mean(),
            },
        }

        self.analysis_report = {
            "basic_stats": stats,
            "problematic_questions": problematic_questions,
            "context_analysis": context_analysis,
            "total_questions": len(df),
        }

        return self.analysis_report

    def get_low_precision_analysis(self) -> pd.DataFrame:
        """Analyze questions with low context precision"""
        if self.combined_data is None:
            self.load_data()

        df = self.combined_data
        if df is None:
            return pd.DataFrame()

        low_precision = df[
            (df["context_precision"] <= 0.5) | (df["context_precision"].isna())
        ].copy()

        return low_precision[
            [
                "question_id",
                "question",
                "context_precision",
                "total_contexts",
                "tools_used",
                "error",
            ]
        ]

    def export_detailed_report(
        self,
        output_file: str = "ragas_dataset_gemini-2.0-flash-001-v1-augmented-e5-v1-100/rag_analysis_report.json",
    ):
        """Export detailed analysis report"""
        if not self.analysis_report:
            self.analyze_metrics()

        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Add detailed question analysis
        detailed_report = self.analysis_report.copy()

        # Add specific question details for problematic cases
        if self.combined_data is not None:
            df = self.combined_data

            detailed_report["detailed_analysis"] = {}

            # Zero precision questions details
            zero_precision_ids = detailed_report["problematic_questions"][
                "zero_context_precision"
            ]
            detailed_report["detailed_analysis"]["zero_precision_questions"] = []

            for qid in zero_precision_ids:
                question_data = df[df["question_id"] == qid].iloc[0]
                detailed_report["detailed_analysis"]["zero_precision_questions"].append(
                    {
                        "question_id": qid,
                        "question": question_data["question"],
                        "total_contexts": question_data["total_contexts"],
                        "tools_used": question_data["tools_used"],
                        "error": question_data["error"],
                        "all_metrics": {
                            "context_precision": question_data["context_precision"],
                            "context_recall": question_data["context_recall"],
                            "faithfulness": question_data["faithfulness"],
                            "answer_relevancy": question_data["answer_relevancy"],
                        },
                    }
                )

        with open(output_path, "w") as f:
            json.dump(detailed_report, f, indent=2, default=str)

        print(f"Detailed report exported to {output_path}")
        return detailed_report

    def generate_recommendations(self) -> List[str]:
        """Generate specific recommendations for improvement"""
        if not self.analysis_report:
            self.analyze_metrics()

        recommendations = []
        stats = self.analysis_report["basic_stats"]

        # Context Precision recommendations
        cp_mean = stats["context_precision"]["mean"]
        cp_zeros = stats["context_precision"]["zero_count"]

        if cp_mean < 0.7:
            recommendations.append(
                f"🔧 LOW CONTEXT PRECISION (avg: {cp_mean:.3f}): "
                f"Reduce temperature from 0.7 to 0.3-0.5 for more focused retrieval. "
                f"Consider improving your retrieval ranking algorithm."
            )

        if cp_zeros > 0:
            recommendations.append(
                f"⚠️  {cp_zeros} questions have 0.0 context precision. "
                f"These likely have irrelevant retrieved contexts. "
                f"Review retrieval strategy and consider adding re-ranking."
            )

        # Context Recall recommendations
        cr_mean = stats["context_recall"]["mean"]
        if cr_mean < 0.8:
            recommendations.append(
                f"📚 LOW CONTEXT RECALL (avg: {cr_mean:.3f}): "
                f"Increase the number of retrieved documents or improve retrieval coverage. "
                f"Consider hybrid search approaches."
            )

        # Faithfulness recommendations
        faith_mean = stats["faithfulness"]["mean"]
        faith_nans = stats["faithfulness"]["nan_count"]

        if faith_mean < 0.7:
            recommendations.append(
                f"🎯 LOW FAITHFULNESS (avg: {faith_mean:.3f}): "
                f"Reduce temperature and add explicit instructions to stick to provided context. "
                f"Consider adding fact-checking prompts."
            )

        if faith_nans > 10:
            recommendations.append(
                f"❓ {faith_nans} questions have NaN faithfulness scores. "
                f"This suggests evaluation issues - check if ground truth comparisons are working."
            )

        # Answer Relevancy recommendations
        ar_mean = stats["answer_relevancy"]["mean"]
        ar_zeros = stats["answer_relevancy"]["zero_count"]

        if ar_zeros > 0:
            recommendations.append(
                f"💬 {ar_zeros} questions have 0.0 answer relevancy. "
                f"These answers are likely off-topic. Review question understanding and response generation."
            )

        # Context-specific recommendations
        context_analysis = self.analysis_report["context_analysis"]
        no_contexts = len(context_analysis["no_contexts"])

        if no_contexts > 0:
            recommendations.append(
                f"🔍 {no_contexts} questions retrieved no contexts. "
                f"Check retrieval system and embedding quality."
            )

        # General recommendations
        recommendations.extend(
            [
                "\n📋 GENERAL RECOMMENDATIONS:",
                "1. Temperature: Reduce from 0.7 to 0.3-0.4 for better precision",
                "2. Retrieval: Implement hybrid search (semantic + keyword)",
                "3. Re-ranking: Add a re-ranking step to improve context precision",
                "4. Evaluation: Fix NaN issues in faithfulness scoring",
                "5. Prompting: Add explicit instructions to stay faithful to context",
                "6. Context Quality: Filter out irrelevant contexts before generation",
            ]
        )

        return recommendations

    def create_visualizations(self, save_plots: bool = True):
        """Create academic-style visualizations for the analysis."""
        if self.combined_data is None:
            self.load_data()

        df = self.combined_data
        if df is None or df.empty:
            print("No data available to create visualizations.")
            return

        # --- Setup Academic Plotting Style ---
        plt.rcParams["font.family"] = "Times New Roman"
        sns.set_theme(style="whitegrid")
        output_dir = Path(self.results_file).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # --- Figure 1: Distribution of RAG Evaluation Metrics ---
        distribution_metrics = [
            "context_precision",
            "context_recall",
            "faithfulness",
            "answer_relevancy",
        ]
        fig1, axes = plt.subplots(2, 2, figsize=(12, 11))
        fig1.suptitle(
            "Figure 1: Distribution of RAG Evaluation Metrics",
            fontsize=18,
            fontweight="bold",
        )
        palette = sns.color_palette("Blues_d", n_colors=1)

        for i, metric in enumerate(distribution_metrics):
            row, col = i // 2, i % 2
            ax = axes[row, col]
            valid_data = df[metric].dropna()

            if not valid_data.empty:
                sns.histplot(
                    x=valid_data,
                    bins=np.arange(0, 1.05, 0.05),  # Consistent bin widths
                    kde=False,  # Remove kernel density estimate
                    ax=ax,
                    color=palette[0],
                    edgecolor="navy",
                )
                mean_val = valid_data.mean()

                ax.axvline(
                    mean_val,
                    color="red",
                    linestyle="--",
                    linewidth=2,
                    label=f"Mean: {mean_val:.3f}",
                )
                ax.legend(loc="upper right")

            ax.set_xlabel(metric.replace("_", " ").title(), fontsize=12)
            ax.set_ylabel("Frequency", fontsize=12)
            ax.set_ylim(0, 100)  # Standardize Y-axis
            ax.set_title(
                f"{metric.replace('_', ' ').title()} Distribution",
                fontsize=14,
                fontweight="bold",
            )
            ax.grid(True, which="both", linestyle="--", linewidth=0.5)

        # All 4 subplots are now used, no need to hide any

        sample_size = len(df)

        caption1_text = (
            f"Figure 1. Distribution of RAGAS evaluation scores across a sample of n={sample_size} questions.\n"
            "Each subplot shows the frequency distribution for a core metric, with the mean indicated by a dashed red line.\n"
            "These distributions help in identifying the overall performance and consistency of the RAG system."
        )
        fig1.text(0.5, 0.02, caption1_text, ha="center", fontsize=10, wrap=True)

        plt.tight_layout(rect=(0, 0.08, 1, 0.96))

        if save_plots:
            fig1_path = output_dir / "figure_1_rag_metrics_distribution_new.png"
            plt.savefig(fig1_path, dpi=300, bbox_inches="tight")
            print(f"📊 Figure 1 saved to '{fig1_path}'")
        plt.show()

        # --- Figure 2: Analysis of Problematic Questions ---
        if not self.analysis_report:
            self.analyze_metrics()

        problem_counts = {
            "Zero Context Recall": len(
                self.analysis_report["problematic_questions"].get(
                    "zero_context_recall", []
                )
            ),
            "Zero Context Precision": len(
                self.analysis_report["problematic_questions"].get(
                    "zero_context_precision", []
                )
            ),
            "Zero Faithfulness": len(
                self.analysis_report["problematic_questions"].get(
                    "zero_faithfulness", []
                )
            ),
            "No Contexts Retrieved": len(
                self.analysis_report["context_analysis"].get("no_contexts", [])
            ),
            "Agent Errors": len(
                self.analysis_report["problematic_questions"].get("errors", [])
            ),
        }

        problem_counts = {k: v for k, v in problem_counts.items() if v > 0}

        if problem_counts:
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            problem_df = pd.DataFrame(
                list(problem_counts.items()), columns=["Issue", "Count"]
            ).sort_values("Count", ascending=True)

            sns.barplot(
                x="Count",
                y="Issue",
                data=problem_df,
                ax=ax2,
                palette="Reds_d",
                edgecolor="darkred",
            )

            ax2.set_title(
                "Figure 2: Count of Key Failure Modes",
                fontsize=16,
                fontweight="bold",
                pad=20,
            )
            ax2.set_xlabel("Number of Questions", fontsize=12)
            ax2.set_ylabel("Failure Category", fontsize=12)
            for container in ax2.containers:
                if isinstance(container, BarContainer):
                    ax2.bar_label(container, fmt="%d", padding=3)

            caption2 = (
                f"Figure 2. Summary of key failure modes identified across the n={len(df)} sample questions.\n"
                "This chart highlights the most frequent issues, providing a clear guide for targeted improvements."
            )
            fig2.text(0.5, -0.15, caption2, ha="center", fontsize=10, wrap=True)
            plt.tight_layout()

            if save_plots:
                fig2_path = output_dir / "figure_2_failure_mode_analysis_new.png"
                plt.savefig(fig2_path, dpi=300, bbox_inches="tight")
                print(f"📊 Figure 2 saved to '{fig2_path}'")
            plt.show()
        else:
            print("✅ No problematic questions found to generate Figure 2.")


def main():
    """Main execution function"""
    # Initialize analyzer
    analyzer = RAGEvaluationAnalyzer(
        results_file="ragas_dataset_gemini-2.0-flash-001-v1-augmented-e5-v1-100/new_results.json",
        questions_file="ragas_dataset_gemini-2.0-flash-001-v1-augmented-e5-v1-100/all_question_files_content_ordered.json",
    )

    # Load and analyze data
    print("Loading and analyzing data...")
    combined_df = analyzer.load_data()
    analysis_report = analyzer.analyze_metrics()

    # Display basic statistics
    print("\n" + "=" * 60)
    print("RAG EVALUATION ANALYSIS REPORT")
    print("=" * 60)

    print(f"\nTotal Questions Analyzed: {analysis_report['total_questions']}")

    print("\n📊 METRIC STATISTICS:")
    for metric, stats in analysis_report["basic_stats"].items():
        print(f"\n{metric.upper().replace('_', ' ')}:")
        print(f"  Mean: {stats['mean']:.3f}")
        print(f"  Std:  {stats['std']:.3f}")
        print(
            f"  NaN:  {stats['nan_count']} ({stats['nan_count'] / analysis_report['total_questions'] * 100:.1f}%)"
        )
        print(f"  Zero: {stats['zero_count']}")

    # Show problematic questions
    print("\n🚨 PROBLEMATIC QUESTIONS:")
    for issue, question_ids in analysis_report["problematic_questions"].items():
        if question_ids:
            print(
                f"  {issue.replace('_', ' ').title()}: {len(question_ids)} questions {question_ids}"
            )

    # Generate and display recommendations
    print("\n" + "=" * 60)
    print("RECOMMENDATIONS FOR IMPROVEMENT")
    print("=" * 60)
    recommendations = analyzer.generate_recommendations()
    for rec in recommendations:
        print(rec)

    # Export detailed report
    analyzer.export_detailed_report()

    # Create visualizations
    print("\nGenerating visualizations...")
    analyzer.create_visualizations()

    # Export combined data to CSV for further analysis
    combined_df.to_csv("combined_rag_analysis.csv", index=False)
    print("\nCombined data exported to 'combined_rag_analysis.csv'")

    # Show low precision questions in detail
    print("\n" + "=" * 60)
    print("LOW CONTEXT PRECISION QUESTIONS (≤0.5 or NaN)")
    print("=" * 60)
    low_precision_df = analyzer.get_low_precision_analysis()
    for _, row in low_precision_df.iterrows():
        print(f"\nQuestion {row['question_id']}: {row['question'][:100]}...")
        print(f"  Context Precision: {row['context_precision']}")
        print(f"  Total Contexts: {row['total_contexts']}")
        print(f"  Tools Used: {row['tools_used']}")
        print(f"  Error: {row['error']}")


if __name__ == "__main__":
    main()
