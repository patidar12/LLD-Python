# pin, bancacount, expiredate, cvv

from bank_account import BankAccount
from datetime import datetime

class Card:
    def __init__(self, bank_account: BankAccount):
        self.bank_account: BankAccount = bank_account
        self.expire_date: datetime  = datetime(2026, 5, 23)
        self.cvv: int = 536
        self.pin: int = 543617

