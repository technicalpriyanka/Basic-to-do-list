#to do list  in python
#menu list view - add - mark - remove - exit 

# tasks = [
#     {"task": "Buy groceries", "done": False},
#     {"task": "Read a book", "done": True},
#     {"task": "Exercise for 30 minutes", "done": False}
# ]


def menu_list():                                #calling in main function
    print("\n--- TO DO List Menu ---")      
    print("1. View task")
    print("2. Add task")
    print("3. Mark completion of task")
    print("4. Remove Task")
    print("5. Exit")

#adding task with the help of different functions 
def view_tasks(tasks):
    if not tasks:
        print("\n Right now u don't have an task please add and work on it..")
    else:
        print("\n Your to do list is here..............")
        for i, task in enumerate(tasks, start=1):
            if task['done']:
                status = "done"
            else:
                status = "not done"
            print(f"{i}. {task['task']} [{status}]")

def add_tasks(tasks):
    task_name = input("\n Enter task here ...").strip()
    if task_name:
        tasks.append({"task": task_name, "done":False})
        print(f"Task '{task_name}' is added in your list")
    else:
        print("\n Nothing to add right now - it should not be empty do some task")

def mark_completion_tasks(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\n enter the task number to mark as done  --> ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]['done'] = True
                print(f"Task '{tasks[task_num]['task']}' is completed and marked as done !")
            else:
                print("Invalid task number")

        except ValueError:
            print("Please enter a valid number..")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\n enter the task number to remove task")) - 1
            if 0 <= task_num < len(tasks):
                removed_task = tasks.pop(task_num)
                print(f"task '{removed_task['task']}' removed task from list")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")

def main():
    tasks=[{"task": "Buy groceries", "done": False},
        {"task": "Read a book", "done": True},
        {"task": "Exercise for 30 minutes", "done": False}] #variable store data 
    #u can add here as well

    while True :                        #here we want this in loop format that's why while is here
        menu_list()  

        choice = input("make a choice from list 1 to 5: ").strip()                  
        #.strip() - removes leading or  trailing whitespaces from  string
        print("you have selected an option ", choice)

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_tasks(tasks)

        elif choice == "3":
            mark_completion_tasks(tasks)

        elif choice == "4":
            remove_task(tasks)

        
        elif choice == "5":
            print("All task are over everything looks good..Bye")
            break                                               
            #here we are breaking loop 
        else:
            print("\nInvalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()

