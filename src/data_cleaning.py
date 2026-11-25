
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "raw" / "sales.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "sales_clean.csv"


def load_data(file_path):
    """Load the raw sales dataset."""
    return pd.read_csv(file_path)


def clean_data(df):
    """Clean and standardize the sales dataset."""

    df = df.copy()

    # 1. Remove duplicate records
    df = df.drop_duplicates()

    # 2. Convert dates
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    # 3. Standardize text columns
    text_columns = [
        "status",
        "category",
        "product_name",
        "city"
    ]

    for column in text_columns:
        df[column] = df[column].str.strip()

    df["status"] = df["status"].str.title()
    df["category"] = df["category"].str.title()

    # 4. Handle missing values
    df["city"] = df["city"].fillna("Unknown")

    # 5. Ensure numeric columns have correct types
    numeric_columns = [
        "quantity",
        "unit_price",
        "discount"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove rows with missing critical information
    required_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "quantity",
        "unit_price",
        "discount",
        "status"
    ]

    df = df.dropna(subset=required_columns)

    # 6. Calculate revenue after discount
    df["revenue"] = (
        df["quantity"]
        * df["unit_price"]
        * (1 - df["discount"])
    ).round(2)

    return df


def save_data(df, output_file):
    """Save the cleaned dataset using the required format."""

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output_file,
        index=False,
        sep=";",
        decimal=",",
        date_format="%Y-%m-%d"
    )


def main():

    print("Loading raw dataset...")

    raw_df = load_data(INPUT_FILE)

    print(f"Original rows: {len(raw_df)}")
    print(f"Original duplicates: {raw_df.duplicated().sum()}")

    print("\nCleaning dataset...")

    clean_df = clean_data(raw_df)

    print("\nSaving cleaned dataset...")

    save_data(clean_df, OUTPUT_FILE)

    print("\nCleaning completed successfully!")
    print(f"Cleaned rows: {len(clean_df)}")
    print(f"Remaining duplicates: {clean_df.duplicated().sum()}")

    print("\nMissing values after cleaning:")
    print(clean_df.isnull().sum())

    print(f"\nSaved file: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
