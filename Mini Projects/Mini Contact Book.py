Book={
    "aiza":"12345",
    "areeba":"11223",
    "amna":"56789",
    "bushra":"19023",
    "fatima":"45678",
    "maryam":"78458"
}
print("The mini contact book")
print(Book)

# Allow user to add new name and number
x=1
count=int(input("Enter number of users you want to add in the book "))
for i in range(count):
    print(f"          {x}          ")
    name=input("Enter name of a person : ")
    number=input("Enter number of a person : ")
    Book.update({name:number})
    x+=1
print("Now the book after updation is : ",Book)







