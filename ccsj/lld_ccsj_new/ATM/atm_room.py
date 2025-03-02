from atm_states.state import State
from atm import Atm
from user import User

class AtmRoom:
    def __init__(self):
        self.atm: Atm = None
        self.user: User = None