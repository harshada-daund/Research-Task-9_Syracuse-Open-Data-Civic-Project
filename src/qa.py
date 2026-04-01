from __future__ import annotations

import pandas as pd


def qa_report(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    rows.append({"check": "row_count", "value": int(len(df))})
    rows.append({"check": "column_count", "value": int(df.shape[1])})
    rows.append({"check": "missing_violation_date", "value": int(df["violation_date"].isna().sum()) if "violation_date" in df.columns else None})
    rows.append({"check": "missing_neighborhood", "value": int(df["Neighborhood"].isna().sum()) if "Neighborhood" in df.columns else None})
    rows.append({"check": "missing_coordinates", "value": int(df[["Latitude", "Longitude"]].isna().any(axis=1).sum()) if {"Latitude", "Longitude"}.issubset(df.columns) else None})
    rows.append({"check": "negative_resolution_days", "value": int((df["resolution_days"].dropna() < 0).sum()) if "resolution_days" in df.columns else None})
    return pd.DataFrame(rows)
