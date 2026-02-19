def show_menu():
    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

tasks = []

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to update: "))
            if 1 <= num <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1-5.")
