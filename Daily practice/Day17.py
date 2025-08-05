# File handling practice questions

# 1.
with open("C:\\Users\\MS\\Desktop\\info.txt") as file:
    data=file.read()
    print(data)

# 2.
with open("C:\\Users\\MS\\Desktop\\Story.txt") as f:
    data=f.read()
    print(data)
    words=data.split()
    print(words)
    print("The total words in the file are : ",len(words))

# 3.
f=open("C:\\Users\\MS\\\Desktop\source.txt")
data=f.read()
f=open("copy.txt","w") 
s=f.write(data)
print(s)

# 4.
f= open("even_no.txt","w") 
for i in range(1,51):
    if i%2==0:
        print(i)
        f.write(str(i)+"\n")
    i+=1
    

# 5.
data=input("Enter a sentence : ")
with open("C:\\Users\\MS\\Desktop\\source.txt","a") as f:
    file=f.write(data)


    
    
    




