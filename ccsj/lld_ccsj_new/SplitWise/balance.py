class Balance:
    def __init__(self):
        self.amount_owe: float = 0
        self.amount_get_back: float = 0
    
    def get_amount_get_back(self):
        return self.amount_get_back
    
    def set_amount_get_back(self, amount):
        self.amount_get_back = amount
    
    def get_amount_owe(self):
        return self.amount_owe
    
    def set_amount_owe(self, amount):
        self.amount_owe = amount
