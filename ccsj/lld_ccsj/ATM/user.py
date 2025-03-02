# has bankacount and card
from card import Card
from bank_account import BankAccount

class User:
    def __init__(self):
        self.bank_acount: BankAccount = None
        self.card: Card = None

    def set_card(self, card: Card) -> None:
        self.card = card
    
    def set_bank_account(self, account: BankAccount) -> None:
        self.bank_acount = account
