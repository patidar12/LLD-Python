from atm import Atm
from card import Card
from atm_states.has_card import HasCardState

class IdleState:
    def __init__(self):
        print("ATM in Idle state now!")

    def insert_card(self, atm: Atm, card: Card):
        print("Card inserted!")
        atm.set_state(HasCardState())
