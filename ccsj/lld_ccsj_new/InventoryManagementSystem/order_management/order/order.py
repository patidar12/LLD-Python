from typing import List, Dict

from catalog import Address
from catalog import (
    Product,
    ProductCategory
)
from catalog.warehouse import WareHouse
from order_management.invoice import Invoice
from order_management.payment import Payment
from order_management.order import OrderStatus
from user import User
from payment import (
    Payment,
    PaymentMode,
    UPIPaymentMode,
    CardPaymentMode
)

class Order:
    def __init__(self, user: User, warehouse: WareHouse):
        self.user: User = user
        self.category_vs_count_map: Dict[int, int] = user.get_user_cart().get_cart_items()
        self.warehouse: WareHouse = warehouse
        self.delivery_address: Address = user.address
        self.order_status: OrderStatus = OrderStatus.INPROGRESS
        self.invoice: Invoice = Invoice()
        self.invoice.generate_invoice(self)
    
    def checkout(self):
        # updating the inventory
        self.warehouse.remove_item_from_inventory(self.category_vs_count_map)

        # making payment
        is_payment_success: bool = self.make_payment(UPIPaymentMode())

        # make cart empty
        if is_payment_success:
            self.user.get_user_cart().empty_cart()
            self.order_status = OrderStatus.DELIVERED
        else:
            self.warehouse.add_items_to_inventory(self.category_vs_count_map)
            self.order_status = OrderStatus.CANCELLED


    def make_payment(payment_mode: PaymentMode):
        payment: Payment = Payment(payment_mode)
        return payment.make_payment()

    def generate_order_invoice(self):
        self.invoice.generate_invoice(self)
