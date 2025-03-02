from atm_states.state import State
from atm_states.idle import IdleState

class Atm:
    def __init__(self):
        self.state: State = IdleState()
        self.balance: int = 0
        self.two_thousand_notes: int = 0
        self.five_hundread_notes: int = 0
        self.hundread_rs_notes: int = 0

    def print_atm_state(self):
        print(f"Total Balance: {self.balance}\nTwo Thousand Notes: {self.two_thousand_notes}\n \
              Five Hundred NOtes: {self.five_hundread_notes}\nHundread Notes: {self.hundread_rs_notes}")    

    def set_state(self, state: State):
        self.state = state
    
    def get_state(self):
        return self.state

    def add_amount(self, amount, two_thousand_notes=0, five_hundread_notes=0, hundread_rs_notes=0):
        self.balance += amount
        self.two_thousand_notes += two_thousand_notes
        self.five_hundread_notes += five_hundread_notes
        self.hundread_rs_notes += hundread_rs_notes
    
    def get_two_thousand_notes(self) -> int:
        return self.two_thousand_notes

    def get_five_hundread_notes(self) -> int:
        return self.five_hundread_notes

    def get_hundread_notes(self) -> int:
        return self.hundread_rs_notes

    def deduct_two_thousand_balance(self, two_thousand_notes: int):
        self.balance -= (two_thousand_notes * 2000)
        self.two_thousand_notes -= two_thousand_notes

    def deduct_five_hundread_balance(self, five_hundread_notes: int):
        self.balance -= (five_hundread_notes * 500)
        self.five_hundread_notes -= five_hundread_notes

    def deduct_hundread_balance(self, hundread_rs_notes: int):
        self.balance -= (hundread_rs_notes * 100)
        self.hundread_rs_notes -= hundread_rs_notes

    def add_two_thousand_balance(self, two_thousand_notes: int):
        self.balance += (two_thousand_notes * 2000)
        self.two_thousand_notes += two_thousand_notes

    def add_five_hundread_balance(self, five_hundread_notes: int):
        self.balance += (five_hundread_notes * 500)
        self.two_thousand_notes += five_hundread_notes

    def add_hundread_balance(self, hundread_rs_notes: int):
        self.balance += (hundread_rs_notes * 100)
        self.two_thousand_notes += hundread_rs_notes
