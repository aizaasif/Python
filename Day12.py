# While Loop

# 1-100
i=1
while i<=100:
    print(i)
    i+=1

# 100-1
# i=100
# while i>=1:
#     print(i)
#     i-=1

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
 


