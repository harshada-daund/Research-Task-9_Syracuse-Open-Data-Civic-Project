import pandas as pd

def load_raw_data(path):
    """Load raw Syracuse housing code violations data."""
    return pd.read_csv(path)
