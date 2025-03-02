from atm_states.state import State
from atm import Atm
from atm_states.has_card import HasCardState
class IdleState(State):

    def insert_card(self, atm: Atm, card):
        print("Card inserted")
        atm.set_state(HasCardState())
