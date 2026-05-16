from __future__ import annotations

import argparse
import os
import pandas as pd

from .data_cleaning import clean_code_violations
from .analysis import (
    summary_metrics,
    violations_by_year,
    top_violation_types,
    top_neighborhoods,
    status_summary,
    avg_resolution_by_neighborhood,
    status_by_neighborhood,
)
from .qa import qa_report
from .visualization import save_standard_figures



def run_pipeline(input_path: str, output_dir: str, processed_dir: str) -> None:
    df = pd.read_csv(input_path, low_memory=False)
    cleaned = clean_code_violations(df)

    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "tables"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "figures"), exist_ok=True)

    cleaned.to_csv(os.path.join(processed_dir, "cleaned_code_violations.csv"), index=False)

    metrics_df = summary_metrics(cleaned)
    by_year_df = violations_by_year(cleaned)
    top_types_df = top_violation_types(cleaned)
    top_neighborhoods_df = top_neighborhoods(cleaned)
    status_df = status_summary(cleaned)
    avg_resolution_df = avg_resolution_by_neighborhood(cleaned)
    qa_df = qa_report(cleaned)
    status_neighborhood = status_by_neighborhood(cleaned)

    metrics_df.to_csv(os.path.join(output_dir, "tables", "summary_metrics.csv"), index=False)
    by_year_df.to_csv(os.path.join(output_dir, "tables", "violations_by_year.csv"), index=False)
    top_types_df.to_csv(os.path.join(output_dir, "tables", "top_violation_types.csv"), index=False)
    top_neighborhoods_df.to_csv(os.path.join(output_dir, "tables", "top_neighborhoods.csv"), index=False)
    status_df.to_csv(os.path.join(output_dir, "tables", "status_summary.csv"), index=False)
    avg_resolution_df.to_csv(os.path.join(output_dir, "tables", "avg_resolution_by_neighborhood.csv"), index=False)
    qa_df.to_csv(os.path.join(output_dir, "tables", "qa_report.csv"), index=False)
    status_neighborhood.to_csv(os.path.join(output_dir, "tables", "status_by_neighborhood.csv"), index=False)

    save_standard_figures(
        by_year_df,
        top_types_df,
        top_neighborhoods_df,
        status_df,
        avg_resolution_df,
        output_dir
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Syracuse Code Violations pipeline")
    parser.add_argument("--input", default="data/raw/Code_Violations.csv")
    parser.add_argument("--output-dir", default="outputs")
    parser.add_argument("--processed-dir", default="data/processed")
    args = parser.parse_args()

    run_pipeline(args.input, args.output_dir, args.processed_dir)


if __name__ == "__main__":
    main()
