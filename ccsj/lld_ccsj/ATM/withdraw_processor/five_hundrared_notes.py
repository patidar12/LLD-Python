from atm import Atm
from withdraw_processor.withdraw import Withdraw

class FiveHundraredNotes(Withdraw):

    def withdraw(self, atm: Atm, amount):
        print("taking five hundred notes...")
        required = amount//500
        balance = amount%500
        if required <= atm.get_five_hundread_notes():
            atm.deduct_five_hundread_balance(required)
        else:
             balance = (amount - (atm.get_five_hundread_notes() * 500))
             atm.deduct_five_hundread_balance(atm.get_five_hundread_notes())
        if balance:
            super().withdraw(atm, balance)
