import pandas as pd


def analyze_sales(file="sales_data.csv"):
    # Read sales data
    data = pd.read_csv(file)

    # Calculate total sales and revenue
    total_sales = data["Sales"].sum()
    total_revenue = data["Revenue"].sum()

    # Find product with highest total revenue
    revenue_by_product = data.groupby("Product")["Revenue"].sum()
    top_product = revenue_by_product.idxmax()

    # Find product with highest total sales
    sales_by_product = data.groupby("Product")["Sales"].sum()
    top_sales_product = sales_by_product.idxmax()

    # Find product with highest number of customers
    customers_by_product = data.groupby("Product")["Customers"].sum()
    top_customer_product = customers_by_product.idxmax()

    # Average revenue per product
    average_revenue = revenue_by_product.mean()

    # Products below average revenue
    low_revenue_products = revenue_by_product[
        revenue_by_product < average_revenue
    ].index.tolist()

    # Generate recommendations
    recommendations = []

    recommendations.append(
        f"Focus on {top_product} because it generates the highest total revenue."
    )

    recommendations.append(
        f"Promote {top_sales_product} because it has the highest sales volume."
    )

    recommendations.append(
        f"{top_customer_product} attracts the highest number of customers."
    )

    if low_revenue_products:
        recommendations.append(
            "Review these low-revenue products: "
            + ", ".join(low_revenue_products)
        )

    return {
        "Total Sales": total_sales,
        "Total Revenue": total_revenue,
        "Top Revenue Product": top_product,
        "Top Sales Product": top_sales_product,
        "Top Customer Product": top_customer_product,
        "Recommendations": recommendations
    }


if _name_ == "_main_":
    print("AI Sales & Revenue Analytics Assistant")
    print("Upload your sales CSV to analyze your business data.")

    try:
        results = analyze_sales()

        print("\n--- Sales Analysis ---")
        print("Total Sales:", results["Total Sales"])
        print("Total Revenue:", results["Total Revenue"])
        print("Top Revenue Product:", results["Top Revenue Product"])
        print("Top Sales Product:", results["Top Sales Product"])
        print("Top Customer Product:", results["Top Customer Product"])

        print("\n--- Recommendations ---")
        for recommendation in results["Recommendations"]:
            print("-", recommendation)

    except FileNotFoundError:
        print("Error: sales_data.csv was not found.")

    except KeyError as e:
        print(f"Error: Missing column in CSV file: {e}")

    except Exception as e:
        print(f"Error: {e}")
