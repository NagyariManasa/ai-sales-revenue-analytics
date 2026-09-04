import streamlit as st
import pandas as pd

st.title("AI Sales & Revenue Analytics")
st.write("Upload your sales CSV to analyze")

uploaded = st.file_uploader("Choose CSV", type=["csv", "CSV"])

def analyze_sales(data):
    total_sales = len(data)
    total_revenue = data["Revenue"].sum()
    top = data.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
    return total_sales, total_revenue, top

if uploaded:
    data = pd.read_csv(uploaded)
    total_sales, total_revenue, top_product = analyze_sales(data)
    
    st.metric("Total Sales", total_sales)
    st.metric("Total Revenue", f"${total_revenue:,.2f}")
    
    st.write("### Product wise Revenue")
    st.dataframe(top_product)
    
    # GRAPHS ADD CHEYADAM
    st.write("### 📊 Graphs")
    st.bar_chart(top_product)
    
    st.write("### Region wise Revenue")
    region_rev = data.groupby("Region")["Revenue"].sum()
    st.bar_chart(region_rev)
    
    st.write("### Product Distribution")
    st.line_chart(data["Revenue"])
    
    st.success("Analysis Complete! 🎉")
