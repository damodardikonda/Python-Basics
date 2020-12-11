import sys
class Bank:

    BankName = 'DamodarBank'

    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def deposite(self , amount):
        self.balance = self.balance+amount
        print(" After Operation Amount is " , self.balance)


    def withdraw(self , amount):
        if self.balance < amount:
            print(" Lavdya tuzya gandit ahet ka paise kadhyla")
            sys.exit()
        else:
            self.balance = self.balance - amount
            print("Now amount is " , self.balance)


print("Welcome to Damodar Bank")
n = input("Enter your name" )
b = Bank( n, 10000)

while True:

       option = input("d - deposite\n w - Withdraw \n ")
       if option == 'd' or option == 'D':
           a = input(" Enter Amount ")
           a = int(a)
           b.deposite(a)

       elif option.lower() == 'w':
           a = input("Enter amount")
           a = int(a)
           b.withdraw(a)
