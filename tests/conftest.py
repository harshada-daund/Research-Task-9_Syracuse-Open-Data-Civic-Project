import pandas as pd
import pytest

@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "complaint_address": ["A", "B", "C"],
            "violation": ["Type 1", "Type 2", "Type 1"],
            "violation_date": ["2024-01-01", "2024-02-01", "2024-02-15"],
            "status_date": ["2024-01-10", "2024-02-20", "2024-02-10"],
            "status_type_name": ["Closed", "Closed", "Open"],
            "Neighborhood": ["Northside", "Southside", "Northside"],
            "Vacant": ["Y", "N", None],
            "Latitude": [43.0, 43.1, 43.2],
            "Longitude": [-76.1, -76.2, -76.3],
        }
    )
