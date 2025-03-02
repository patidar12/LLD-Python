from atm import Atm
from cash_withdraw.withdraw_processor import CashWithdrawProcessor

class FiveHundreadProcessor(CashWithdrawProcessor):
    
    def withdraw(self, atm: Atm, amount):
        required = amount//500
        remaining = amount%500
        if atm.get_five_hundread_notes() >= required:
            if remaining:
                super().withdraw(atm, remaining)
            atm.deduct_five_hundread_balance(required)
        else:
            two_thousand_notes = atm.get_five_hundread_notes()
            remaining = remaining + ((required-two_thousand_notes) * 500)
            super().withdraw(atm, remaining)
            atm.deduct_five_hundread_balance(two_thousand_notes)
