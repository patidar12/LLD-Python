from atm import Atm
from card import Card

class CheckBalanceState:
    
    def check_balance(self, atm: Atm, card: Card):
        print("Current Balance: ", card.bank_account.balance)
        self.exit(atm)
        from atm_states.idle_state import IdleState
        atm.set_state(IdleState())

    def exit(self, atm: Atm):
        print("Atm exit.. returning Card!")
        self.return_card()

    def return_card(self):
        print("Card returned")
