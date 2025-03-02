from typing import List, Dict

from order_management.order import (
    Order,
    OrderStatus
)
from user import User
from catalog.warehouse import WareHouse

class OrderController:
    def __init__(self):
        self.order_list: List[Order] = []
        self.user_id_vs_orders: Dict[int, List[Order]] = {}
    
    def create_new_order(self, user: User, warehouse: WareHouse):
        order = Order(user, warehouse)
        self.order_list.append(order)

        if user.uid in self.user_id_vs_orders:
            self.user_id_vs_orders[user.uid].append(order)
        else:
            self.user_id_vs_orders[user.uid] = [order]
        return order
    
    # remove order
    def remove_order(self, order: Order):
        # remove order capability goes here
        pass
    
    def get_orders_by_customer_id(self, user_id: int):
        return self.user_id_vs_orders.get(user_id)
    
    def get_order_by_order_id(self, order_id: int):
        # for this we can use one more map of order_id_vs_order
        return None
