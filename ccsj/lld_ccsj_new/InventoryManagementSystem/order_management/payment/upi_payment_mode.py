from payment import PaymentMode

class UPIPaymentMode(PaymentMode):

    def make_payment(self):
        return True