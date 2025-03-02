from order_facade import OrderFacade

class OrderClient:
    def create_order(self):
        OrderFacade().create_order(123)

OrderClient().create_order()
