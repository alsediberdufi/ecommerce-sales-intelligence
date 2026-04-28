-- KPIs
CREATE VIEW ecommerce_kpis AS
SELECT
    ROUND(SUM(item_total_value)::numeric, 2) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(AVG(delivery_time_days)::numeric, 2) AS avg_delivery_days
FROM ecommerce_orders;

-- Monthly revenue
CREATE VIEW ecommerce_monthly_revenue AS
SELECT
    order_month,
    ROUND(SUM(item_total_value)::numeric, 2) AS monthly_revenue
FROM ecommerce_orders
GROUP BY order_month;

-- Top cities
CREATE VIEW ecommerce_top_cities AS
SELECT
    customer_city,
    ROUND(SUM(item_total_value)::numeric, 2) AS revenue
FROM ecommerce_orders
GROUP BY customer_city;