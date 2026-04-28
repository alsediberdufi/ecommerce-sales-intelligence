import pandas as pd


def clean_orders(orders):
    # Convert dates
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
    orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"])

    return orders


def create_features(orders):
    # Delivery time
    orders["delivery_time_days"] = (
        orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]
    ).dt.days

    # Time features
    orders["order_month"] = orders["order_purchase_timestamp"].dt.month
    orders["order_year"] = orders["order_purchase_timestamp"].dt.year

    return orders


def merge_datasets(orders, customers, order_items, products):
    df = orders.merge(customers, on="customer_id", how="left")
    df = df.merge(order_items, on="order_id", how="left")
    df = df.merge(products, on="product_id", how="left")

    return df