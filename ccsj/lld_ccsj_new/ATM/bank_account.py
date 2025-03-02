from enums import AccountType

class BankAccount:
    def __init__(self, account_no, account_type: AccountType, balance = 0):
        self.balance = balance
        self.acc_no = account_no
        self.acc_type: AccountType = account_type
    
    def deduct_balance(self, amount):
        self.balance -= amount

    def add_balance(self, amount):
        self.balance += amount
