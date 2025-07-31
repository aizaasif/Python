list=[]

# User creating the list
i=1
while(i<=5):
    task=input(f"Enter {i} task in to do list ")
    list.append(task)
    i+=1
# Showing list to user 
print("Your TO-DO List contains the following tasks --->",list)

# Updating list (Adding task on the basis of users choice)
choice1=input("If you want to ADD any task from the To-Do List you can simply enter the task or Enter (NO) ")
if choice1!="NO":
    list.append(choice1)
    print("Task added successfully in to do list")
    print(list)
elif choice1=="NO":
    print("Noting added in TO-Do List ")

# Removing any task from the list on the basis of users choice 
choice2=input("Remove the task from To-Do Lisy which you have done Enter the anme of the task only : ")
if choice2 in list:
    list.remove(choice2)
    print("Task removed successfully fron To-Do List ")
    print(list)
else:
    print("Task not available in list")


    





