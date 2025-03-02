from typing import List

from item_shelf import ItemShelf

class Invnetoy:
    def __init__(self, item_count):
        self.inventory: List[ItemShelf] = [None] * item_count
    
    def get_inventory(self) -> List[ItemShelf]:
        return self.inventory

    def set_inventory(self, inventory: List[ItemShelf]) -> None:
        self.inventory = inventory
    
    def initial_empty_inventory(self):
        for item_code in len(101, 101 + self.inventory):
            space = ItemShelf()
            space.set_code(item_code)
            self.inventory[item_code-101] = space            

    def add_item(self, item, item_code):
        for item_shelf in self.inventory:
            if item_shelf.code == item_code:
                if item_shelf.is_sold_out():
                    item_shelf.item = item
                    item_shelf.set_sold_out(False)
                else:
                    raise Exception("Already item present, you can not add item here")

    def get_item(self, item_code):
        for item_shelf in self.inventory:
            if item_shelf.code == item_code:
                if item_shelf.is_sold_out():
                    raise Exception("Item already sold out!")
                else:
                    return item_shelf.item
        raise Exception("Invalid Item Code!")
    
    def update_sold_out_item(self, item_code):
        for item_shelf in self.inventory:
            if item_shelf.code == item_code:
                item_shelf.set_sold_out(True)
