# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference code: look at the employees table
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# STEP 2
# Employee number and last name only, for all employees
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)

# STEP 3
# Same as step 2, but with the columns in reverse order
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)

# STEP 4
# Same as step 3, but employeeNumber is renamed to 'ID' with an alias
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)

# STEP 5
# Use CASE to bin job titles into a new 'role' column
df_executive = pd.read_sql("""
    SELECT *,
        CASE
            WHEN jobTitle = 'President'
              OR jobTitle = 'VP Sales'
              OR jobTitle = 'VP Marketing' THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)

# STEP 6
# LENGTH() gives the number of characters in each last name
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)

# STEP 7
# SUBSTR(text, start, length): first two letters of each job title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)

# Reference code: look at the orderDetails table
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# Round each line's total (priceEach * quantityOrdered) first, then add them up.
# Selecting the column from the result gives a Series, so sum_total_price[0]
# is the total.
sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price
    FROM orderDetails
""", conn)["total_price"]

# STEP 9
# orderDate lives in the orders table (not orderDetails).
# strftime() pulls out the day (%d), month (%m) and year (%Y) as text,
# so day '06' keeps its leading zero.
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
           strftime('%d', orderDate) AS day,
           strftime('%m', orderDate) AS month,
           strftime('%Y', orderDate) AS year
    FROM orders
""", conn)

# Close the connection
conn.close()