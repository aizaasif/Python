import random
secret_no=random.randint(1, 10)

i=1
while(i<=3):
    no=int(input("Enter a number you have only 3 attempts "))
    if(secret_no==no):
        print("Congratulations! you have guesed the right number ")
        break
    elif(no>secret_no):
        print("Your guesed number is high than the actual number ")
    else:
        print("Your guesed number is low than the actual number ")
    i+=1
    if i > 3 and secret_no != no:
        print(f"Game Over! The correct number was: {secret_no}")



        
        
    
        



    
    