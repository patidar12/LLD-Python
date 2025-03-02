from typing import List

from catalog import Address
from cart import Cart

class User:
    def __init__(self, uid: int, name: str, address: Address):
        self.uid: int = uid
        self.name: str = name
        self.address: Address = address
        self.cart_details: Cart = None
        self.order_ids: List[int] = []
    
    def set_cart_details(self, cart: Cart):
        self.cart_details = cart
    
    def add_order_id(self, order_id: int):
        self.order_ids.append(order_id)
    
    def get_user_cart(self):
        return self.cart_details
