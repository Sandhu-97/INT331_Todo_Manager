import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(title: str):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    
    tasks.append({
        "id": task_id,
        "title": title,
        "completed": False
    })

    save_tasks(tasks)
    print("Task saved!")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
 
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f'{task["id"]}. [{status}] {task["title"]}')


def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id']!=task_id]
    save_tasks(tasks)
    print("Task deleted.")
    
def menu():
    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Mark Task Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if (choice=="1"):
            title = input("Task title: ")
            add_task(title)
        
        elif (choice=="2"):
            list_tasks()

        elif choice == "3":
            task_id = int(input("Task ID: "))
            delete_task(task_id)

        elif (choice=="5"):
            break

        else:
            print("Invalid choice")

if (__name__ == "__main__"):
    menu()