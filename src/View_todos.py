

from src import _config

def view_todos(conn):
    """Views all todos in the database."""
    sql = "SELECT * FROM todos;"
    todos = _config.fetch_sql(conn, sql)
    if todos:
        for todo in todos:
            print(f"ID: {todo[0]}, Task: {todo[1]}, Completed: {'Yes' if todo[2] else 'No'}")
    else:
        print("No todos found.")