---
toc: True
comments: True
layout: post
title: To Do list
courses: {'csp': {'week': 5}}
type: hacks
---

```python
#Create an empty list to store tasks
tasks = []

#Function to add a task to the list
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

#Function to view the task list
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

#Function to mark a task as complete
def complete_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter the number of the task you completed: "))
        if 1 <= task_index <= len(tasks):
            completed_task = tasks.pop(task_index - 1)
            print(f"Task '{completed_task}' marked as complete.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to mark as complete.")

#Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```

    
    Options:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Quit

