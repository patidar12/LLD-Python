# balance, acc_no, acount_type
from account_type import AccountType

class BankAccount:
    def __init__(self, acc_no: str, acc_type: AccountType, balance: float = 0):
        self.acc_no: str = acc_no
        self.acc_type: AccountType = acc_type
        self.balance: float = balance
    
    def add_balance(self, amount: float):
        self.balance += amount
    
    def deduct_balance(self, amount: float):
        self.balance -= amount
