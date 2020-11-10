from random import randint

class BankAccount:
    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = 192840982
        self.balance = float(0)

    def deposit(self):
        amount = float(input("Enter amount of money you want to deposit:\n"))
        self.balance += amount
        print(f"You deposited {amount}\n")

    def withdraw(self):
        amount = float(input("Enter amount of money you want to withdraw:"))
        if amount > self.balance:
            print("Insufficient funds\n")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"You have withdrawn {amount}\n")
        
    def get_balance(self):
        print(f"Your balance: {self.balance}\n")
        return self.balance
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        print(f"Interest earned: {interest}")
    def print_receipt(self):
        print(self.full_name)
        print(f"Account Number {self.account_number}")
        print(f"Routing Number {self.routing_number}")
        print(f"Balance {self.balance}")
#Three accounts
account1 = BankAccount("Sergio", randint(00000000,99999999))
account2 = BankAccount("John", randint(00000000,99999999))
account3 = BankAccount("Tom", randint(00000000,99999999))

# For testing!!
BankAccount.deposit(account1)
BankAccount.withdraw(account1)
BankAccount.get_balance(account1)
BankAccount.add_interest(account1)
BankAccount.print_receipt(account1)
