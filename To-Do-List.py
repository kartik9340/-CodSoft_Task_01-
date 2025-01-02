# Create a To-Do list project using python

tasks = []

# Defining tasks

def addTask():
    task = input("Please enter a task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the list.")


def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"Task #{index} - {task['task']} [{status}]")


def deleteTask():
    listTasks()
    if tasks:
        try:
            taskToDelete = int(input("Enter the task number to delete: "))
            if 0 <= taskToDelete < len(tasks):
                removed_task = tasks.pop(taskToDelete)
                print(f"Task '{removed_task['task']}' has been removed.")
            else:
                print(f"Task #{taskToDelete} was not found.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def markCompleted():
    listTasks()
    if tasks:
        try:
            taskToMark = int(input("Enter the task number to mark as completed: "))
            if 0 <= taskToMark < len(tasks):
                tasks[taskToMark]["completed"] = True
                print(f"Task #{taskToMark} has been marked as completed.")
            else:
                print(f"Task #{taskToMark} was not found.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


if __name__ == "__main__":
    print("Welcome to the To-Do list app! 😊")

# initializing loop

    while True:
        print("\nPlease select one of the following options:")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List all tasks")
        print("4. Mark a task as completed")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            markCompleted()
        elif choice == "5":
            print("Goodbye! 👋👋")
            break
        else:
            print("Invalid input. Please try again.")
