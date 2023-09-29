# TO-DO LIST - (Task 1 - CodSoft)

tasks = []


def add_task(task):
    tasks.append(task)


def remove_task(task):
    if task in tasks:
        tasks.remove(task)


def list_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        list_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Try again.")
