from typing import Dict

from catalog import Invenotry
from catalog import Address

class WareHouse:
    def __init__(self, address: Address):
        self.invnetory: Invenotry = None
        self.address: Address = address
    
    def set_inventory(self, inventory: Invenotry):
        self.invnetory = inventory
    
    def remove_item_from_inventory(self, category_and_count_map: Dict[int, int]):
        self.invnetory.remove_items(category_and_count_map)
    
    def add_items_to_inventory(self, category_and_count_map: Dict[int, int]):
        # it will update the items in the inventory based upon product category.
        pass
