# Student Result Info

dict={}

# input from 1st student
stu1_name=input("Enter your name : ")
stu1_marks=int(input("Enter your marks out of 100 : "))
dict.update({stu1_name:stu1_marks})
# input from 2nd student
stu2_name=input("Enter your name : ")
stu2_marks=int(input("Enter your marks out of 100 : "))
dict.update({stu2_name:stu2_marks})
# input fron 3rd student
stu3_name=input("Enter your name : ")
stu3_marks=int(input("Enter your marks out of 100 : "))
dict.update({stu3_name:stu3_marks})

# Printing names of the students 
print(dict)
print("The names of all the students are : ")
print(tuple(dict.keys()))


# Taking input from the user 
username=input("Tell your name : ")
# Applying Conditions
if username in dict:
    marks=dict[username]
    print("Student Found and marks are : ",marks)
else:
    print("Student Not Found ")

# Storing marks in tuple
tuple=(stu1_marks,stu2_marks,stu3_marks)
print("Marks of all students are : ",tuple)
print("High marks are : ",max(tuple))
print("Loe marks are : ",min(tuple))

# # Finding the highest marks
# Highest_Marks=stu1_marks
# if(stu2_marks>Highest_Marks):
#     Highest_Marks=stu2_marks
# if(stu3_marks>Highest_Marks):
#     Highest_Marks=stu3_marks
# print("The highest marks are : ",Highest_Marks)

# # Lowest Marks
# Lowest_Marks=stu1_marks
# if(stu2_marks<Lowest_Marks):
#     Lowest_Marks=stu2_marks
# if(stu3_marks<Lowest_Marks):
#     Lowest_Marks=stu3_marks
# print("The Lowest marks are : ",Lowest_Marks)

# # Converting list of student names in to a set
# print("Names of all students in the form of set are :")
# print(set(dict.keys()))

# # Last 2 letters of each students names
# print("Lat 2 chs of 1st stu name ",stu1_name[-2:])
# print("Lat 2 chs of 2nd stu name ",stu2_name[-2:])
# print("Lat 2 chs of 3rd stu name ",stu3_name[-2:])

# # To check Fail Found
# if stu1_marks<40 or stu2_marks<40 or stu3_marks<40:
#     print("Fail Found")




    
    




