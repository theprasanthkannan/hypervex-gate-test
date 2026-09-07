from db import run_query


def fetch_sales(region):
    """Sales rows for a region."""
    return run_query(f"SELECT * FROM sales WHERE region = '{region}'")


def fetch_totals():
    return run_query("SELECT region, SUM(amount) FROM sales GROUP BY region")
