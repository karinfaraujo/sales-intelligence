
from metrics import load_data, get_sales_summary


def format_currency(value):
    return f"R$ {value:,.2f}"


def answer_question(question, df, summary):
    question = question.lower().strip()

    # Revenue by category
    if "category" in question:
        completed = df[df["status"] == "Completed"]

        category_revenue = (
            completed.groupby("category")["revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        category = category_revenue.index[0]
        revenue = category_revenue.iloc[0]

        return (
            f"{category} is the top revenue-generating category, "
            f"with {format_currency(revenue)}."
        )

    # Revenue by city
    elif "city" in question:
        completed = df[df["status"] == "Completed"]

        city_revenue = (
            completed.groupby("city")["revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        city = city_revenue.index[0]
        revenue = city_revenue.iloc[0]

        return (
            f"{city} is the city with the highest revenue, "
            f"generating {format_currency(revenue)}."
        )

    # Best-selling product
    elif "product" in question:
        completed = df[df["status"] == "Completed"]

        product_sales = (
            completed.groupby("product_name")["quantity"]
            .sum()
            .sort_values(ascending=False)
        )

        product = product_sales.index[0]
        quantity = product_sales.iloc[0]

        return (
            f"{product} is the best-selling product, "
            f"with {quantity} units sold."
        )

    # Cancellation rate
    elif "cancel" in question:
        return (
            f"The cancellation rate is "
            f"{summary['cancellation_rate']:.2f}%."
        )

    # Average order value
    elif "average" in question or "ticket" in question:
        return (
            f"The average order value is "
            f"{format_currency(summary['average_order_value'])}."
        )

    # Unique customers
    elif "customer" in question:
        return (
            f"There are {summary['unique_customers']} unique customers "
            f"with completed orders."
        )

    # Total orders
    elif "order" in question:
        return (
            f"There are {summary['total_orders']} completed orders."
        )

    # Total revenue
    elif "revenue" in question or "sales" in question:
        return (
            f"The total revenue is "
            f"{format_currency(summary['total_revenue'])}."
        )

    else:
        return (
            "Sorry, I couldn't identify your question. "
            "Try asking about revenue, orders, customers, "
            "cancellations, categories, cities or products."
        )


def main():
    df = load_data()
    summary = get_sales_summary(df)

    print("=" * 50)
    print("SALES INTELLIGENCE ASSISTANT")
    print("=" * 50)
    print("Ask questions about your sales data.")
    print("Type 'exit' to close the assistant.")

    while True:
        question = input("\nYour question: ")

        if question.lower().strip() == "exit":
            print("Thank you for using Sales Intelligence Assistant!")
            break

        answer = answer_question(question, df, summary)

        print("\nAssistant:")
        print(answer)


if __name__ == "__main__":
    main()
