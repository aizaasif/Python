# Dictionary
data={
    "user1":{
        "pin":"1234",
        "balance":5000
    },
    "user2":{
        "pin":"1122",
        "balance":10000
    },
    "user3":{
        "pin":"9990",
        "balance":7000
    }
    }

# check balance function
def check_balance(username):
    print("Your balance is : ",data[username]["balance"])

#Deposit Function
def deposit(username):
        deposit_amount=int(input("Enter Amount you want to deposit : "))
        data[username]["balance"]=data[username]["balance"]+deposit_amount
        print("----------Amount Deposited Successfully----------")
        print("Your balance after Depositing ",deposit_amount,"is ",data[username]["balance"])
        
# withdraw Function
def withdraw(username):  
    withdraw_amount=int(input("Enter Amount you want to withdraw: "))
    if withdraw_amount<data[username]["balance"]:
        data[username]["balance"]=data[username]["balance"]-withdraw_amount
        print("Amount withdrawed successfully : ")
        print("Your balance after withdraw ",withdraw_amount,"is ",data[username]["balance"]) 
    else:
        print("You are trying to withdraw amount more than your actual balance")    

# Exit Function
def exiting():
    print("          Process Terminated          ")

# Login Functionality
def login():  
    for i in range(1,4):
        username=input("Enter your username : ")
        pin=input("Enter your pin : ")
        if username in data and data[username]["pin"]==pin:
            print("----------Login successful----------")
            menu(username)
            break
        else:
            print(f"Attempts Left {3-i}")
    else:
        print("Account Locked")
        exit()

# menu and user input function
def menu(username):
    i=1
    while True:
        print("------------------MENU------------------")
        print("       Press 1 to Check Balance         ")
        print("       Press 2 to Deposit               ")
        print("       Press 3 to withdraw              ")
        print("       Press 4 to Exit                  ")
        userchoice=int(input("Now Enter ---> your choice "))
        if userchoice==1:
            check_balance(username)
        if userchoice==2:
            deposit(username)
        if userchoice==3:
            withdraw(username)
        if userchoice==4:
            exiting()
            break   
    i+=1
    
login()


            
     







        



        
