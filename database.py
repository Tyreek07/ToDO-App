import sqlite3

class Database:
    def __init__(self, db_path="database/todo.db"):
        self.con = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            is_completed BOOLEAN DEFAULT 0
        )
        """
        self.con.execute(query)
        self.con.commit()

    def insert_task(self, task):
        query = """
        INSERT INTO tasks (title, description, due_date)
        VALUES (?, ?, ?)
        """
        self.con.execute(query, (task.title, task.description, task.due_date))
        self.con.commit()
        print("Task added")

    def close_task(self, task_id):
        query = "UPDATE task SET is_completed = 1 WHERE id = ?"
        self.con.execute(query, (task_id,))
        self.con.commit()
        print(f"Task {task_id} marked as completed.")

    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id = ?"
        self.con.execute(query, (task_id,))
        self.con.commit()
        print("Task deleted")

    def get_all_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.con.execute(query)
        return result.fetchall()
    
    def get_all_open_tasks(self):
        query = "SELECT * FROM tasks WHERE is_completed = 0"
        result = self.con.execute(query)
        return result.fetchall()

    def get_all_closed_tasks(self):
        query = "SELECT * FROM tasks WHERE is_completed = 1"
        result = self.con.execute(query)
        return result.fetchall()

    def search_task(self, searchtext):
        query = "SELECT * FROM tasks WHERE title LIKE ?"
        pattern = f"%{searchtext}%"
        result = self.con.execute(query, (pattern,))
        return result.fetchall()
