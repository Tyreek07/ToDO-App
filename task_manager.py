# Klasse TaskManager: steuert alle Aufgabenoperationen
from task import Task
from database import Database

class TaskManager:
    def __init__(self):
        self.db = Database()

    def add_task(self):
        task_title = input("Write the title of the task: ")
        task_desc = input("Write the description of the task:\n")
        task_due_date_month = input("What month is the task due?: ")
        task_due_date_day = input("What day is the task due?: ")
        task_due_date_year = input("What year is the task due?: ")
        task_due_date = str(task_due_date_day) + "/" + str(task_due_date_month) + "/" + str(task_due_date_year)
        new_task = Task(task_title, task_desc, task_due_date)
        self.db.insert_task(new_task)

    def del_task(self):
        self.db.get_all_tasks()
        picked_task = input("Which task do you want to delete?: ")
        picked_task = int(picked_task)
        self.db.delete_task(picked_task)
    
    def search_task(self):
        search_text = input("Write your search text: ")
        self.db.search_task(search_text)

    def close_task(self):
        self.db.get_all_open_tasks()
        picked_task = input("Which task do you want to close?: ")
        picked_task = int(picked_task)
        self.db.close_task(picked_task)

