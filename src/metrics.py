
import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = BASE_DIR / "data" / "processed" / "sales_clean.csv"


def load_data():
    """Load the cleaned sales dataset."""

    df = pd.read_csv(
        DATA_FILE,
        sep=";",
        decimal=",",
        parse_dates=["order_date"]
    )

    return df


def get_completed_orders(df):
    """Return only completed orders."""

    return df[df["status"] == "Completed"].copy()


def calculate_total_revenue(df):
    """Calculate revenue from completed orders."""

    completed_orders = get_completed_orders(df)

    return round(completed_orders["revenue"].sum(), 2)


def calculate_total_orders(df):
    """Count unique completed orders."""

    completed_orders = get_completed_orders(df)

    return int(completed_orders["order_id"].nunique())


def calculate_average_order_value(df):
    """Calculate average revenue per completed order."""

    total_revenue = calculate_total_revenue(df)
    total_orders = calculate_total_orders(df)

    if total_orders == 0:
        return 0.0

    return round(total_revenue / total_orders, 2)


def calculate_unique_customers(df):
    """Count unique customers with completed orders."""

    completed_orders = get_completed_orders(df)

    return int(completed_orders["customer_id"].nunique())


def calculate_cancellation_rate(df):
    """Calculate the percentage of cancelled orders."""

    total_orders = df["order_id"].nunique()

    if total_orders == 0:
        return 0.0

    cancelled_orders = df.loc[
        df["status"] == "Cancelled",
        "order_id"
    ].nunique()

    return round(
        (cancelled_orders / total_orders) * 100,
        2
    )


def get_sales_summary(df):
    """Generate a summary of all business metrics."""

    return {
        "total_revenue": calculate_total_revenue(df),
        "total_orders": calculate_total_orders(df),
        "average_order_value": calculate_average_order_value(df),
        "unique_customers": calculate_unique_customers(df),
        "cancellation_rate": calculate_cancellation_rate(df)
    }


if __name__ == "__main__":

    df = load_data()

    summary = get_sales_summary(df)

    print("=" * 45)
    print("SALES INTELLIGENCE - BUSINESS METRICS")
    print("=" * 45)

    print(f"Total Revenue: R$ {summary['total_revenue']:,.2f}")
    print(f"Total Orders: {summary['total_orders']}")
    print(
        f"Average Order Value: "
        f"R$ {summary['average_order_value']:,.2f}"
    )
    print(f"Unique Customers: {summary['unique_customers']}")
    print(f"Cancellation Rate: {summary['cancellation_rate']:.2f}%")

    print("=" * 45)
