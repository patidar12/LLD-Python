from enums import ItemType

class Item:
    def __init__(self, item_type: ItemType, price):
        self.item_type: ItemType = item_type
        self.price = price