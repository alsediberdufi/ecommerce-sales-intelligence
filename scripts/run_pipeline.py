#Pipeline runner
#Pipeline runner
#Pipeline runner
print("PIPELINE STARTED")
from pathlib import Path
import pandas as pd
from scripts.data_processing import clean_orders, create_features, merge_datasets

BASE_DIR = Path(__file__).resolve().parent.parent

def run_pipeline():
    print("Loading data...")

    orders = pd.read_csv(BASE_DIR / "data" / "raw" / "olist_orders_dataset.csv")
    customers = pd.read_csv(BASE_DIR / "data" / "raw" / "olist_customers_dataset.csv")
    order_items = pd.read_csv(BASE_DIR / "data" / "raw" / "olist_order_items_dataset.csv")
    products = pd.read_csv(BASE_DIR / "data" / "raw" / "olist_products_dataset.csv")

    print("Cleaning data...")
    orders = clean_orders(orders)

    print("Creating features...")
    orders = create_features(orders)

    print("Filtering delivered orders...")
    orders = orders[orders["order_status"] == "delivered"].copy()
    orders = orders[orders["delivery_time_days"].notna()].copy()

    print("Preparing order items...")
    order_items["item_total_value"] = order_items["price"] + order_items["freight_value"]

    print("Merging datasets...")
    df = merge_datasets(orders, customers, order_items, products)

    print("Saving dataset...")
    output_path = BASE_DIR / "data" / "cleaned" / "final_dataset.csv"
    df.to_csv(output_path, index=False)

    print(f"Pipeline finished! Saved to: {output_path}")

if __name__ == "__main__":
    run_pipeline()