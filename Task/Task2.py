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

# weight=float(input("Enter your weught in Kilograms : "))
# Height=float(input("Enter your height in Meters : "))
# H2=(Height*Height)
# BMI=(weight/H2)
# print("Your BMI is : ",BMI)    
# if(BMI<18.5):
#     print("You are underweight")
# elif(BMI>=18.5 and BMI<=24.9):
#     print("You are Normal")
# elif(BMI>=25 and BMI<=29.9):
#     print("You are Overweight")
# elif(BMI>30):
#     print("You are Obese")

# Task 10: Write a program to display "NTU" if a number entered by user is a multiple of five , otherwise print "DCS".

# no=int(input("Enter a number : "))
# if(no%5==0):
#     print("NTU")
# else:
#     print("DCS")

# Task 11: Write a program to check whether the last digit of a number (entered by user) is divisible by 3 or not.

# no=int(input("Enter a number must contains more than 1 digit : "))
# last=no%10
# if(last%3==0):
#     print(f"Number {last} is divisible by 3")
# else:
#     print(f"Number {last} is not divisible by 3")

# Task 12: Implement a currency converter which ask the user to enter value in Pak Rupees and convert in following: 

# value=int(input("Enter a value in PKR :"))
# print("1.Australian Dollar")
# print("2.China Yuan")
# print("3.Euro")
# print("4.Qatri Riyal")
# print("5.Saudi Riyal")
# print("6.UAE Dirham")
# print("7.UK pound")
# print("8.Us Dollar")
# choice=int(input("Enter your choice, only enter number "))
# if (choice==1):
#     AD=(value/102.6)
#     print(f"{value} PKR = {AD} Australian Dollar")
# elif (choice==2):
#     CY=value/22
#     print(f"{value} PKR = {CY} China Yuan")
# elif (choice==3):
#     E=value/168.15
#     print(f"{value} PKR = {E} Euro")
# elif (choice==4):
#     QR=(value/42.2)
#     print(f"{value} PKR = {QR} Qatri Riyal")
# elif (choice==5):
#     SR=value/40.95
#     print(f"{value} PKR = {SR} Saudi Riyal")
# elif (choice==6):
#     UAED=value/42.2
#     print(f"{value} PKR = {UAED} UAE Dirham")
# elif (choice==7):
#     UKP=value/198.15
#     print(f"{value} PKR = {UKP} UK Pound")
# elif (choice==8):
#     USD=value/154
#     print(f"{value} PKR = {USD} US Dollar")










