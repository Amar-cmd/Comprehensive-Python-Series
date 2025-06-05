#! +------------+
#! | To-Do List |
#! +------------+

def show_menu():
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Tasks")
    print("4. Remove Tasks")
    print("5. Exit")
    print()

todo_list = []


def add_task():
    task = input("Enter Task: ").strip()

    if task:
        if task not in todo_list:
            todo_list.append(task)
            print(f"Task Added: {task}")
        else:
            print("Task already exists in the list.")
    else:
        print("Task cannot be empty.")


def view_task():
    if todo_list:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("No Task Found")


def update_task():
    if todo_list:
        view_task()

        task_no = input("\nEnter Task Number To Update: ").strip()

        if task_no.isdigit():
            task_no = int(task_no)

            if 1 <= task_no <= len(todo_list):
                new_task = input("\nEnter New Task: ").strip()

                if new_task:
                    old_task = todo_list[task_no - 1]
                    todo_list[task_no - 1] = new_task
                    print(f"Task Updated: {old_task} → {new_task}")
                else:
                    print("Task cannot be empty")
            else:
                print("Invalid Task Number")
        else:
            print("Please enter a valid number.")
    else:
        print("No task to update")


def remove_task():
    if todo_list:
        view_task()
        task_no = input("\nEnter task number to remove: ").strip()

        if task_no.isdigit():
            task_no = int(task_no)
            if 1 <= task_no <= len(todo_list):
                removed_task = todo_list.pop(task_no - 1)
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number")

        else:
            print("Please enter a valid number.")
    else:
        print("No task to remove.")


while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    match choice:
        case "1":
            add_task() # Create
        case "2":
            view_task() # Read
        case "3":
            update_task() # Update
        case "4":
            remove_task() # Delete
        case "5":
            print("Exiting To Do List")
            break
        case _:
            print("Invalid Choice. Please select from the menu.")
















