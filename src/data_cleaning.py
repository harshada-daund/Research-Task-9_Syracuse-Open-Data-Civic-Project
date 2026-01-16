import pandas as pd

def clean_data(df):
    df = df.copy()

    for col in ["open_date", "violation_date", "status_date"]:
        df[col + "_dt"] = pd.to_datetime(df[col], errors="coerce")

    df["Year"] = df["open_date_dt"].dt.year
    df["Is_Open"] = df["status_type_name"].str.lower() != "closed"

    df["Violation_Clean"] = df["violation"].astype(str).str.lower().str.strip()
    df["Neighborhood_Clean"] = df["Neighborhood"].astype(str).str.strip().str.title()

    df["Resolution_Days"] = (df["status_date_dt"] - df["open_date_dt"]).dt.days

    return df
