

from src import _config

def delete_todo(conn):
    """Deletes a todo from the database."""
    todo_id = input("Enter todo ID to delete: ")
    sql = "DELETE FROM todos WHERE id = ?;"
    _config.execute_sql(conn, sql, (todo_id,))
    print("Todo deleted successfully.")