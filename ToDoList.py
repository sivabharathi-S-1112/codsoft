tasks = []
completed = []

def add_tasks():
    global tasks, completed
    n = int(input("Enter how many tasks to add: "))
    for i in range(n):
        task = input(f"Enter task {i+1}: ")
        tasks.append(task)
        completed.append(False)

def view_tasks():
    if tasks:
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if completed[i-1] else "Not Completed"
            print(f"{i}. {task} - {status}")
    else:
        print("Nothing stored in task list")

def remove_task():
    global tasks, completed
    if tasks:
        task_num = int(input("Which task to remove? Enter the corresponding number: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            completed.pop(task_num)
        else:
            print("Invalid task number")
    else:
        print("Nothing stored in task list")

def mark_task_completed():
    if tasks:
        task_num = int(input("Which task is completed? Enter the corresponding task number: ")) - 1
        if 0 <= task_num < len(tasks):
            completed[task_num] = True
        else:
            print("Invalid task number")
    else:
        print("Nothing stored in task list")

def add_task_to_existing():
    task = input("Enter the new task to add: ")
    tasks.append(task)
    completed.append(False)

def main():
    while True:
        print("\nTo perform below tasks, enter the corresponding task number:\n")
        print("1. To add tasks")
        print("2. To view tasks")
        print("3. To remove a task")
        print("4. To mark a task as completed")
        print("5. To add a task to the existing list")
        print("6. To end the process\n")
        option = int(input("Enter your choice: "))

        if option == 1:
            add_tasks()
        elif option == 2:
            view_tasks()
        elif option == 3:
            remove_task()
        elif option == 4:
            mark_task_completed()
        elif option == 5:
            add_task_to_existing()
        elif option == 6:
            break
        else:
            print("INVALID OPTION")

main()