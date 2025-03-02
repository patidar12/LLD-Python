from atm_states.state import State
from atm import Atm
from card import Card
from atm_states.idle import IdleState

class CheckBalanceState(State):
    def check_balance(self, atm: Atm, card: Card):
        print(f"Total Amount: {card.bank_account.balance}")
        self.exit(atm)

    def exit(self, atm: Atm):
        self.return_card()
        atm.set_state(IdleState())

    def return_card(self):
        print("Card returned...")