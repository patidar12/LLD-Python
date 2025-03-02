from user import User

class Split:
    def __init__(self, user: User, amount_owe: float):
        self.user: User = user
        self.amount_owe: float = amount_owe

    def get_amount_owe(self):
        return self.amount_owe
    
    def get_user(self):
        return self.user
