import sqlite3

class Task:
    def __init__(self, task_id, description, completed, user_id, category_id):
        self.task_id = task_id
        self.description = description
        self.completed = completed
        self.user_id = user_id
        self.category_id = category_id

class User:
    def __init__(self, user_id, name):
        self.user_id =user_id
        self.name = name
        
class Category:
    def __init__(self, user_id, category):
        self.user_id =user_id
        self.name = category
 

# Connect to the SQLite database
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# # Drop existing tables if they exist
# c.execute('''DROP TABLE IF EXISTS users''')
# c.execute('''DROP TABLE IF EXISTS categories''')
# c.execute('''DROP TABLE IF EXISTS tasks''')

# Recreate tables with the correct schema
c.execute('''CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY,
          name TEXT
          )''')

c.execute('''CREATE TABLE IF NOT EXISTS categories (
          id INTEGER PRIMARY KEY,
          name TEXT
          )''')

c.execute('''CREATE TABLE IF NOT EXISTS tasks (
          id INTEGER PRIMARY KEY,
          task TEXT,
          completed INTEGER,
          user_id INTEGER,
          category_id INTEGER,
          FOREIGN KEY (user_id) REFERENCES users(id),
          FOREIGN KEY (category_id) REFERENCES categories(id)
          )''')

conn.commit()

def add_user (name):
    c.execute("INSERT INTO users (name) VALUES (?)" , (name,))
    conn.commit()
    print(f"User {name} added successfully.")

def add_category (name):
    c.execute("INSERT INTO users (name) VALUES (?)" , (name,))
    conn.commit()
    print(f"Category {name} added successfully.")

def add_task(description, user_id, category_id):
    c.execute("INSERT INTO tasks (task, completed, user_id, category_id) VALUES (?, ?, ?, ?)", (description, 0, user_id, category_id))
    conn.commit()
    print("Task added successfully.")

def remove_task(task_id):
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    print("Task removed successfully.")

def update_task(task_id, description):
    c.execute("UPDATE tasks SET task=? WHERE id=?", (description, task_id))
    conn.commit()
    print("Task updated successfully.")

def mark_completed(task_id):
    c.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()
    print("Task marked as completed.")

def view_tasks():
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    print("To-Do List:")
    for task in tasks:
        status = "Completed" if task[2] else "Pending"
        print(f"{task[0]}. {task[1]} - {status}")