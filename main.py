#!usr/bin/env python3
from models import add_user, add_category, add_task, remove_task,update_task,mark_completed,view_tasks

def main():
    while True:
        print("\n1. Add User")
        print("2. Add Category")
        print("3. Add Task")
        print("4. Remove Task")
        print("5. Update Task")
        print("6. Mark Task as Completed")
        print("7. View Tasks")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice = int(choice)

            if choice == 1:
                user_name = input("Enter user name: ")
                add_user(user_name)

            if choice == 2:
                category_name = input("Enter category name: ")
                add_category(category_name)

            if choice == 3:
                task_description = input("Enter task description: ")
                user_id = input("Enter User ID")
                category_id = input("Enter Category ID")
                add_task(task_description, user_id,category_id)
                  
            elif choice == 4:
                task_id = int(input("Enter task id to remove: "))
                remove_task(task_id)

            elif choice == 5:
                task_id = int(input("Enter task id to update: "))
                task_description = input("Enter new task description: ")
                update_task(task_id, task_description)

            elif choice == 6:
                task_id = int(input("Enter task id to mark as completed: "))
                mark_completed(task_id)

            elif choice == 7:
                view_tasks()

            elif choice == 8:
                 print("exiting...")
                 break
            else:
                print("Invalid choice, please try again.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()