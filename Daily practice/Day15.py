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