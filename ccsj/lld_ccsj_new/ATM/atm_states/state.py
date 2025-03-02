class State:
    def insert_card(self, atm, card):
        raise Exception("Something went wrong!")
    def authenticate_pin(self, atm, card, pin):
        raise Exception("Something went wrong!")
    def select_operation(self, atm, card, txn_type):
        raise Exception("Something went wrong!")
    def withdraw_operation(self, atm, card, ammount):
        raise Exception("Something went wrong!")
    def check_balance(self, atm, card):
        raise Exception("Something went wrong!")
    def exit(self, atm):
        raise Exception("Something went wrong!")
    def return_card(self):
        raise Exception("Something went wrong!")