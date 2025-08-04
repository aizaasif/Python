# file handling

# Opening a file
f=open("C:\\Users\\MS\\Desktop\\File.txt")
# Reading a file
data=f.read()
print(data)
# Closing a file
f.close()

# Opening,Reading,closing a file in the same directory
f=open("E:\\Python\\Daily practice\\text.txt","r")
data=f.read()
print(data)
f.close()

# Read a single line
f=open("C:\\Users\\MS\\Desktop\\File.txt")
data=f.read()
print(data)
line1=f.readline()
line2=f.readline()
line3=f.readline()
print(line1)
print(line2)
print(line3)

f=open("C:\\Users\\MS\\Desktop\\File.txt","w")
data=f.write("My name is aiza asif\nI am 19 years old")
print(data)

#We can also read a python File
f=open("E:\\Python\\Daily practice\\Day1.py")
data=f.read()
print(data)

f=open("C:\\Users\\MS\\Desktop\\File.txt","a")
data=f.write("\nappend")
print(data)

# With syntax
with open("C:\\Users\\MS\\Desktop\\File.txt","a") as f:
    f.write("\nI have appended")

# removing a file
import os
os.remove("C:\\Users\\MS\\Desktop\\File.txt")

    






