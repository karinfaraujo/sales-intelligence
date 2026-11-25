
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "processed" / "sales_clean.csv"
OUTPUT_DIR = BASE_DIR / "outputs" / "charts"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    return pd.read_csv(
        DATA_FILE,
        sep=";",
        decimal=",",
        parse_dates=["order_date"]
    )


def generate_charts(df):
    completed = df[df["status"] == "Completed"].copy()

    # 1. Revenue by Category
    category_revenue = (
        completed.groupby("category")["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    fig = px.bar(
        category_revenue,
        x="category",
        y="revenue",
        title="Revenue by Product Category",
        labels={
            "category": "Category",
            "revenue": "Revenue (BRL)"
        },
        text_auto=".2s"
    )
    fig.write_html(OUTPUT_DIR / "revenue_by_category.html")

    # 2. Monthly Revenue
    monthly_revenue = (
        completed.set_index("order_date")["revenue"]
        .resample("MS")
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly_revenue,
        x="order_date",
        y="revenue",
        title="Monthly Revenue",
        labels={
            "order_date": "Month",
            "revenue": "Revenue (BRL)"
        },
        markers=True
    )
    fig.write_html(OUTPUT_DIR / "monthly_revenue.html")

    # 3. Revenue by City
    city_revenue = (
        completed.groupby("city")["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    fig = px.bar(
        city_revenue,
        x="city",
        y="revenue",
        title="Revenue by City",
        labels={
            "city": "City",
            "revenue": "Revenue (BRL)"
        },
        text_auto=".2s"
    )
    fig.write_html(OUTPUT_DIR / "revenue_by_city.html")

    # 4. Top 5 Products by Quantity
    top_products = (
        completed.groupby("product_name")["quantity"]
        .sum()
        .nlargest(5)
        .reset_index()
        .sort_values("quantity", ascending=True)
    )

    fig = px.bar(
        top_products,
        x="quantity",
        y="product_name",
        orientation="h",
        title="Top 5 Products by Quantity Sold",
        labels={
            "product_name": "Product",
            "quantity": "Units Sold"
        },
        text="quantity"
    )
    fig.write_html(OUTPUT_DIR / "top_5_products.html")

    # 5. Order Status Distribution
    status_counts = (
        df["status"].value_counts()
        .rename_axis("status")
        .reset_index(name="orders")
    )

    fig = px.pie(
        status_counts,
        names="status",
        values="orders",
        title="Order Status Distribution",
        hole=0.4
    )
    fig.write_html(OUTPUT_DIR / "order_status_distribution.html")

    print("All charts were generated successfully!")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    data = load_data()
    generate_charts(data)
