from atm_states.state import State
from atm import Atm
from card import Card
from atm_states.selection_operation import SelectOperationState
from atm_states.idle import IdleState

class HasCardState(State):

    def authenticate_pin(self, atm: Atm, card: Card, pin):
        if not card.verify_pin(pin):
            print("Invalid pin...")
            self.exit(atm)
        print("pin authenticated succesfully...")
        atm.set_state(SelectOperationState())
    
    def exit(self, atm: Atm):
        self.return_card()
        atm.set_state(IdleState())

    def return_card(self):
        print("Card returned...")
