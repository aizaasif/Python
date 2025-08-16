# Add Student
stu_list=[]
no=int(input("How many students you want to add : "))

i=1
while i<=no:
    roll_no=int(input("Enter the roll number of student you want to add  : "))
    if roll_no in stu_list:
        print("Roll no already exsist please add another student ")
        continue
    name=input("Enter the name of student you want to add : ")
    marks=list(map(int,input("Enter marks in 3 subjects seprated by space : ").split()))
    stu_list.append(roll_no)
    stu_list.append(name) 
    stu_list.append(marks)
    if name and roll_no and marks in stu_list:
        print(f" ✅ Student added successfully\n")
        i+=1



# View all students 
t1=type(stu_list[0])
t2=type(stu_list[1])
t3=type(stu_list[2])
print("     The list of all the students is : ")
for i in stu_list:
    if type(i)==t1:
        print("     Roll no : ",i)
    if type(i)==t2:
        print("     Name : ",i)
    if type(i)==t3:
        print("     Marks : ",i)
    










    




    
    