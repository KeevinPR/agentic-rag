#!/usr/bin/env python3
"""
RAG Results Comparison Analysis - Academic Standards Edition
Compares different RAG setups with statistical rigor and publication-quality output.
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Any
from scipy import stats


class RAGComparison:
    """
    Handles the loading, statistical analysis, and visualization of RAG evaluation results.
    """

    def __init__(self, baseline_name: str):
        self.datasets: Dict[str, pd.DataFrame] = {}
        self.comparison_results: Dict[str, Any] = {}
        self.baseline_name = baseline_name
        self.metrics = [
            "context_precision",
            "context_recall",
            "faithfulness",
            "answer_relevancy",
        ]
        # Set professional typography for all plots
        plt.rcParams["font.family"] = "Times New Roman"

    def load_datasets(self, file_paths: Dict[str, str]):
        """Load multiple dataset files and ensures they have the same number of records."""
        base_len = -1
        for name, path in file_paths.items():
            try:
                with open(path, "r") as f:
                    data = json.load(f)["scores"]
                    self.datasets[name] = pd.DataFrame(data)
                    print(f"✅ Loaded {name}: {len(data)} records")
                    if base_len == -1:
                        base_len = len(data)
                    elif len(data) != base_len:
                        print(
                            f"❌ Error: Datasets must have the same number of records for paired tests."
                        )
                        self.datasets = {}
                        return
            except Exception as e:
                print(f"❌ Error loading {name}: {e}")
                self.datasets = {}
                return

    def _calculate_stats(self, data: pd.Series) -> Dict[str, float]:
        """Calculates mean, std, and 95% CI for a series."""
        n = len(data.dropna())
        if n == 0:
            return {"mean": np.nan, "ci_lower": np.nan, "ci_upper": np.nan, "n": 0}

        mean = data.mean()
        sem = data.sem()
        ci = stats.t.interval(0.95, df=n - 1, loc=mean, scale=sem)
        return {"mean": mean, "ci_lower": ci[0], "ci_upper": ci[1], "n": n}

    def _calculate_pairwise_stats(
        self, series1: pd.Series, series2: pd.Series
    ) -> Dict[str, float]:
        """Performs paired t-test and calculates Cohen's d."""
        # Drop NaN values pairwise
        combined = pd.concat([series1, series2], axis=1).dropna()
        if len(combined) < 2:
            return {"p_value": np.nan, "cohen_d": np.nan}

        s1, s2 = combined.iloc[:, 0], combined.iloc[:, 1]

        # Paired t-test
        t_stat, p_value = stats.ttest_rel(s1, s2)

        # Cohen's d for paired samples
        diff = s2 - s1
        pooled_std = diff.std()
        cohen_d = diff.mean() / pooled_std if pooled_std != 0 else 0

        return {"p_value": p_value, "cohen_d": cohen_d}

    def calculate_aggregated_metrics(self):
        """Calculate aggregated metrics and pairwise stats against the baseline."""
        if not self.datasets or self.baseline_name not in self.datasets:
            print(f"❌ Baseline dataset '{self.baseline_name}' not found.")
            return

        baseline_df = self.datasets[self.baseline_name]
        results: Dict[str, Any] = {"datasets": {}}

        for metric in self.metrics:
            results[metric] = {}
            # Calculate stats for all datasets
            for name, df in self.datasets.items():
                stats_res = self._calculate_stats(df[metric])
                results[metric][name] = stats_res

                # For non-baseline datasets, calculate pairwise stats
                if name != self.baseline_name:
                    pairwise_res = self._calculate_pairwise_stats(
                        baseline_df[metric], df[metric]
                    )
                    results[metric][name].update(pairwise_res)

        self.comparison_results = results

    def print_supplementary_table(self):
        """Prints a detailed supplementary data table for academic papers."""
        if not self.comparison_results:
            return

        print("\n" + "=" * 100)
        print("Supplementary Data Table: RAG Performance Metrics")
        print("=" * 100)
        print(
            "Values are Mean (95% CI). Pairwise stats are vs. baseline '{}'.".format(
                self.baseline_name
            )
        )

        header = f"{'Metric':<20}"
        for name in self.datasets.keys():
            header += f" | {name:<25}"
        print(header)
        print("-" * len(header))

        for metric in self.metrics:
            row_str = f"{metric.replace('_', ' ').title():<20}"
            for name in self.datasets.keys():
                stats = self.comparison_results[metric][name]
                mean_ci = f"{stats['mean']:.3f} ({stats['ci_lower']:.3f} - {stats['ci_upper']:.3f})"

                if name != self.baseline_name:
                    p_val = stats.get("p_value")
                    cohen_d = stats.get("cohen_d")
                    stats_str = (
                        f"p={p_val:.3f}, d={cohen_d:.2f}" if p_val is not None else ""
                    )
                    row_str += f" | {mean_ci:<15} {stats_str:<10}"
                else:
                    row_str += f" | {mean_ci:<25}"
            print(row_str)
        print("-" * 100)

    def create_visualization(self, save_plots: bool = True):
        """Creates a single, publication-quality bar chart with error bars and a detailed caption."""
        if not self.comparison_results:
            return

        sns.set_theme(style="whitegrid")
        plot_data = []
        for metric in self.metrics:
            for name, stats in self.comparison_results[metric].items():
                plot_data.append(
                    {
                        "Version": name,
                        "Metric": metric.replace("_", " ").title(),
                        "Average Score": stats["mean"],
                        "Error": stats["ci_upper"]
                        - stats["mean"],  # Symmetric error for plotting
                    }
                )

        df_plot = pd.DataFrame(plot_data)

        # Create the plot
        plt.figure(figsize=(10, 6))
        # Use academic blue palette instead of grayscale
        palette = sns.color_palette("Blues_r", n_colors=len(self.datasets))

        # Explicitly define the order to prevent seaborn from creating extra bars
        metric_order = [m.replace("_", " ").title() for m in self.metrics]
        hue_order = list(self.datasets.keys())

        ax = sns.barplot(
            data=df_plot,
            x="Metric",
            y="Average Score",
            hue="Version",
            palette=palette,
            edgecolor="navy",  # Darker blue edge color for better contrast
            order=metric_order,
            hue_order=hue_order,
        )

        # Add error bars using a systematic approach
        # Create a lookup dictionary for error values
        error_lookup = {}
        for _, row in df_plot.iterrows():
            key = (row["Metric"], row["Version"])
            error_lookup[key] = row["Error"]

        # Get error values in the order that matches the bars
        errors = []
        x_coords = []
        y_coords = []

        for patch in ax.patches:  # type: ignore
            x_coord = patch.get_x() + 0.5 * patch.get_width()  # type: ignore
            y_coord = patch.get_height()  # type: ignore

            # Skip bars with zero height (these might be placeholder bars)
            if y_coord > 0:
                x_coords.append(x_coord)
                y_coords.append(y_coord)

                # Find the corresponding error value
                # This is tricky, so we'll match by finding the closest data point
                best_match_error = 0.0
                min_distance = float("inf")

                for (metric, version), error_val in error_lookup.items():
                    expected_y = df_plot[
                        (df_plot["Metric"] == metric) & (df_plot["Version"] == version)
                    ]["Average Score"].iloc[0]
                    distance = abs(expected_y - y_coord)
                    if distance < min_distance:
                        min_distance = distance
                        best_match_error = error_val

                errors.append(best_match_error)

        # Plot error bars
        if len(errors) == len(x_coords) == len(y_coords):
            ax.errorbar(
                x=x_coords,
                y=y_coords,
                yerr=errors,  # type: ignore
                fmt="none",
                c="darkblue",  # Dark blue to complement the palette
                capsize=3,  # type: ignore
            )

        ax.set_title(
            "Figure 1: RAG Performance Metrics Comparison", fontsize=16, pad=20
        )
        ax.set_xlabel("Metric", fontsize=12)
        ax.set_ylabel("Average Score", fontsize=12)
        ax.tick_params(axis="x", rotation=45)
        ax.legend(title="Version")
        plt.ylim(0, 1.1)

        # Create detailed caption
        sample_size = self.comparison_results[self.metrics[0]][self.baseline_name]["n"]
        caption = (
            f"Figure 1. Comparison of RAG performance across {len(self.datasets)} versions based on a sample of n={sample_size} queries.\\n"
            "Metrics are defined as: Context Precision (relevance of retrieved context), Context Recall (ability to retrieve all relevant context),\\n"
            "Faithfulness (factual consistency of the answer), and Answer Relevancy (relevance of the answer to the query).\\n"
            f"Error bars represent the 95% confidence interval. A paired t-test was used to assess statistical significance between versions."
        )

        plt.figtext(0.5, -0.3, caption, ha="center", fontsize=10, wrap=True)
        plt.tight_layout(rect=(0, 0, 1, 1))

        if save_plots:
            filename = "figure_1_rag_comparison.png"
            plt.savefig(filename, dpi=300, bbox_inches="tight")
            print(f"\n📊 Publication-quality visualization saved as '{filename}'")
        plt.show()


def main():
    """Main execution function."""
    print("RAG Results Comparison Analysis (Academic Edition)")
    print("=" * 60)

    # Define file paths and the baseline for comparison
    baseline_version = "Augmented (Simple hybrid search)"
    file_paths = {
        "Augmented (Simple hybrid search)": "/Users/id05309/Documents/tfm/chainlit/final_eval/ragas_dataset_final-v1-100/new_results.json",
        "Augmented (Enhanced hybrid search)": "/Users/id05309/Documents/tfm/chainlit/final_eval/ragas_dataset_final-v2-100/new_results.json",
    }

    comparator = RAGComparison(baseline_name=baseline_version)
    comparator.load_datasets(file_paths)

    if not comparator.datasets:
        return

    # Perform analysis
    comparator.calculate_aggregated_metrics()

    # Display results
    comparator.print_supplementary_table()

    # Create visualization
    comparator.create_visualization()

    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
