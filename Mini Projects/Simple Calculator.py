
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
operator=input("Enter operator : ")

def sum(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def Mul(a,b):
    print(a*b)

def div(a,b):
    if(b==0):
        print("Error cant divide ")
    else:
        print(a/b)
    

if(operator=="+"):
    sum(a,b)
elif(operator=="-"):
    sub(a,b)
elif(operator=="*"):
    Mul(a,b)
elif(operator=="/"):
    div(a,b)
elif(operator=="/" and b==0):
    print("Error can't divide")
else:
    print("Invalid input :(")

