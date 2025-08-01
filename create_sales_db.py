import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON;")

# Drop old tables if they exist
cursor.execute("DROP TABLE IF EXISTS order_details;")
cursor.execute("DROP TABLE IF EXISTS orders;")
cursor.execute("DROP TABLE IF EXISTS customers;")

# Create tables with constraints
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    age INTEGER NOT NULL CHECK(age >= 0)
);
""")

cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
""")

cursor.execute("""
CREATE TABLE order_details (
    order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    item TEXT NOT NULL,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CHECK(quantity IS NULL OR quantity >= 0)
);
""")

# Insert data
cursor.executemany("INSERT INTO customers VALUES (?, ?)", [
    (1, 21), (2, 23), (3, 35)
])

cursor.executemany("INSERT INTO orders VALUES (?, ?)", [
    (1001, 1), (1002, 2), (1003, 3), (1004, 2)
])

cursor.executemany("""
INSERT INTO order_details (order_id, item, quantity)
VALUES (?, ?, ?)
""", [
    (1001, "x", 5),
    (1001, "y", None),
    (1002, "x", 1),
    (1002, "y", 1),
    (1002, "z", 1),
    (1003, "z", 2),
    (1004, "x", None)
])

conn.commit()
conn.close()

print("Database created successfully with constraints and sample data!")
