
tasks = []

def addTask():
    User = input("Enter a task: ")
    tasks.append(User)
    print("SUCCESFULLY ADDED")

def viewTask():
    if  not tasks:
        print("You have no tasks.")
    else:
        print("These are your current tasks: ")
        for task in tasks:
            print(task)

def removeTask():
    user = input("Enter the task to delete: ")

    if user not in tasks:
        print(user + " is not in the list!")
    else:
        tasks.remove(user)
        print("REMOVED SUCCESFULLY")


while True:
    print("To ADD a task, enter (1)")
    print("To VIEW your tasks, enter (2)")
    print("To DELETE a task, enter (3)")
    print("To exit, enter (4)")
    choice = input("Enter your choice: ")

    if choice == "1":
        addTask()

    elif choice == "2":
        viewTask()
    
    elif choice == "3":
        removeTask()

    elif choice == "4":
        print("Exited succesfully")
        break

    else:
        print("Invalid input. Please enter (1-4)")


