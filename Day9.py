book_details={}

b1_title=input("Enter the title of 1st book : ")
b1_price=int(input("Enter the price of 1st book : "))
book_details.update({b1_title:b1_price})

b2_title=input("Enter the title of 2nd book : ")
b2_price=int(input("Enter the price of 2nd book : "))
book_details.update({b2_title:b2_price})

b3_title=input("Enter the title of 3rd book : ")
b3_price=int(input("Enter the price of 3rd book : "))
book_details.update({b3_title:b3_price})
print(book_details)

username=input("Enter your name : ")
userbook=input("Enter your fav book : ")

if userbook in book_details:
    print("The book is avalible in the store : ")
    price = book_details[userbook]
    print("The price of your book is : ",price)
    if price>500:
       discount=price*0.10
       newprice=price-discount
       print("Since the price of your book is greater than 500 so you are getting 10 percent discount Now the price of your book after discount is: git ",newprice)
else:
    print("Not available")

