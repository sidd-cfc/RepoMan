# task_tracker.py

import os

tasks = []

def show_menu():
    print("\nTask Tracker")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Exit")

def add_task(task_name=None):
    if task_name is None:  # interactive mode
        task = input("Enter task: ")
    else:  # demo mode
        task = task_name
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "✅" if t["done"] else "❌"
            print(f"{i}. {t['task']} [{status}]")

def complete_task(index=None):
    view_tasks()
    if index is None:  # interactive mode
        num = int(input("Enter task number to mark complete: "))
    else:  # demo mode
        num = index
    if 1 <= num <= len(tasks):
        tasks[num-1]["done"] = True
        print(f"Task '{tasks[num-1]['task']}' marked complete!")
    else:
        print("Invalid task number.")

# detect demo mode (GitHub Actions sets CI=true)
demo_mode = os.environ.get("CI") == "true"

if demo_mode:
    print("Running in DEMO MODE (GitHub Actions)")
    add_task("Learn Python")
    add_task("Build CI/CD Pipeline")
    view_tasks()
    complete_task(1)
    view_tasks()
else:
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
            print("Invalid choice. Please try again.")