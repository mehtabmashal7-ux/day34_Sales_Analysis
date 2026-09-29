import pandas as pd

# ---------------- LOAD DATA ----------------
df = pd.read_csv(r"E:\AI_ML\day34_Sales_Analysis\sales.csv", skipinitialspace=True)

# ---------------- CALCULATE TOTAL SALES ----------------
df["Total_Sales"] = df["Quantity"] * df["Price"]

# ---------------- 1. TOTAL REVENUE ----------------
total_revenue = df["Total_Sales"].sum()

print("Total Revenue: ", total_revenue)

# ---------------- 2. PRODUCT ANALYSIS ----------------
product_sales = df.groupby("Product")["Total_Sales"].sum()
highest_product = product_sales.idxmax()
highest_sales = product_sales.max()

print("Highst Selling Product: ", highest_product)
print("Highest Product Sales: ", highest_sales)

# ---------------- 3. CITY ANALYSIS ----------------
city_sales = df.groupby("City")["Total_Sales"].sum()

print("Sales by City:")
print(city_sales)

highest_city = city_sales.idxmax()
highest_city_sales = city_sales.max()

print("Highest Sales City:", highest_city)
print("Highest City Sales:", highest_city_sales)

# ---------------- 4. QUANTITY ANALYSIS ----------------
product_quantity = df.groupby("Product")["Quantity"].sum()

print("Quantity Sold by Product")
print(product_quantity)

most_sold_product = product_quantity.idxmax()
most_sold_quantity = product_quantity.max()

print("Most Sold Product:", most_sold_product)
print("Units Sold:", most_sold_quantity)

# ---------------- 5. SALE STATISTICS ----------------
average_sale = df["Total_Sales"].mean()
print("Average Sale:", average_sale)

highest_single_sale = df["Total_Sales"].max()
print("Highest Single Sale:", highest_single_sale)

# ---------------- 6. RANKINGS ----------------
print("\nProduct by Total Sales:")
print(product_sales.sort_values(ascending=False))

print("\nCities by Total Sales:")
print(city_sales.sort_values(ascending=False))