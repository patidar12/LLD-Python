from atm import Atm

class CashWithdrawProcessor:
    def __init__(self, next_processor):
        self.next_processor: CashWithdrawProcessor = next_processor
    
    def withdraw(self, atm: Atm, amount):
        if self.next_processor:
            self.next_processor.withdraw(amount)
        else:
            raise Exception("Can't full fill the requested amount...")
