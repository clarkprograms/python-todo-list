import json
import os

task_list = []

print("Welcome to the To-Do List Tracker! \n")

print("The commands are as follows:")
print("- add: Add a new task")
print("- complete: Mark a task as complete")
print("- clear completed: Clear all completed tasks")
print("- delete: Remove a task")
print("- view: View all tasks")
print("- view completed: View completed tasks")
print("- view all: View all tasks")
print("- quit: Quit the application \n")

def print_task_list(print_message, completed):
    if task_list:
        print(print_message)
        index = 1

        contains_items = False

        for task in task_list:
            if task["completed"] == completed:
                print(f"{index}. {task}")
                index += 1

            contains_items = True

        if not contains_items:
            if completed:
                print("No completed tasks in the list.")
            else:
                print("No incomplete tasks in the list.")
            return
            
    else:
        if completed:
            print("No completed tasks in the list.")
        else:
            print("No incomplete tasks in the list.")
        return

def delete_task(task):
    for existing_task in task_list:
        if existing_task["name"] == task:
            task_list.remove(existing_task)
            print(f"Task '{task}' removed from the list.")
            return

    print(f"Task '{task}' not found in the list.")

def complete_task(task):
    for existing_task in task_list:
        if existing_task["name"] == task:
            existing_task["completed"] = True
            print(f"Task '{task}' marked as complete.")
            return

    print(f"Task '{task}' not found in the list.")

def add_task(task):
    for existing_task in task_list:
        if existing_task["name"] == task:
            print(f"Task '{task}' already exists in the list.")
            return

    if task == "":
        print("Task cannot be empty. Please enter a valid task.")
        return
    
    task_list.append({"name": task, "completed": False})
    print(f"Task '{task}' added to the list.")

def clear_completed_tasks():
    completed_tasks = []

    for task in task_list:
        if task["completed"]:
            completed_tasks.append(task)

    if not completed_tasks:
        print("No completed tasks to clear.")
        return

    for task in completed_tasks:
        task_list.remove(task)

    print("All completed tasks have been cleared.")

def view_tasks():
    print_task_list("Your tasks:")

def view_completed_tasks():
    print_task_list("Completed tasks:", True)

def view_all_tasks():
    print_task_list("Current tasks:", False)
    print_task_list("Completed tasks:", True)

if os.path.isfile("tasks.json"):
    with open("tasks.json", "r", encoding="utf-8") as file:
        task_list = json.load(file)
        
        print_task_list("Your tasks loaded from the previous session:\n")
        print_task_list("Completed tasks:", True)
        print_task_list("Incomplete tasks:", False)
        print("\n")

while True:
    command_input = input("input a command: ")

    if command_input == "add":
        task = input("Enter the task: ")
        add_task(task)
    
    elif command_input == "complete":
        completed_task = input("Enter the task to mark as complete: ")

        remove_task(completed_task)
    
    elif command_input == "delete":
        task_to_delete = input("Enter the task to delete: ")
        remove_task(task_to_delete)

    elif command_input == "clear completed":
        clear_completed_tasks()
    
    elif command_input == "view":
        view_tasks()

    elif command_input == "view completed":
        view_completed_tasks()
    
    elif command_input == "view all":
        view_all_tasks()
    
    elif command_input == "quit":
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(task_list, file)

        print("Exiting the To-Do List Tracker. Goodbye!")
        break
    
    else:
        print("Invalid command. Please try again.")
