from atm_states.state import State
from atm import Atm
from card import Card
from atm_states.idle import IdleState
from  cash_withdraw import TwoThousandProcessor, FiveHundreadProcessor, HundreadRsProcessor

class WithDrawState(State):

    def withdraw_operation(self, atm: Atm, card: Card, ammount: int):
        if atm.balance < ammount:
            print("insufficient amount in atm...")
            self.exit(atm)
            return
        if card.bank_account.balance < ammount:
            print("insufficient amount in bank account...")
            self.exit(atm)
            return
        # chain of responsibility
        withoraw_processor = TwoThousandProcessor(
            FiveHundreadProcessor(
                HundreadRsProcessor(
                    None
                )
            )
        )
        withoraw_processor.withdraw(atm, ammount)
        card.bank_account.deduct_balance(ammount)
        self.exit(atm)

    def exit(self, atm: Atm):
        self.return_card()
        atm.set_state(IdleState())

    def return_card(self):
        print("Card returned...")