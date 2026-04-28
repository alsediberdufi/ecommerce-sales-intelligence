from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent

def load_to_postgres():
    dataset_path = BASE_DIR / "data" / "cleaned" / "final_dataset.csv"

    # 🔴 CHANGE ONLY PASSWORD
    username = "postgres"
    password = "'']'"
    host = "localhost"
    port = "5432"
    database = "ecommerce_db"

    connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)

    print("Reading dataset...")
    df = pd.read_csv(dataset_path)

    print("Loading into PostgreSQL...")
    df.to_sql("ecommerce_orders", engine, if_exists="replace", index=False)

    print("Done! Table created: ecommerce_orders")

if __name__ == "__main__":
    load_to_postgres()