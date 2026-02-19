import os

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append("[ ] " + task)
        save_tasks(tasks)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to mark completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = tasks[num - 1].replace("[ ]", "[✔]")
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter updated task: ")
            tasks[num - 1] = "[ ] " + new_task
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    elif choice == "6":
        print("Exiting To-Do List Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1-6.")
