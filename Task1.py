# Task 1: Ask the user to enter a value in miles and convert it in kilo meters (1 kilometer=0.6213 Mile).

value=int(input("Enter a value in miles : "))
km=value*0.6213
print(f" {value} miles = {km} kilometers ")

#Task 2: Given an equation y=ax3+ax2+x-7. Input the values of a and x from user and display the value of y on screen.

a=int(input("Enter value of a : "))
x=int(input("Enter value of x : "))
y=(a*x**3)+(a*x**2)+(x-7)
print("The value of Y is : ",y)

#Task 3: Write a program that reads a Celsius degree from the console and converts it to Fahrenheit and displays the result.

cel=int(input("Enter value in celcius : "))
far=(cel*9/5)+32
print(f"{cel} celcius = {far} fahrenheit")

#Task 4: Write a program that reads in the radius and length of a cylinder and computes the area and volume. 		( area = radius * radius * π )	( volume = area * length )
radius=int(input("Enter radius of a cylinder : "))
length=int(input("Enter Length of cylinder : "))
area=radius*radius*3.14
volume=area*length
print("Area of cylinder is : ",area)
print("Volume of cylinder is : ",volume)

# Task 5: Output the value of X using the below given equation. Input the value of n from user.
n=int(input("Enter the value of n : "))
a=((n*n)+8)*2
x=(n+a)*3
print("The value of x is ",x)

#Task 6: Input the values of a, b, c and d. Verify that the inputted values satisfy the below given equation or not.
import math
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
d=int(input("Enter the value of d : "))
LHS=(a/b)+(c/d)
RHS=((a*d)+(b*c))/(b*d)
print(LHS)
print(RHS)
if math.isclose(LHS, RHS):
    print("Hence proved that LHS=RHS")
else:
    print("LHS!=RHS")

#Task 7: Output the value of ‘x’ using the below given equation. Analyze and input the values to be inputted.
import math
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
p=(b*b)-(4*a*c)
r=math.sqrt(p)
q=(2*a)
x=(-b+r)/q
print("The value of x is : ",x)




