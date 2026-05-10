import sqlite3
import pandas as pd
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect('sales.db')

# Load data into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM sales", conn)

# Close the connection
conn.close()

# Display the first few rows of the DataFrame to verify
print("Data loaded into DataFrame:")
print(df.head())

# Perform some basic statistical analysis using NumPy and Pandas

# Calculate total sales
total_sales = df['sales'].sum()
print(f"Total Sales: {total_sales}")

# Calculate average sales
average_sales = df['sales'].mean()
print(f"Average Sales: {average_sales}")

# Calculate standard deviation of sales
std_deviation = df['sales'].std()
print(f"Standard Deviation of Sales: {std_deviation}")

# Calculate total sales by product
sales_by_product = df.groupby('product')['sales'].sum()
print("\nTotal Sales by Product:")
print(sales_by_product)

# Calculate total sales by region
sales_by_region = df.groupby('region')['sales'].sum()
print("\nTotal Sales by Region:")
print(sales_by_region)

# Calculate monthly sales trends (assuming 'date' is in YYYY-MM-DD format)
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')

monthly_sales_trends = df.groupby('month')['sales'].sum()
print("\nMonthly Sales Trends:")
print(monthly_sales_trends)
