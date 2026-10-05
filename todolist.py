import json
import os

task_list = []

print("Welcome to the To-Do List Tracker! \n")

print("The commands are as follows:")
print("- add: Add a new task")
print("- complete: Mark a task as complete")
print("- delete: Remove a task")
print("- view: View all tasks")
print("- quit: Quit the application \n")

def print_task_list(print_message):
    if task_list:
        print(print_message)
        index = 1

        for task in task_list:
            print(f"{index}. {task}")
            index += 1
    else:
        print("No tasks in the list.")

def remove_task(task):
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

def add_task(task):
    if not task in task_list:
        if not task == "":
            task_list.append(task)
            print(f"Task '{task}' added to the list.")
        else:
            print("Task cannot be empty. Please enter a valid task.")
    else:
        print(f"Task '{task}' already exists in the list.")

def view_tasks():
    print_task_list("Your tasks:")

if os.path.isfile("tasks.json"):
    with open("tasks.json", "r", encoding="utf-8") as file:
        task_list = json.load(file)
        print_task_list("Your tasks loaded from the previous session:")

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
    
    elif command_input == "view":
        view_tasks()
    
    elif command_input == "quit":
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(task_list, file)

        print("Exiting the To-Do List Tracker. Goodbye!")
        break
    
    else:
        print("Invalid command. Please try again.")