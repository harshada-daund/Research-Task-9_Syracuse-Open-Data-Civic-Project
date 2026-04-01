from __future__ import annotations

import pandas as pd


def summary_metrics(df: pd.DataFrame) -> pd.DataFrame:
    metrics = {
        "rows": len(df),
        "columns": df.shape[1],
        "closed_cases": int(df["is_closed"].fillna(False).sum()) if "is_closed" in df.columns else 0,
        "open_cases": int((~df["is_closed"].fillna(False)).sum()) if "is_closed" in df.columns else 0,
        "avg_resolution_days_closed": float(df.loc[df["is_closed"] == True, "resolution_days"].dropna().mean()) if {"is_closed", "resolution_days"}.issubset(df.columns) else None,
    }
    return pd.DataFrame([metrics])


def violations_by_year(df: pd.DataFrame) -> pd.DataFrame:
    if "year" not in df.columns:
        return pd.DataFrame(columns=["year", "violations"])
    return (
        df.dropna(subset=["year"])
        .groupby("year")
        .size()
        .reset_index(name="violations")
        .sort_values("year")
    )


def top_violation_types(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    out = df["violation"].fillna("Unknown").value_counts().head(n).reset_index()
    out.columns = ["violation", "count"]
    return out


def top_neighborhoods(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    out = df["Neighborhood"].fillna("Unknown").value_counts().head(n).reset_index()
    out.columns = ["Neighborhood", "count"]
    return out


def status_summary(df: pd.DataFrame) -> pd.DataFrame:
    out = df["status_type_name"].fillna("Unknown").value_counts().reset_index()
    out.columns = ["status_type_name", "count"]
    return out


def avg_resolution_by_neighborhood(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    if not {"Neighborhood", "is_closed", "resolution_days"}.issubset(df.columns):
        return pd.DataFrame(columns=["Neighborhood", "resolution_days"])

    closed = df[(df["is_closed"] == True) & (df["resolution_days"].notna())].copy()
    out = (
        closed.groupby("Neighborhood", as_index=False)["resolution_days"]
        .mean()
        .sort_values("resolution_days", ascending=False)
        .head(n)
    )
    return out
