from __future__ import annotations

import os
import matplotlib.pyplot as plt
import pandas as pd


def _save_bar_chart(df: pd.DataFrame, x: str, y: str, title: str, path: str, rotation: int = 45) -> None:
    if df.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df[x].astype(str), df[y])
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    plt.xticks(rotation=rotation, ha="right")
    plt.tight_layout()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_standard_figures(
    year_df: pd.DataFrame,
    violation_df: pd.DataFrame,
    neighborhood_df: pd.DataFrame,
    status_df: pd.DataFrame,
    avg_resolution_df: pd.DataFrame,
    output_dir: str
) -> None:
    _save_bar_chart(
        year_df, "year", "violations", "Violations by Year",
        os.path.join(output_dir, "figures", "violations_by_year.png"), rotation=0
    )
    _save_bar_chart(
        violation_df, "violation", "count", "Top Violation Types",
        os.path.join(output_dir, "figures", "top_violation_types.png")
    )
    _save_bar_chart(
        neighborhood_df, "Neighborhood", "count", "Top Neighborhoods",
        os.path.join(output_dir, "figures", "top_neighborhoods.png")
    )
    _save_bar_chart(
        status_df, "status_type_name", "count", "Open vs Closed Cases",
        os.path.join(output_dir, "figures", "open_vs_closed_cases.png"), rotation=0
    )
    _save_bar_chart(
        avg_resolution_df, "Neighborhood", "resolution_days", "Average Resolution by Neighborhood",
        os.path.join(output_dir, "figures", "avg_resolution_by_neighborhood.png")
    )
