from typing import List
from enums import Coin
from inventory import Inventory

class VendingMachine:
    def __init__(self):
        from VendinState.impl.idle_state import IdleState
        self.state = IdleState(self)
        self.coins: List[Coin] = []
        self.inventory: Inventory = Inventory(10)

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
    
    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory: Inventory):
        self.inventory = inventory
    
    def set_coins(self, coins: List[Coin]):
        self.coins = coins

    def get_coins(self):
        return self.coins