

from src import _config

def update_todo(conn):
    """Updates a todo in the database."""
    todo_id = input("Enter todo ID to update: ")
    todo = _config.get_todo_by_id(conn, todo_id)
    if not todo:
      print("Todo not found")
      return
    task = input(f"Enter updated task (current: {todo[1]}): ")
    completed = input(f"Mark as completed? (yes/no) (current: {'Yes' if todo[2] else 'No'}): ").lower()
    completed_int = 1 if completed == "yes" else 0
    sql = "UPDATE todos SET task = ?, completed = ? WHERE id = ?;"
    _config.execute_sql(conn, sql, (task, completed_int, todo_id))
    print("Todo updated successfully.")