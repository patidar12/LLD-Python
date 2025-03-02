from bank_account import BankAccount
from card import Card

class User:
    def __init__(self):
        self.banck_account: BankAccount = None
        self.card: Card = None

    def set_card(self, card: Card) -> None:
        self.card = card
    
    def set_bank_account(self, account: BankAccount) -> None:
        self.bank_acount = account
