from ecomm import (
    ProductDAO,
    Product,
    Invoice,
    Payment,
    Notification
)

class OrderFacade:
    def __init__(self):
        self.product_dao: ProductDAO = ProductDAO()
        self.invoice: Invoice = Invoice()
        self.payment: Payment = Payment()
        self.notification: Notification = Notification()
    
    def create_order(self, pid: int):
        product: Product = self.product_dao.get_product(pid)
        self.payment.make_payment(product)
        self.invoice.generate_invoice()
        self.notification.send_notification()
