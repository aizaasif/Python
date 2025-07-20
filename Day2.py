#Indexing
string="aiza_asif"
print(string[2])
print(string[0])
print(string[4])
print(string[0:len(string)])
#Negative indexing 
print(string[-4:-2])
#string Functions
str="my name is Aiza Asif"
print(str.endswith("Aiza Asif"))
str=str.capitalize()
print(str)
print(str.replace(" name is", "self"))
str=str.capitalize()
print(str)
print(str.find("a"))
print(str.find("Q"))
print(str.count("a"))
print(str.count("A"))
print(str.count("Name"))

# Input user first name and find its length
firstname=input("Enter your First name : ")
print("Your first name is ",firstname)
length=(len(firstname))
print("The length of your name is  ",length)

#
str="The price of this book is 10$. If you want to purchase that book then you must have to pay 10$."
print(str.count("$"))








