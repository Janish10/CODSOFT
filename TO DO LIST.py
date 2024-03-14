tasks = []

def display_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

while True:
    user_input = input("Enter a task :")

    if user_input.lower() == 'exit':
        print("Exiting program.")
        break

    tasks.append(user_input)
    print("Task added!\n")
    
    display_tasks()
