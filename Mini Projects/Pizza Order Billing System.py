# dictionary
data={
    "chicken_pizza":500,
    "BBQ_pizzza":700,
    "MalaiBoti_Pizza":900,
    "Margherita":1200,
    "Pepperoni":1500
}

pizzaname=None
quantity=0

# Intro Function
def intro():
    print("          Welcome to 🍕Pizza Hub🍕")
    print("          Press 1 to check Menu")
    print("          Press 2 to order")
    print("          Press 3 to view bill")
    print("          Press 4 to exit")

# Menu funtion
def Menu():
    print("---------------MENU---------------\n")
    print("     1.chicken_pizza----Price-->500")
    print("     2.BBQ_pizzza-------Price-->700")
    print("     3.MalaiBoti_Pizza--Price-->900")
    print("     4.Margherita-------Price-->1200")
    print("     5.Pepperoni--------Price-->1500")



# Order Function
def order():
    pizzaname=input("Enter the name of the pizza you want to order : ")
    quantity=int(input("Enter quantity : "))
    if pizzaname in data:
        print("✅ Your Order is placed")
    else:
        print("Invalid Input ")
    return pizzaname, quantity

# Bill Function
def bill(pizzaname,quantity):
    print("The details of your order are : ")
    print(f"{pizzaname}")
    print(f"--> RS.{data[pizzaname]}")
    print(f"Quantity: {quantity}")
    if(quantity==1):
        print(f"Total is---> {data[pizzaname]}")
    elif(quantity>1):
        total=data[pizzaname]*quantity
        print(f"Total is---> {total}")

# Exit Function
def Exit():
    print("   Exited    ")

intro()
while True:
    choice=int(input("Enter---> "))
    if choice==1:
        Menu()
    if choice==2:
        pizzaname,quantity=order()
    if choice==3:
        bill(pizzaname,quantity)
    if choice==4:
        Exit()
        break