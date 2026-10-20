# Getting Started with Databases and SQL

Practice retrieving and transforming data with SQL from Python. The lab uses
the fictional Northwind company database (`data.sqlite`), reads query results
into Pandas DataFrames with `pd.read_sql()`, and covers `SELECT`, aliases,
`CASE`, and SQL built-in functions.

## Learning objectives

- Connect to a SQLite database file with `sqlite3`
- Use `SELECT` to choose columns from a table
- Use aliases (`AS`) to rename columns
- Use `CASE` to create a new column from conditions
- Use built-in string, numeric, and date functions to transform values

## Project structure

| File             | Purpose                                      |
|------------------|----------------------------------------------|
| `main.py`        | Solution code for Steps 1-9                  |
| `test_main.py`   | Tests that check each step                   |
| `data.sqlite`    | Northwind database (`employees`, `orders`, `orderDetails`, ...) |
| `Pipfile`        | Project dependencies                         |

## Setup

```bash
git clone <repo-url>
cd se_sql_select_lab
pipenv install
pipenv shell
```

If pipenv isn't working, a virtual environment works too:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas pytest
```

## Run

```bash
python3 main.py   # prints the employees and orderDetails tables
pytest            # runs the tests
```

## What each step does

| Step | Variable             | Query idea                                                        |
|------|----------------------|-------------------------------------------------------------------|
| 1    | `conn`               | `sqlite3.connect("data.sqlite")`                                  |
| 2    | `df_first_five`      | `SELECT employeeNumber, lastName FROM employees`                  |
| 3    | `df_five_reverse`    | Same columns, `lastName` first                                    |
| 4    | `df_alias`           | `employeeNumber AS ID`                                            |
| 5    | `df_executive`       | `CASE WHEN jobTitle IN (President, VP Sales, VP Marketing) THEN 'Executive' ELSE 'Not Executive' END AS role` |
| 6    | `df_name_length`     | `LENGTH(lastName) AS name_length`                                 |
| 7    | `df_short_title`     | `SUBSTR(jobTitle, 1, 2) AS short_title`                           |
| 8    | `sum_total_price`    | `SUM(ROUND(priceEach * quantityOrdered))` from `orderDetails`     |
| 9    | `df_day_month_year`  | `strftime('%d' / '%m' / '%Y', orderDate)` from `orders`           |

### Example: Step 5 (`CASE`)

```python
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
```

### Example: Step 9 (date parts)

```python
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
           strftime('%d', orderDate) AS day,
           strftime('%m', orderDate) AS month,
           strftime('%Y', orderDate) AS year
    FROM orders
""", conn)
```

## Notes

- Each row's total is rounded **before** summing (Step 8), as the lab asks.
- `orderDate` is stored in the `orders` table, not `orderDetails`.
- `strftime` returns text, so days and months keep their leading zero (`'06'`).
- Remember to close the connection with `conn.close()` when finished.

## Submitting

```bash
git add .
git commit -m "Complete SQL select lab"
git push origin main   # or master, depending on your branch (check with git branch)
```