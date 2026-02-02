def validate_claims(df):
    results = {}

    # Claim: "Recent years have more open cases"
    if "Year" in df.columns and "Is_Open" in df.columns:
        yearly_open = df.groupby("Year")["Is_Open"].mean().dropna()
        if len(yearly_open) >= 2:
            trend = yearly_open.iloc[-1] - yearly_open.iloc[0]
            results["Recent years have more open cases"] = "Supported" if trend > 0 else "Not clearly supported"
        else:
            results["Recent years have more open cases"] = "Insufficient data"

    # Claim: "Some violation types take longer to resolve"
    if "Violation_Clean" in df.columns and "Resolution_Days" in df.columns:
        by_type = df.groupby("Violation_Clean")["Resolution_Days"].median().dropna()
        results["Some violation types take longer to resolve"] = "Supported" if by_type.nunique() > 1 else "Not clearly supported"

    # Claim: "Neighborhood variation exists"
    if "Neighborhood_Clean" in df.columns:
        counts = df["Neighborhood_Clean"].value_counts(dropna=True)
        results["Neighborhood variation exists"] = "Supported" if counts.nunique() > 1 else "Not clearly supported"

    return results

