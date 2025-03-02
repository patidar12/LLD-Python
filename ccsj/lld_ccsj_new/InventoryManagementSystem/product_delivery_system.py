from typing import List, Dict

from user import (
    User,
    UserController
)
from catalog.warehouse import (
    WareHouse,
    WareHouseController
)

from catalog.warehouse.strategy import WarehouseSelectionStrategy

from order_management.order import (
    Order,
    OrderController
)

from catalog import (
    Product,
    ProductCategory
)


class ProductDeliverySystem:

    def __init__(self, user_list: List[User], warehouse_list:  List[WareHouse] ):
        self.user_controller = UserController(user_list)
        self.warehouse_controller = WareHouseController(warehouse_list , None)
        self.order_controller = OrderController()

    # get user object
    def get_user(self, user_id: int):
        return self.user_controller.get_user_by_id(user_id)

    # get warehouse
    def get_warehouse(self, warehouse_selection_strategy: WarehouseSelectionStrategy):
        return self.warehouse_controller.select_warehouse(warehouse_selection_strategy)


    # get inventory
    def get_inventory(self, warehouse: WareHouse):
        return warehouse.invnetory


    # add product to cart
    def add_product_to_cart(self, user: User, product: ProductCategory, count: int):
        cart = user.get_user_cart()
        cart.add_item_to_cart(product.pcid, count)

    # place order
    def place_order(self, user: User, warehouse: WareHouse):
        return self.order_controller.create_new_order(user, warehouse)

    def checkout(self, order: Order):
        order.checkout()
