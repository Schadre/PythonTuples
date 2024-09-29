def add_task(tasks):
    name = input("Enter employee's name: ")
    description = input("Enter task description: ")
    deadline = input("Enter deadline (dd/mm/yyyy)")
    tasks.append((name, description, deadline))

def display_task(tasks):
    for task in tasks:
        name, description, deadline = task 
        print(f"Employee: {name}, Task: {description}, Deadline: {deadline}")

def complete_task(tasks):
    task_to_remove = input("Enter the description of the completed task: ")
    for i, task in enumerate(tasks):
        if task[1] == task_to_remove:
            del tasks[i]
            print("Task completed and removed.")
            break
    else:
        print("Task not found")

def main():
    task = []
    while True:
        print("\n1. Add a Task")
        print("2. View Task")
        print("3. Complete a task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(task)
        elif choice == "2":
            display_task(task)
        elif choice == "3":
            complete_task(task)
        elif choice == "4":
            print("Exiting program")
            break 
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()