from payment_flow import PaymentFlow

class PaymentToMerchent(PaymentFlow):
    def validate_request(self):
        print("Validating request for pay to mechent")

    def debit_amount(self):
        print("Amount debidate using pay to mechent")
    
    def calculate_fees(self):
        print("10 percent fees")
    
    def credit_amount(self):
        print("Amount after platform fee deduction credited")