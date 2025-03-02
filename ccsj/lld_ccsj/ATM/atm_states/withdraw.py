from atm import Atm
from card import Card
from withdraw_processor.five_hundrared_notes import FiveHundraredNotes
from withdraw_processor.hundred_rs_notes import HundredRsNotes
from withdraw_processor.two_thousand_notes import TwoThousandNotes

class WithdrawState:
    
    def withdraw_operation(self, atm:Atm, card: Card, ammount: int):
        if atm.balance < ammount:
            print("Insufficient fund in atm machine!")
            self.exit(atm)
            return
        if card.bank_account.balance < ammount:
            print("Insufficient fund in card!")
            self.exit(atm)
            return
        card.bank_account.deduct_balance(ammount)
        withdra_processor = TwoThousandNotes(FiveHundraredNotes(HundredRsNotes(next_processor=None)))
        withdra_processor.withdraw(atm, ammount)
        self.exit(atm)
        print("Transaction completed!!!")

    def exit(self, atm: Atm):
        print("Atm exit.. returning Card!")
        self.return_card()
        from atm_states.idle_state import IdleState
        atm.set_state(IdleState())

    def return_card(self):
        print("Card returned")
