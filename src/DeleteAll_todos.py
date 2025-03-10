

from src import _config

def delete_all_todos(conn):
    """Deletes all todos from the database."""
    sql = "DELETE FROM todos;"
    _config.execute_sql(conn, sql)
    print("All todos deleted successfully.")