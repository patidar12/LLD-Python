from typing import List

from item_shelf import ItemShelf

class Inventory:
    def __init__(self, item_count: int):
        self.inventory: List[ItemShelf] = [None] * item_count
        self.initial_empty_inventory()

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory
    
    def initial_empty_inventory(self):
        for item_code in range(101, 101+len(self.inventory)):
            space = ItemShelf()
            space.set_code(item_code)
            self.inventory[item_code-101] = space
    def add_item(self, item, item_code):
        for space in self.inventory:
            if space.code == item_code:
                if space.is_sold_out():
                    space.set_item(item)
                    space.set_sold_out(False)
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
