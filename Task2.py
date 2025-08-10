#Task 8: Ask the user to enter his subject marks. Find his grade in that subject according to these conditions.

marks=int(input("Enter your marks : "))
if(marks>=90):
    print("Your Grade is A+ ")
elif(marks>=85 and marks<=89.9):
    print("Your Grade is A ")
elif(marks>=80 and marks<=84.9):
    print("Your Grade is A- ")
elif(marks>=75 and marks<=79.9):
    print("Your Grade is B+ ")
elif(marks>=71 and marks<=74.9):
    print("Your Grade is B ")
elif(marks>=68 and marks<=70.9):
    print("Your Grade is B- ")
elif(marks>=64 and marks<=67.9):
    print("Your Grade is C+ ")
elif(marks>=61 and marks<=63.9):
    print("Your Grade is C ")
elif(marks>=58 and marks<=60.9):
    print("Your Grade is C+ ")
elif(marks>=54 and marks<=57.9):
    print("Your Grade is D+ ")
elif(marks>=50 and marks<=53.9):
    print("Your Grade is D ")
else:
    print("Your Grade is F ")

# Task 9: User will enter his weight in Kilograms and height in meters (1 M=3.23 Feet). Calculate the BMI of the user and display following: 

weight=int(input("Enter your weught in Kilometers : "))
Height=int(input("Enter your height in Meters : "))
H2=(Height*Height)
BMI=(weight/H2)
print("Your BMI is : ",BMI)    
if(BMI<18.5):
    print("You are underweigt")
if(BMI>=18.5 and BMI<=24.9):
    print("You are Normal")
if(BMI>=25 and BMI<=29.9):
    print("You are Overweight")
if(BMI>30):
    print("You are Obese")

