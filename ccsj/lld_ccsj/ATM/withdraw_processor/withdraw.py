class Withdraw:
    def __init__(self, next_processor):
        self.next_processor: Withdraw = next_processor
    
    def withdraw(self, atm, amount):
        if self.next_processor:
            self.next_processor.withdraw(atm, amount)
