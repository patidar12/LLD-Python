from payment_flow import PaymentFlow

class PaymentToFriend(PaymentFlow):
    def validate_request(self):
        print("Validating request for pay to firend")

    def debit_amount(self):
        print("Amount debidate using pay to firend")
    
    def calculate_fees(self):
        print("0 percent fees")
    
    def credit_amount(self):
        print("Same amount credited to friend")