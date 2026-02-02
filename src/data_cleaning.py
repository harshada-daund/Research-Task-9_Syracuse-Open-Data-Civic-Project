import pandas as pd

def clean_data(df):
    df = df.copy()

    date_cols = ["open_date", "violation_date", "status_date"]
    for col in date_cols:
        if col in df.columns:
            df[col + "_dt"] = pd.to_datetime(df[col], errors="coerce")

    if "open_date_dt" in df.columns:
        df["Year"] = df["open_date_dt"].dt.year

    if "status_type_name" in df.columns:
        df["Is_Open"] = df["status_type_name"].astype(str).str.lower() != "closed"

    if "violation" in df.columns:
        df["Violation_Clean"] = df["violation"].astype(str).str.lower().str.strip()

    if "Neighborhood" in df.columns:
        df["Neighborhood_Clean"] = df["Neighborhood"].astype(str).str.strip().str.title()

    # Only compute resolution if both dates exist
    if "status_date_dt" in df.columns and "open_date_dt" in df.columns:
        df["Resolution_Days"] = (df["status_date_dt"] - df["open_date_dt"]).dt.days
        df.loc[df["Resolution_Days"] < 0, "Resolution_Days"] = pd.NA

    return df

