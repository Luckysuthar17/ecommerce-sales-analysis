import streamlit as st
import pandas as pd

st.title("E-Commerce Sales Dashboard")

data = pd.read_csv("ecommerce_data.csv")

st.subheader("Dataset Preview")
st.write(data)

# KPIs
total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
profit_margin = (total_profit / total_sales) * 100

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", total_sales)
col2.metric("Total Profit", total_profit)
col3.metric("Profit Margin %", round(profit_margin,2))

st.subheader("Sales by Category")
sales_category = data.groupby("Category")["Sales"].sum()
st.bar_chart(sales_category)

st.subheader("Sales by Region")
sales_region = data.groupby("Region")["Sales"].sum()
st.bar_chart(sales_region)

st.subheader("Profit by Category")
profit_category = data.groupby("Category")["Profit"].sum()
st.bar_chart(profit_category)
