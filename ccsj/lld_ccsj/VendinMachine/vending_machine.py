from typing import List

from VendingStates.impl.idle_state import IdleState
from inventory import Invnetoy
from coin import Coin

class VendingMachine:
    def __init__(self):
        self.state = IdleState(self)
        self.inventory = Invnetoy(10)
        self.coins: List[Coin] = []
    
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
    
    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory: Invnetoy):
        self.inventory = inventory
    
    def set_coins(self, coins: List[Coin]):
        self.coins = coins

    def get_coins(self):
        return self.coins
