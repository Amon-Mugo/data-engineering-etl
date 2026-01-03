import pandas as pd

def extract_data(path):
    df = pd.read_csv(path)
    print("Data extracted")
    return df
