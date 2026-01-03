def transform_data(df):
    df = df.dropna(subset=["age"])
    df["age"] = df["age"].astype(int)
    df["salary"] = df["salary"] * 1.1
    print(" Data transformed")
    return df
