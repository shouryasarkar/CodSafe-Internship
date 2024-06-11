# Importing the required modules and files 
import sys
from todolist import ToDoList


def print_menu():
    print("\nTo-Do List Application")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")

def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice  = input("Enter your choice: ")

        if choice == '1':
            for idx, task in enumerate(todo_list.tasks):
                print(f"{idx + 1}.{task}")
            
        elif choice == '2':
            desciption = input("Enter the task desciption: ")
            todo_list.add_task(desciption)
            print("Task added.")

        elif choice == '3':
            try:
                index = int(input("Enter the task number to mark as complete: ")) - 1
                todo_list.update_task(index, completed=True)
                print("Task marked as complet.")
            except(ValueError, IndexError):
                print("Invalid task number.")
            
        elif choice == '4':
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(index)
                print("Task deleted.")
            except:
                print("Invalid task number.")
            
        elif choice == '5':
            filename = input("Enter the filename to save tasks: ")
            todo_list.save_tasks(filename)
            print("Tasks saved.")
        
        elif choice == '6':
            filename = input("Enter the filename to load tasks: ")
            todo_list.load_tasks(filename)
            print("Tasks loaded.")
        
        elif choice == '7':
            print("Exiting the application.")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()