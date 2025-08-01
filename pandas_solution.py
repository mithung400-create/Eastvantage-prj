import sqlite3
import pandas as pd

# 1. Connect to SQLite database
conn = sqlite3.connect("sales.db")

# 2. Load tables into Pandas DataFrames
df_customers = pd.read_sql_query("SELECT * FROM customers", conn)
df_orders = pd.read_sql_query("SELECT * FROM orders", conn)
df_details = pd.read_sql_query("SELECT * FROM order_details", conn)

# 3. Merge tables (equivalent to SQL JOIN)
df = df_orders.merge(df_customers, on="customer_id")
df = df.merge(df_details, on="order_id")

# 4. Filter age between 18 and 35
df = df[(df['age'] >= 18) & (df['age'] <= 35)]

# 5. Remove rows where quantity is NULL
df = df[df['quantity'].notna()]

# 6. Group by customer, age, item → sum quantities
df_grouped = df.groupby(['customer_id', 'age', 'item'], as_index=False)['quantity'].sum()

# 7. Remove rows where total quantity is 0
df_grouped = df_grouped[df_grouped['quantity'] > 0]

# 8. Rename columns for final output
df_grouped.columns = ['Customer', 'Age', 'Item', 'Quantity']

# 9. Save to CSV with semicolon separator
df_grouped.to_csv("output_pandas.csv", sep=";", index=False)

print("Pandas solution completed! File saved as output_pandas.csv")