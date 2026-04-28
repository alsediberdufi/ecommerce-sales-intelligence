# 🛒 E-commerce Sales Intelligence Dashboard

## 🚀 Live Project Preview



---

## 📌 Project Overview

This project is an end-to-end data analytics solution designed to analyze e-commerce sales performance. It covers the full data lifecycle: from raw data processing and transformation to database storage and interactive dashboard visualization.

The objective is to extract actionable business insights such as revenue trends, customer behavior, and geographic performance.

---

## 🧰 Tech Stack

* **Python (Pandas, NumPy)** → Data processing & feature engineering
* **PostgreSQL** → Data storage & querying
* **SQL** → Data modeling, aggregation, and views
* **Power BI** → Interactive dashboard & visualization

---

## 🏗️ Architecture

Raw Data → Python Pipeline → Clean Dataset → PostgreSQL → SQL Views → Power BI Dashboard

---

## ⚙️ Data Pipeline

The pipeline processes raw datasets and produces a clean, analysis-ready dataset.

### Steps:

1. Load raw CSV datasets
2. Clean and transform data
3. Create new features:

   * Order total value
   * Delivery time (days)
   * Order month
4. Filter relevant records (e.g., delivered orders)
5. Merge datasets into a final dataset

📂 Output:

```
data/cleaned/final_dataset.csv
```

---

## 🗄️ Database Layer (PostgreSQL)

### Main Table

* `ecommerce_orders`

### SQL Views

#### 📊 KPI View

```sql
SELECT * FROM ecommerce_kpis;
```

#### 📈 Monthly Revenue

```sql
SELECT * FROM ecommerce_monthly_revenue;
```

#### 🌍 Top Cities

```sql
SELECT * FROM ecommerce_top_cities;
```

---

## 📊 Dashboard (Power BI)

### Key Components

#### 🔹 KPI Cards

* Total Revenue
* Total Orders
* Total Customers
* Average Delivery Time

#### 🔹 Revenue Trend

* Monthly revenue evolution

#### 🔹 Geographic Analysis

* Top cities by revenue

---

## 📸 Dashboard Preview

### Full Dashboard

![Dashboard Overview](dashboard/dashboard_overview.png)

### Monthly Revenue

![Monthly Revenue](dashboard/monthly_revenue.png)

### Top Cities

![Top Cities](dashboard/top_cities.png)

---

## 📈 Key Insights

* São Paulo generates the highest revenue, indicating strong regional concentration
* Revenue peaks during mid-year months and declines significantly after month 8
* The near 1:1 ratio of customers to orders suggests low repeat purchase behavior
* Delivery time averages ~12 days, highlighting potential optimization opportunities

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
py -3.12 -m scripts.run_pipeline
py -3.12 -m scripts.load_to_postgres
```

Then:

1. Open PostgreSQL (`ecommerce_db`)
2. Run SQL views from `sql/views.sql`
3. Open Power BI and connect to PostgreSQL
4. Load views and refresh dashboard

---

## 📂 Project Structure

```
ecommerce-sales-intelligence/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── notebooks/
│   └── ecommerce_analysis.ipynb
│
├── scripts/
│   ├── run_pipeline.py
│   └── load_to_postgres.py
│
├── sql/
│   └── views.sql
│
├── dashboard/
│   ├── dashboard_overview.png
│   ├── monthly_revenue.png
│   └── top_cities.png
│
├── README.md
└── requirements.txt
```

---

## 🧠 What This Project Demonstrates

* End-to-end data pipeline design
* Data cleaning and feature engineering
* SQL data modeling and reusable views
* Database integration (PostgreSQL)
* Data visualization and storytelling
* Cross-tool integration (Python → SQL → BI)

---

## 🔮 Future Improvements

* Add customer segmentation analysis
* Implement repeat customer / retention metrics
* Automate pipeline scheduling
* Deploy dashboard to Power BI Service
* Add real-time data ingestion

---

## 👤 Author

Alsedi Berdufi
