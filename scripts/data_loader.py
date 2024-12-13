import os
import pandas as pd

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}.")
    return pd.read_csv(file_path)
