import sqlite3
import csv

# Connect to SQLite database
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# SQL query to aggregate quantities
sql_query = """
SELECT 
    c.customer_id AS Customer,
    c.age AS Age,
    od.item AS Item,
    CAST(SUM(od.quantity) AS INTEGER) AS Quantity
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
WHERE c.age BETWEEN 18 AND 35
  AND od.quantity IS NOT NULL
GROUP BY c.customer_id, c.age, od.item
HAVING SUM(od.quantity) > 0
ORDER BY c.customer_id, od.item;
"""

# Run the query
cursor.execute(sql_query)

# Get column names from the query
fieldnames = [desc[0] for desc in cursor.description]

# Fetch all results
rows = cursor.fetchall()

# Write results to CSV with semicolon separator
with open("output_sql.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    for row in rows:
        writer.writerow(dict(zip(fieldnames, row)))

# Close connection
conn.close()

print("SQL solution completed! File saved as output_sql.csv")