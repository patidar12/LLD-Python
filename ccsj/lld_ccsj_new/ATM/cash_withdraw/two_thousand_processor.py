from atm import Atm
from cash_withdraw.withdraw_processor import CashWithdrawProcessor

class TwoThousandProcessor(CashWithdrawProcessor):
    
    def withdraw(self, atm: Atm, amount):
        required = amount//2000
        remaining = amount%2000
        if atm.get_two_thousand_notes() >= required:
            if remaining:
                super().withdraw(atm, remaining)
            atm.deduct_two_thousand_balance(required)
        else:
            two_thousand_notes = atm.get_two_thousand_notes()
            remaining = remaining + ((required-two_thousand_notes) * 2000)
            super().withdraw(atm, remaining)
            atm.deduct_two_thousand_balance(two_thousand_notes)
