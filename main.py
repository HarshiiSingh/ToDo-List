# To-Do list
tasks = []


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)


def show_tasks():
    print("To-Do List: ")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")


def remove_task():
    index = int(input("Enter the task number to remove: "))
    tasks.pop(index - 1)

def display_menu():
    print("\nMenu")
    print("1. Add a new task")
    print("2. Show all tasks")
    print("3. Remove a task")
    print("4. Exit")


while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")