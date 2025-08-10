# Functions 

# Task 13: Modify the two-number calculator problem and solve it using functions for add, sub etc. Return the results from these functions and display them in main.

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: Division by zero"

# print("Two Number Calculator")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("\nResults:")
# print(f"Addition: {add(num1, num2)}")
# print(f"Subtraction: {sub(num1, num2)}")
# print(f"Multiplication: {mul(num1, num2)}")
# print(f"Division: {div(num1, num2)}")

# Task 14: Write a function which take the radius of circle as first argument and a char (a or c) as second argument. If second argument is a then return the area of circle. If the second argument is c then return the circumference of circle.

# def function(radius,char):
#     if char=="A" or char=="a":
#         Area=3.13*(radius*radius)
#         print(f"Since, your choice is {char} so Area of circle is : ",Area)
#     elif char=="C" or char=="c":
#         circumference=2*3.14*radius
#         print(f"Since. You entered {char} so Circumference is : ",circumference)
#     else:
#         print("Invalid Input")

# radius=float(input("Enter the radius of circle : "))
# char=input("Enter your choice (a or c) ")

# function(radius,char)

# Task 15: Write a function which takes 5 arguments and print their average. Call this function.

# def avg_calc(a,b,c,d,e):
#     average=(a+b+c+d+e)/5
#     print(average)

# avg_calc(1,2,3,4,5)

# Task 16: Write two functions add and multiply with five arguments and default values. These functions display result.

# def add(a,b,c,d=4,e=5):
#     s=a+b+c+d+e
#     print("Sum of numbers is ",s)

# add(1,2,3)

# def mul(a,b,c,d,e=9):
#     m=a*b*c*d*e
#     print("Multiplication of numbers is : ",m)

# mul(1,2,3,4)

# Task 17: Write a program to create a function show_employee() using the following conditions.
# •	It should accept the employee’s name and salary and display both.
# •	If the salary is missing in the function call then assign default value 9000 to salary

# def show(name,salary=9000):
#     print("The name of the emloyee is : ",name)
#     print("The salary of the employee is : ",salary)

# show("Aiza")

# Task 18: Write a program to create a function show_details() using the following conditions.
# •	It should accept the employee’s name and salary and display both
# •	If the salary is greater than 90000 then it shows the designation as Manager
# •	If salary is less than 90000 then it shows the designation as Worker

def show(name,salary):
    print("The name of the emloyee is : ",name)
    print("The salary of the employee is : ",salary)
    if(salary>=90000):
        print("----Manager----")
    elif(salary<90000):
        print("----Worker----")


show("Aiza",100000)
show("Areeba",50000)