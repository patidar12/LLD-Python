class Invoice:

    def __init__(self):
        self.total_item_price: float = 0.0
        self.total_tax: float = 0.0
        self.total_final_price: float = 0.0
    
    def generate_invoice(self, order):
        # it will compute and update the above details
        self.total_item_price = 200.00
        self.total_tax = 20.00
        self.total_final_price = 220.00

