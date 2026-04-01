from src.data_cleaning import clean_code_violations


def test_cleaning_adds_year_and_resolution_days(sample_df):
    cleaned = clean_code_violations(sample_df)
    assert "year" in cleaned.columns
    assert "resolution_days" in cleaned.columns
    assert cleaned.loc[0, "year"] == 2024
    assert cleaned.loc[0, "resolution_days"] == 9


def test_cleaning_normalizes_vacant(sample_df):
    cleaned = clean_code_violations(sample_df)
    assert cleaned.loc[0, "Vacant"] == "yes"
    assert cleaned.loc[1, "Vacant"] == "no"
