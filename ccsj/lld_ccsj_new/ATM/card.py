from datetime import datetime
from bank_account import BankAccount

class Card:
    def __init__(self, bank_account: BankAccount):
        self.bank_account = bank_account
        self.cvv = 899
        self.expiry_date = datetime(2030, 5, 5).date()
        self.pin = 5050
    
    def verify_pin(self, pin):
        if pin != self.pin:
            return False
        print("Pin verified succesfully...")
        return True
