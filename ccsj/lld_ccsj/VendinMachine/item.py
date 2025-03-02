from item_type import ItemType

class Item:
    def __init__(self, item_type: ItemType, price: int):
        self.item_type: ItemType = item_type
        self.price: int = price
