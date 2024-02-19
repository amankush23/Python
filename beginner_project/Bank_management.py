class bank:
    def __init__(self,account_number,account_holder,initial_balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.initial_balance = initial_balance
        print(f'congratulation!🥰')
        
    def deposit(self,ammount):
        self.ammount=ammount
        if ammount>0:
            self.initial_balance += ammount
            return f'Ammount after deposit: {self.initial_balance}😊'
        else:
            print("ammount is not valid!🥲")

    def withdraw1(self,ammount):
        if ammount > self.initial_balance:
            return "Not enough balance to withdraw!🥲"
        else:
            self.initial_balance -= ammount
            return f'Ammount after withdral: {self.initial_balance}'
    
    def check_bal(self):
        return f"Total Balance: {self.initial_balance}"

    def details(self):
        return f'''Account Number: {self.account_number}
Account_Holder_Name: {self.account_holder}
Initial_balance:{self.initial_balance}'''
        


# implement inheritance and polymorphism cncepts by extending the bank account system . create differenr types of acount (saving,checking)that inherit from a base bankaccount class . implement polymorphic methods and demonstarate their usage.

if __name__ == ('__main__'):
    class savingaccount(bank):
        def __init__(self,account_number,account_holder,interest_rate=0.02):
            super().__init__(account_number,account_holder,interest_rate)
            self.interst_rate = interest_rate
            

    class checkingaccount(bank):
        def __init__(self,account_number,account_holder,Initial_balance=0,overdraf_limit=100):
            super().__init__(account_number,account_holder,overdraf_limit)
            self.overdraf_limit = overdraf_limit
    
        def withdraw1(self,ammount):
            if ammount <= (self.balance +self.overdraf_limit):
                self.balance -= ammount
                print(f"Withdraw {ammount}.new balance {self.balance}")
            else:
                print("Insufficient funds overdraft limit reached")
    
        def add_interest(self):
            interest = self.initial_balance + self.interest_rate
            self.balance += interest
            print("interest added {interest},new balance {self.balance}")


cash=bank(123,'aman',10000)
print(cash.deposit(5000))
print(cash.withdraw1(8000))



# while True:
#     print('''Menu
#     1. Deposit
#     2.Withdraw
#     3.check_balance
#     4. Exit''')
#     choice=int(input("enter the choice 1/2/3/4: "))
#     if choice == 1:
#         deposit=int(input("enter the ammount to be deposit: "))
#         add=deposit + bank.initial_balance
        
#         print(add)
#     elif choice == 2:
#         withdraw=int(input("enter the withdrawl money: "))
#         sub= bank.initial_balance - withdraw
#         print(sub)
#     elif choice == 3:
#         print(bank.initial_balance)
#     else:
#         break
    
#main code

if __name__ == '__main__':
    savingaccount = savingaccount(account_number=123,account_holder='aman',initial_balance=1000)
    checkingaccount = checkingaccount(account_number=345,account_holder='Kartik',initial_balance=2000)

    #deposit
    
    savingaccount.deposit(200)
    savingaccount.check_bal()

    checkingaccount.deposit(200)
    checkingaccount.check_bal()

    #withdraw
    
    savingaccount.withdraw1(200)
    savingaccount.check_bal()

    checkingaccount.withdraw1(200)
    checkingaccount.check_bal()

    #add interest

    savingaccount.add_interest(200)
    savingaccount.check_bal()
