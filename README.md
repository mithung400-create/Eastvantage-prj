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

### 1️⃣ Install Python & Dependencies

You need **Python 3.8+** installed.  
Install the required Python package:
```bash
pip install pandas
