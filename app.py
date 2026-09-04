import streamlit as st
import pandas as pd

st.title("AI Sales & Revenue Analytics")
st.write("Upload your sales CSV to analyze")

def analyze_sales(file):
    data = pd.read_csv(file)
    total_sales = data["Sales"].sum() if "Sales" in data.columns else len(data)
    total_revenue = data["Revenue"].sum() if "Revenue" in data.columns else 0
    top_product = data.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(1) if "Product" in data.columns else "N/A"
    return {"Total Sales": total_sales, "Total Revenue": total_revenue, "Top Product": top_product}

uploaded = st.file_uploader("Choose CSV", type="csv")
if uploaded is not None:
    result = analyze_sales(uploaded)
    st.metric("Total Sales", result["Total Sales"])
    st.metric("Total Revenue", f"${result['Total Revenue']:,.2f}")
    st.write(result["Top Product"])