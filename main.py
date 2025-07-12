# Einstiegspunkt, Menü und Programmstart
from task_manager import TaskManager

def main():
    manager = TaskManager()
    while True: 
        print("\n1. Add Task\n2. Delete Task\n3. Show Open Tasks\n4. Show Open Tasks\n5. Show Closed Tasks\n5. Search Tasks\n6. Close Task\nPress any other key to close the Task Manager")
        order = input()
        order = str(order)
        if order == "1" or order == "a":
            manager.add_task()
        elif order == "2":
            manager.del_task()
        elif order == "3":
            result = manager.db.get_all_open_tasks()
            print(result)
        elif order == "4":
            result = manager.db.get_all_closed_tasks()
            print(result)
        elif order == "5":
            manager.search_task()
        elif order == "6":
            manager.close_task()
        else:
            print("See you soon :)")
            break





if __name__== "__main__":
    main()