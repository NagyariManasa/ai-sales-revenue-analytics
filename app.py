import pandas as pd

def analyze_sales(file):
    data = pd.read_csv(file)

    total_sales = data["Sales"].sum()
    total_revenue = data["Revenue"].sum()
    top_product = data.groupby("Product")["Revenue"].sum().idxmax()

    return {
        "Total Sales": total_sales,
        "Total Revenue": total_revenue,
        "Top Product": top_product
    }

if _name_ == "_main_":
    print("AI Sales & Revenue Analytics Assistant")
    print("Upload your sales CSV to analyze your business data.")
