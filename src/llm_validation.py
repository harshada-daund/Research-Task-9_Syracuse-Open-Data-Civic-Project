from __future__ import annotations

import pandas as pd


def validate_claim_contains_top_neighborhood(claim: str, top_neighborhoods_df: pd.DataFrame) -> dict:
    if top_neighborhoods_df.empty:
        return {"valid": False, "reason": "No neighborhood summary available."}

    top_name = str(top_neighborhoods_df.iloc[0]["Neighborhood"])
    valid = top_name.lower() in claim.lower()
    return {
        "valid": valid,
        "expected_top_neighborhood": top_name,
        "reason": "Claim mentions computed top neighborhood." if valid else "Claim does not mention computed top neighborhood.",
    }
