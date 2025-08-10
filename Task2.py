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
    
