from src.data_cleaning import clean_code_violations
from src.analysis import violations_by_year, top_neighborhoods, avg_resolution_by_neighborhood


def test_violations_by_year_returns_counts(sample_df):
    cleaned = clean_code_violations(sample_df)
    out = violations_by_year(cleaned)
    assert out["violations"].sum() == 3


def test_top_neighborhoods_returns_expected_top(sample_df):
    cleaned = clean_code_violations(sample_df)
    out = top_neighborhoods(cleaned, n=1)
    assert out.iloc[0]["Neighborhood"] == "Northside"
    assert out.iloc[0]["count"] == 2


def test_avg_resolution_by_neighborhood(sample_df):
    cleaned = clean_code_violations(sample_df)
    out = avg_resolution_by_neighborhood(cleaned, n=5)
    assert "Neighborhood" in out.columns
    assert "resolution_days" in out.columns
    assert not out.empty
