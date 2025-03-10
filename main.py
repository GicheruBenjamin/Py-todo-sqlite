

'''
    Entry point
'''

import os
import sqlite3
from src import _config, Add_todo, Delete_todo, DeleteAll_todos, Update_todo, View_todos

def main():
    _config.load_env_variables()
    db_path = os.getenv("TODO_DB_PATH", "todo.db")
    conn = _config.create_connection(db_path)
    if not conn:
        return

    _config.ensure_table(conn)

    while True:
        print("\nTodo List Application")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Delete All Todos")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Add_todo.add_todo(conn)
        elif choice == "2":
            View_todos.view_todos(conn)
        elif choice == "3":
            Update_todo.update_todo(conn)
        elif choice == "4":
            Delete_todo.delete_todo(conn)
        elif choice == "5":
            DeleteAll_todos.delete_all_todos(conn)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

    conn.close()

if __name__ == "__main__":
    main()