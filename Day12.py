# While Loop

# 1-100
i=1
while i<=100:
    print(i)
    i+=1

# 100-1
i=100
while i>=1:
    print(i)
    i-=1

#Multiplication of number n
num=int(input("Enter a number : "))
i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i+=1

#print the elements
num=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(num):
    print(num[i])
    i+=1

# Search for a number
num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number : "))
i=0
while i < len(num):
    if(num[i]==x):
        print("Number exsist at index ",i) 
        break
    else:
        print("--")     
    i+=1 

# Continue
i = 1
while i <= 10:
     if(i%2==0):
        i+=1
        continue
     print(i)
     i+=1

#
i=1
while(i<=10):
    if(i==5):
        i+=1
        continue
    print(i)
    i+=1

#
i=1
while i<=10:
    if(i==7):
        print(i)
        break
    print(i)
    i+=1
 
num=[1,2,-3,-4,5,6,-7,-8,9,10]
list=[int(input("Enter a list of numbers : "))]
i=0
while i<len(num):
    if(num[i]>0):
        i+=1
        continue
    print(num[i])
    i+=1

# Taking a list from the user
num=list(map(int,input("Enter numbers seprated by space : ").split()))
print("The list of numbers is ",num)

# Printing multiples of 7
i=7
while i<=100:
    if(i%7!=0):
        i+=1
        continue
    print(i)
    i+=1

# 1st even no in a list
# num=list(map(int,input("Enter a list of numbers ").split()))
# print(num)
num=[1,2,3,4,5]
i=0
while i<len(num):
    if(num[i]%2==0):
        print(num[i])
        break
    i+=1

# for loop
num=tuple(map(int,input("Enter a list of numbers ").split()))
print(num)
for var in num:
    print(var)

num=[1,4,9,16,25,36,49,64,81,100]
for var in num:
    if(var==16):
        print("16 found")
        print(var)
    else:
        print(var)
        
num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number : "))
for var in num:
    if(var==x):
        print("Number find in the list ")
        break
    else:
        print("Finding the number : ")
    
# print even numbers using for loop
for i in range(2,101,2):
    print(i)

# print odd numbers using for loop
for i in range(1,10,2):
    print(i)

for i in range(100,0,-1):
    print(i)

n=5
for i in range(1,11):
    print(n,"*",i,"=",n*i)


i=1
sum=0
while i <= 5:
    sum+=i
    i+=1
print(sum)

fac=1
i=1
while i<=5:
    fac*=i
    i+=1
print(fac)

fac=1
for i in range(1,6):
    fac*=i
    i+=1
print(fac)
    

    
    



        


    




