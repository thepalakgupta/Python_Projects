todo_list = []

def show_tasks():
    if not todo_list:
        print("\nNo tasks in your to-do list.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(todo_list, 1):
        status = "✓" if task['completed'] else "✗"
        print(f"{i}. {task['name']} [{status}]")

def add_task():
    task_name = input("Enter the task name: ")
    todo_list.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added.")

def complete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed['name']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Have a productive day!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the To-Do List App
main()
