# Data Engineer Assignment

This repository contains my implementation of the Data Engineer assignment.  
It demonstrates two different approaches to solve the same business problem using:
1. **Pure SQL + Python**  
2. **Pandas DataFrames**  

## Objective

Company XYZ ran a promotional sale for their signature items `x`, `y`, and `z`.  
They want to analyze sales to create a marketing strategy targeting specific age groups.

The tasks were:
- Connect to a **SQLite3** database.
- Extract the **total quantities** of each item bought per customer aged **18–35**.
- For each customer:
  - Calculate the **sum** of quantities per item.
  - Omit items where total quantity = 0.
  - Show no decimal points (only whole numbers).
- Save the results to a **CSV** file with **`;`** as the delimiter.
- Provide two solutions:
  1. **Pure SQL**  
  2. **Pandas DataFrames**  

## Repository Structure
PROJECT/
│
├── sales.db # SQLite database (sample input data for testing)
├── create_sales_db.py # Script to create a sample database with constraints & data
├── sql_solution.py # SQL-based solution
├── pandas_solution.py # Pandas-based solution
└── README.md # This file

## 🛠 Setup Instructions

### 1 Install Python & Dependencies

You need **Python 3.8+** installed.  
Install the required Python package:
```bash
pip install pandas
```

### 2 Create Sample Database (Optional for Testing)
If you do not have the official Eastvantage-provided database, you can create a sample database for local testing:

bash
Copy
Edit
python create_sales_db.py
This will generate sales.db containing:

customers → customer IDs and ages

orders → mapping customers to orders

order_details → items purchased and their quantities

The sample database includes:

Primary keys

Foreign keys

Constraints (NOT NULL, CHECK)

## 📄 Example Output
Both the SQL and Pandas solutions produce the same results
a CSV file listing each customer (aged 18–35), their purchased items,  
and the total quantity per item, formatted with `;` as the delimiter.
