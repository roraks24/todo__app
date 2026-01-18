task = []

def create_task():
    t = input("Enter Task : ")
    task.append(t)
    print("Task Added!")
    
def show_task():
    if not task:
        print("No tasks added")

    else:
        for i, t in enumerate(task, start=1):
         print(i,t)

def delete_task():
    show_task()
    num = int(input("Enter task to delete : "))
    task.pop(num-1)
    print("Task Deleted!")

while True:
    
    print(
        "\n1. Create Task"
        "\n2. Show Tasks"
        "\n3. Delete Task"
        "\n4. Quit"
    )

    choice = input("Enter Chocie : ")

    if choice == "1":
        create_task()
    elif choice == "2":
        show_task()
    elif choice == "3":
        delete_task()
        
    else:
        break