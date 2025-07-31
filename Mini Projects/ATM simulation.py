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


for i in range(3):
        username=input("Enter your username : ")
        pin=input("Enter your pin : ")
        if username in data and data[username]["pin"]==pin:
            print("Login successful ")
        else:
             print(f"Try again attempts left {i}")
else:
    print("Account Locked")


        



        
