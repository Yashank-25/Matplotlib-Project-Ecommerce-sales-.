import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------
# Load Dataset
# --------------------------------------------
df = pd.read_csv("ecommerce_sales(2).csv")

# --------------------------------------------
# Basic Information
# --------------------------------------------
print("=" * 50)
print("FIRST 5 RECORDS")
print("=" * 50)
print(df.head())

print("\n")
print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)
print(df.info())

print("\n")
print("=" * 50)
print("STATISTICAL SUMMARY")
print("=" * 50)
print(df.describe())

print("\n")
print("=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

# --------------------------------------------
# Convert Date Column
# --------------------------------------------
df["Date"] = pd.to_datetime(df["Date"])

# Create Month Column
df["Month"] = df["Date"].dt.strftime("%b")

# --------------------------------------------
# Total Sales & Profit
# --------------------------------------------
print("\n")
print("=" * 50)
print("TOTAL SALES")
print("=" * 50)
print(df["Sales"].sum())

print("\n")
print("=" * 50)
print("TOTAL PROFIT")
print("=" * 50)
print(df["Profit"].sum())

# --------------------------------------------
# Sales by Region
# --------------------------------------------
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
plt.bar(region_sales.index,
        region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.grid(axis="y")
plt.show()

# --------------------------------------------
# Category-wise Revenue
# --------------------------------------------
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
plt.bar(category_sales.index,
        category_sales.values)

plt.title("Category-wise Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.grid(axis="y")
plt.show()

# --------------------------------------------
# Monthly Sales Trend
# --------------------------------------------
month_order = ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"]

monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales = monthly_sales.reindex(month_order)

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index,
         monthly_sales.values,
         marker="o",
         linewidth=2)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# --------------------------------------------
# Top 10 Products by Sales
# --------------------------------------------
top_products = (
    df.groupby("Product")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))
plt.barh(top_products.index,
         top_products.values)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.gca().invert_yaxis()
plt.grid(axis="x")
plt.show()

# --------------------------------------------
# Profit by Category
# --------------------------------------------
profit_category = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(7,7))
plt.pie(
    profit_category.values,
    labels=profit_category.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Profit Contribution by Category")
plt.show()

# --------------------------------------------
# Quantity Sold by Category
# --------------------------------------------
quantity = df.groupby("Category")["Quantity"].sum()

plt.figure(figsize=(8,5))
plt.bar(quantity.index,
        quantity.values)

plt.title("Quantity Sold by Category")
plt.xlabel("Category")
plt.ylabel("Quantity")
plt.grid(axis="y")
plt.show()

# --------------------------------------------
# Profit vs Sales
# --------------------------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["Sales"],
            df["Profit"])

plt.title("Profit vs Sales")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.show()

# --------------------------------------------
# Top 5 Regions by Profit
# --------------------------------------------
region_profit = (
    df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
plt.bar(region_profit.index,
        region_profit.values)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.grid(axis="y")
plt.show()

print("\nDashboard Analysis Completed Successfully!")
