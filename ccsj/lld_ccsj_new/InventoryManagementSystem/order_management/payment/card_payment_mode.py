from payment import PaymentMode

class CardPaymentMode(PaymentMode):

    def make_payment(self):
        return True