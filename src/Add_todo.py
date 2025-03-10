

'''
Add a new todo to the database
'''

from src import _config

def add_todo(conn):
    """Adds a new todo to the database."""
    task = input("Enter todo task: ")
    sql = "INSERT INTO todos (task) VALUES (?);"
    _config.execute_sql(conn, sql, (task,))
    print("Todo added successfully.")