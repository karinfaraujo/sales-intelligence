# Sales Intelligence — Python Data Analysis & Assistant

## Project Overview

Sales Intelligence is a data analysis project developed with Python to explore sales performance, calculate business metrics, create interactive visualizations, and answer questions about sales data through a rule-based assistant.

The project uses a synthetic sales dataset and demonstrates a complete data analysis workflow, from data generation and cleaning to business insights and interactive question answering.

## Objectives

- Generate and prepare a structured sales dataset.
- Clean and transform data using Pandas.
- Perform Exploratory Data Analysis (EDA).
- Calculate key business performance indicators (KPIs).
- Build interactive charts with Plotly.
- Develop a Python-based assistant to answer questions about sales data.

## Technologies

- Python 3.13
- Pandas
- NumPy
- Plotly
- Jupyter Notebook

## Project Structure

```text
sales-intelligence/
│
├── data/
│   ├── raw/
│   │   └── sales.csv
│   └── processed/
│       └── sales_clean.csv
│
├── notebooks/
│   └── exploratory_data_analysis.ipynb
│   └── data_validation.ipynb
│
├── src/
│   ├── generate_dataset.py
│   ├── data_cleaning.py
│   ├── metrics.py
│   ├── visualizations.py
│   └── assistant.py
│
├── outputs/
│   └── charts/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Dataset

The project uses a synthetic dataset containing 1,000 sales orders from 2024.

The dataset includes information such as:

- Order ID and order date
- Customer and product IDs
- Product names and categories
- City
- Quantity
- Unit price
- Discount
- Order status

The raw dataset intentionally includes data quality issues, such as duplicate records, missing city values, and inconsistent text formatting, to demonstrate data cleaning techniques.

**Note:** All sales records are fictional and were generated for educational and portfolio purposes.

## Data Analysis

The Exploratory Data Analysis covers:

- Revenue by product category
- Monthly revenue trends
- Revenue by city
- Top-selling products
- Order status distribution
- Cancellation rate

## Business Metrics

The project calculates the following KPIs:

| Metric | Result |
|---|---:|
| Total Revenue | R$ 2,171,034.51 |
| Total Orders | 875 |
| Average Order Value | R$ 2,481.18 |
| Unique Customers | 280 |
| Cancellation Rate | 12.50% |

Revenue and average order value are calculated using completed orders only. The cancellation rate considers all orders.

## Interactive Visualizations

The project generates five interactive HTML charts using Plotly:

1. Revenue by Product Category
2. Monthly Revenue
3. Revenue by City
4. Top 5 Products by Quantity Sold
5. Order Status Distribution

The charts are saved in `outputs/charts/`.

## Sales Intelligence Assistant

The project includes a command-line assistant developed in Python.

It processes natural-language questions using keyword-based rules and retrieves information from the project's sales data and business metrics.

Example questions:

- What is the total revenue?
- How many orders were completed?
- What is the average order value?
- What is the cancellation rate?
- How many unique customers do we have?
- Which category generates the highest revenue?
- Which city has the highest revenue?
- What is the best-selling product?

**Important:** This is a rule-based assistant, not an AI language model. It does not use an external AI API or Large Language Model (LLM).

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/karinfaraujo
cd sales-intelligence
```

### 2. Create a virtual environment

```bash
py -3.13 -m venv .venv
```

### 3. Activate the environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Generate the dataset

```bash
python src/generate_dataset.py
```

### 6. Clean the data

```bash
python src/data_cleaning.py
```

### 7. Calculate business metrics

```bash
python src/metrics.py
```

### 8. Generate visualizations

```bash
python src/visualizations.py
```

### 9. Run the assistant

```bash
python src/assistant.py
```

To explore the analysis notebook, launch Jupyter:

```bash
jupyter notebook
```

Then open `notebooks/exploratory_data_analysis.ipynb`.

## Key Insights

The analysis identified the following results in the synthetic dataset:

- Electronics is the highest revenue-generating category.
- Porto Alegre is the city with the highest revenue.
- April recorded the highest monthly revenue.
- Office Chair is the best-selling product by quantity.
- The overall cancellation rate is 12.50%.

These findings describe the generated dataset and should not be interpreted as real-world market trends.

## Project Scope and Limitations

This project focuses on Python programming, data analysis, data visualization, and rule-based question answering.

It does not include a web application, database, external AI API, or machine learning model.

## Author

Developed as a Data Analytics portfolio project.

**Focus:** Python | Data Analysis | Business Intelligence | Data Visualization