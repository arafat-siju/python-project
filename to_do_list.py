tasks = []

def show_menu():
    print("\n=== To-Do List ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour tasks:")
        for i, user_input in enumerate(tasks, 1):
            print(f"{i}. {user_input}")

def add_task():
    user_input = input("\nEnter new task: ")
    tasks.append(user_input)
    print(f"Added: {user_input}")

def remove_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("\nEnter task number to remove: "))
            if (1 <= num <= len(tasks)):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a number!")

def main():
    print("Welcome to your To-Do List!")
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("\n----- Goodbye! -----")
            break
        else:
            print("Invalid choice! Please choose between 1 to 4.")

if __name__ == "__main__":
    main()