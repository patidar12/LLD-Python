from atm import Atm
from withdraw_processor.withdraw import Withdraw

class HundredRsNotes(Withdraw):

    def withdraw(self, atm: Atm, amount):
        print("taking hundred rs notes...")
        required = amount//100
        balance = amount%100
        if required <= atm.get_hundread_notes():
            atm.deduct_hundread_balance(required)
        else:
             balance = (amount - (atm.get_hundread_notes() * 100))
             atm.deduct_hundread_balance(atm.get_hundread_notes())
        if balance:
            super().withdraw(atm, balance)
