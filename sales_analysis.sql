-- Create Table
CREATE TABLE ecommerce_sales (
Order_ID INT,
Order_Date DATE,
Customer VARCHAR(50),
Category VARCHAR(50),
Region VARCHAR(50),
Sales INT,
Profit INT
);

-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM ecommerce_sales;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM ecommerce_sales;

-- Profit Margin
SELECT 
SUM(Profit) / SUM(Sales) * 100 AS Profit_Margin
FROM ecommerce_sales;

-- Sales by Category
SELECT Category, SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Category;

-- Profit by Category
SELECT Category, SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Category;

-- Sales by Region
SELECT Region, SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Region;

-- Top Selling Category
SELECT Category, SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Category
ORDER BY Total_Sales DESC
LIMIT 1;
