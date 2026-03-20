import pandas as pd

# Load dataset
data = pd.read_csv("ecommerce_data.csv")

print("Dataset Preview:")
print(data.head())

# KPI Calculations
total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
avg_profit_margin = (total_profit / total_sales) * 100

print("\nKey Performance Indicators")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Profit Margin: {:.2f}%".format(avg_profit_margin))

# Sales by Category
print("\nSales by Category")
print(data.groupby("Category")["Sales"].sum())

# Sales by Region
print("\nSales by Region")
print(data.groupby("Region")["Sales"].sum())

# Most Profitable Category
print("\nProfit by Category")
print(data.groupby("Category")["Profit"].sum())
