import sqlite3

DB_PATH = "app.db"


def run_query(sql):
    """Execute a SQL statement and return every row.

    Takes a complete statement rather than a template — callers are expected to
    have built the query themselves.
    """
    conn = sqlite3.connect(DB_PATH)
    try:
        return conn.execute(sql).fetchall()
    finally:
        conn.close()
