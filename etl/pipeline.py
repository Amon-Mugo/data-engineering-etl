from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    print(" Starting ETL pipeline...")
    df = extract_data("data/sample.csv")
    df = transform_data(df)
    load_data(df, "employees")
    print(" Pipeline finished successfully")

if __name__ == "__main__":
    run_pipeline()
