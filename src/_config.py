

'''
Using std lib to load env file and creating a 
sqlite db connection that will be used to store
todos . It is always connected immediately it is 
created 
'''

import os
import sqlite3

def load_env_variables(env_file=".env"):
    """Loads environment variables from a .env file."""
    try:
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    os.environ[key] = value
    except FileNotFoundError:
        print(f"Warning: .env file not found at {env_file}")
    except ValueError:
        print(f"Warning: Invalid line in .env file.")

def create_connection(db_file):
    """Creates a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def execute_sql(conn, sql, params=None):
    """Executes an SQL query."""
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conn.commit()
        return cursor
    except sqlite3.Error as e:
        print(f"Error executing SQL: {e}")
        return None

def fetch_sql(conn, sql, params=None):
    """Executes an SQL query and fetches the results."""
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Error fetching SQL: {e}")
        return None

def ensure_table(conn):
    """Creates the 'todos' table if it doesn't exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    );
    """
    execute_sql(conn, create_table_sql)

def get_todo_by_id(conn, todo_id):
    """Fetchs a todo by id"""
    sql = "SELECT * FROM todos WHERE id = ?;"
    result = fetch_sql(conn, sql, (todo_id,))
    if result:
        return result[0]
    return None

