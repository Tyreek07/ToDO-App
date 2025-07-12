# Klasse Task: Modell für einzelne Aufgaben

class Task:
    def __init__(self, title, description, due_date):
        self.id = 0
        self.title = title
        self.description = description
        self.due_date = due_date
        self.is_completed = 0
    

