from atm import Atm
from cash_withdraw.withdraw_processor import CashWithdrawProcessor

class HundreadRsProcessor(CashWithdrawProcessor):
    
    def withdraw(self, atm: Atm, amount):
        required = amount//100
        remaining = amount%100
        if atm.get_hundread_notes() >= required:
            if remaining:
                super().withdraw(atm, remaining)
            atm.deduct_hundread_balance(required)
        else:
            two_thousand_notes = atm.get_hundread_notes()
            remaining = remaining + ((required-two_thousand_notes) * 100)
            super().withdraw(atm, remaining)
            atm.deduct_hundread_balance(two_thousand_notes)
