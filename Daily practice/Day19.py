# Account Class

class Account:


    # Paramitarized Constructor 
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance

    
    # Debit Method
    def debit(self):
        d_amo=int(input("Enter amount you want to debit : "))
        self.balance=self.balance-d_amo
        print("Debit Successfull✅")
        print("balance is ",self.balance)
    
    # Credit Method
    def credit(self):
        c_amo=int(input("Enter amount you want to credit : "))
        self.balance=self.balance+c_amo
        print("Credit Successfull✅")
        print("balance is ",self.balance)
    
    # Balance method
    def printing(self):
        print(f"The balance in Account_No {self.account_no} is ",self.balance)
    
account1=Account("123",5000)
account1.debit()
account1.credit()
account1.printing()
    
    

    

    