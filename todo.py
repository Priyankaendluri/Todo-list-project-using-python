import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TASKS_FILE, "w") as file:
        file.writelines(task + "\n" for task in tasks)

def show_tasks(tasks):
    """Display tasks"""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task"""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added successfully.")

def mark_completed(tasks):
    """Mark a task as completed"""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index] = f"[✓] {tasks[index]}"
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task"""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the To-Do List"""
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

