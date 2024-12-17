# To-Do List Application
tasks = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks added yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter updated task: ")
            tasks[task_num] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input!")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-5.")
