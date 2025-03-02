from atm import Atm
from card import Card
from atm_states.selection_operation import SelecOperationState

class HasCardState:

    def __init__(self):
        print("ATM in HasMoney state now!")
    
    def authentication(self, atm: Atm, card: Card, pin: int):
        if card.pin != pin:
            print("Authentication failed. Please provide correct pin.")
            self.exit(atm)
            from atm_states.idle_state import IdleState
            atm.set_state(IdleState())
            return
        atm.set_state(SelecOperationState())

    def exit(self, atm):
        print("Atm exit.. returning Card!")
        self.return_card()

    def return_card(self):
        print("Card returned")
