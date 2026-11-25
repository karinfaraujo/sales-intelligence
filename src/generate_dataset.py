
import pandas as pd
import numpy as np
from pathlib import Path

# Reproducibility
np.random.seed(42)

# Dataset configuration
N_ORDERS = 1000

# Product catalog
products = [
    ("P001", "Laptop", "Electronics", 3500.00),
    ("P002", "Smartphone", "Electronics", 2200.00),
    ("P003", "Headphones", "Electronics", 350.00),
    ("P004", "Office Chair", "Furniture", 850.00),
    ("P005", "Desk", "Furniture", 1200.00),
    ("P006", "T-shirt", "Clothing", 65.00),
    ("P007", "Jeans", "Clothing", 150.00),
    ("P008", "Blender", "Home & Kitchen", 280.00),
    ("P009", "Coffee Maker", "Home & Kitchen", 450.00),
    ("P010", "Running Shoes", "Sports", 320.00),
    ("P011", "Yoga Mat", "Sports", 90.00),
]

cities = [
    "Sao Paulo",
    "Rio de Janeiro",
    "Curitiba",
    "Belo Horizonte",
    "Porto Alegre"
]

# Generate orders
orders = []

for i in range(N_ORDERS):

    product = products[np.random.randint(0, len(products))]

    order_date = pd.Timestamp("2024-01-01") + pd.Timedelta(
        days=np.random.randint(0, 366)
    )

    quantity = np.random.randint(1, 6)

    unit_price = product[3] * np.random.uniform(0.90, 1.10)

    discount = np.random.choice(
        [0, 0.05, 0.10, 0.15, 0.20],
        p=[0.40, 0.20, 0.20, 0.15, 0.05]
    )

    status = np.random.choice(
        ["Completed", "Cancelled"],
        p=[0.88, 0.12]
    )

    order = {
        "order_id": f"ORD{i + 1:04d}",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "customer_id": f"CUST{np.random.randint(1, 301):04d}",
        "product_id": product[0],
        "product_name": product[1],
        "category": product[2],
        "city": np.random.choice(cities),
        "quantity": quantity,
        "unit_price": round(unit_price, 2),
        "discount": discount,
        "status": status
    }

    orders.append(order)

# Create DataFrame
df = pd.DataFrame(orders)

# Introduce intentional data quality issues
# 1. Inconsistent status formatting
df.loc[10:19, "status"] = df.loc[10:19, "status"].str.lower()
df.loc[20:24, "status"] = " " + df.loc[20:24, "status"] + " "

# 2. Missing city values
missing_city_indices = np.random.choice(
    df.index, size=8, replace=False
)
df.loc[missing_city_indices, "city"] = np.nan

# 3. Duplicate records
duplicates = df.sample(n=10, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# Save raw dataset
output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "sales.csv"
df.to_csv(output_file, index=False)

# Display generation summary
print("Dataset successfully generated!")
print(f"File: {output_file}")
print(f"Total rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("\nDataset preview:")
print(df.head())

print("\nStatus distribution:")
print(df["status"].value_counts(dropna=False))

print("\nMissing values:")
print(df.isnull().sum())
