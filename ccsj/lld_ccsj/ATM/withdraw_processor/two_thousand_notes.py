from atm import Atm
from withdraw_processor.withdraw import Withdraw

class TwoThousandNotes(Withdraw):

    def withdraw(self, atm: Atm, amount):
        print("taking two thousand notes...")
        required = amount//2000
        balance = amount%2000
        if required <= atm.get_two_thousand_notes():
            atm.deduct_two_thousand_balance(required)
        else:
             balance = (amount - (atm.get_two_thousand_notes() * 2000))
             atm.deduct_two_thousand_balance(atm.get_two_thousand_notes())
        if balance:
            super().withdraw(atm, balance)
