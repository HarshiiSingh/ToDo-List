import json


def save_tasks_to_file(tasks, filename):
    with open(filename, 'w') as f:
        json.dump(tasks, f)

def load_tasks_from_file(filename):
    with open(filename, 'r') as f:
        tasks = json.load(f)
    return tasks

filename = "tasks.json"

# To-Do list
try:
    tasks = load_tasks_from_file(filename)
except FileNotFoundError:
    tasks = []

# Main Program
while True:
    print("Current tasks: ")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']} ({task['priority']})")

    commands = input("Enter a command (add, remove, quit): ").lower()

    if commands == "quit":
        break

    if commands == "add":
        task_name = input("Enter a task name: ")
        task_priority = input("Enter a task priority (high, medium, low): ")
        tasks.append({
                "name": task_name,
                "priority": task_priority,
                })

    if commands == "remove":
        task_index = int(input("Enter task index to remove: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task index.")
        else:
            removed_task = tasks.pop(task_index)
            print(f"Remove task: {removed_task['name']} ({removed_task['priority']})")

    save_tasks_to_file(tasks, filename)

print("Saved tasks: ")
for task in tasks:
    print(f" - {task['name']} ({task['priority']})")
