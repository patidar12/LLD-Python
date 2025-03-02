from order_management.payment import PaymentMode

class Payment:
    def __init__(self, payment_mode: PaymentMode):
        self.payment_mode: PaymentMode = payment_mode

    def make_payment(self):
        return self.payment_mode.make_payment()
