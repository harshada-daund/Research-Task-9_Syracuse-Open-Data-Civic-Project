from __future__ import annotations

import pandas as pd

DATE_COLUMNS = ["open_date", "violation_date", "comply_by_date", "status_date"]


def clean_code_violations(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]

    for col in DATE_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    if "Neighborhood" in df.columns:
        df["Neighborhood"] = (
            df["Neighborhood"]
            .astype("string")
            .str.strip()
            .replace({"<NA>": pd.NA, "": pd.NA})
        )

    if "status_type_name" in df.columns:
        df["status_type_name"] = df["status_type_name"].astype("string").str.strip()

    if "Vacant" in df.columns:
        df["Vacant"] = (
            df["Vacant"]
            .astype("string")
            .str.strip()
            .str.lower()
            .replace({"y": "yes", "n": "no", "true": "yes", "false": "no"})
        )

    if "violation_date" in df.columns:
        df["year"] = df["violation_date"].dt.year

    if "status_type_name" in df.columns:
        df["is_closed"] = df["status_type_name"].str.lower().eq("closed")
    else:
        df["is_closed"] = False

    if {"violation_date", "status_date"}.issubset(df.columns):
        resolution = (df["status_date"] - df["violation_date"]).dt.days
        resolution = resolution.where(resolution >= 0)
        df["resolution_days"] = resolution
    else:
        df["resolution_days"] = pd.NA

    return df
