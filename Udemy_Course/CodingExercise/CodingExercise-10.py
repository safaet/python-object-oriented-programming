class BankAccount:
    
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds available.")
        else:
            self.balance -= amount
        

class CheckingAccount(BankAccount):
    
    def __init__(self, number, balance, overdraft_limit):
        BankAccount.__init__(self, number, balance)
        self.overdraft_limit = overdraft_limit
        
    # Write your code below:
    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            print("Not enough funds available.")
        else:
            self.balance -= amount

checking_account = CheckingAccount("4552 2325 3566 3423", 4500, 500)