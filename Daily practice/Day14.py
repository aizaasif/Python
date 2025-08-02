# # student report management program

# total_student=int(input("Enter total students : "))

# name=[]
# roll_no=[]
# marks=[]
# avg_marks=[]



# for i in range(1,total_student+1):
#     name[i]=input("Enter your name : ")
#     roll_no[i]=int(input("Enter your roll number : "))
#     marks[i]=list(map(int,input("Enter your marks of 3 subjects seprated by space : ").split()))

#     avg_marks[i]=sum(marks[i])/len(marks[i])

#     dict={
#         roll_no[i]:(name[i],marks[i])
#     }
#     print("The data of student ",i,"is ",dict)
#     i+=1

# # 5 stu input --> show 
# marks=[]
# for i in range(1,6):
#     m=int(input(f"{i} Enter your marks "))
#     marks.append(m)
# print(marks)

# def count_even(list):
#     count=0
#     i=0
#     while i<len(list):
#         if(list[i]%2==0):
#             count+=1
#         i+=1
#     print(count)

# # marks=[2,4,6,1,3]
# # count_even(marks)

# num=list(map(int,input("Enter a list of numbers : ").split()))
# count_even(num)

# def calc_fac(n):
#     fac=1
#     for i in range(1,n+1):
#         fac*=i
#     print(f"Fac of {n} is : ",fac)

# calc_fac(5)
# calc_fac(4)
# calc_fac(3)
# calc_fac(2)
# calc_fac(0)

# num=int(input("Enter a number : "))
# def calc_no(n):
#     count=0
#     for i in range(1,n+1):
#         if(i%2!=0):
#             count+=1
#             i+=1
#     print(f"The count of prime number form 1 to {n} is : ",count)

# calc_no(7)
# calc_no(100)

word=input("Enter list of strings seprated by space : ")
list=word.split()
print(list)

def check(list):
    count=0
    for i in range<len(list):
        if i == i[::-1]:
            count+=1
      
    print(f"The no of palindromes in {list} are : ",count)    
    
    
check(list)
        
    
 
        





        















