from bill import Bill

class Payment:
    def __init__(self, bill: Bill):
        self.bill: Bill = bill
    
    def pay_bill(self):
        print(f"Bill payment of rs{self.bill.total_bill_amount} is Done\nThank You...")
        self.bill.is_bill_paid = True
