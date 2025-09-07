# task_tracker.py

tasks = []  # an empty list to store our tasks

def show_menu():
    print("\nTask Tracker")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "✅" if t["done"] else "❌"
            print(f"{i}. {t['task']} [{status}]")

def complete_task():
    view_tasks()
    num = int(input("Enter task number to mark complete: "))
    if 1 <= num <= len(tasks):
        tasks[num-1]["done"] = True
        print(f"Task '{tasks[num-1]['task']}' marked complete!")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
