dict={}

i=1
while(i<=2):
    key=input(f"{i}--> Enter your username : ")
    passwords=input(f"{i}--> Enter your password : ")
    dict.update({key:passwords})
    i+=1
print("The usernames and passwords of the user are : ",dict)

print("------------Login system------------")
username=input("Enter your username first : ")
if(username in dict):
    password=input("Enter your password to login :")
    if(dict[username]==password):
        print("Correct password! login successfull:)")
    else:
        print("Wrong Password")
else:
    print("Invalid user!")
