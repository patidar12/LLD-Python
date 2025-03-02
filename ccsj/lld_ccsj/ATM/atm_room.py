from atm import Atm
from user import User
from card import Card
from bank_account import BankAccount
from account_type import AccountType
from txn_type import TransactionType

class AtmRoom:
    def __init__(self):
        self.atm: Atm = None
        self.user: User = None
        self.initialize()
    
    def initialize(self):
        atm = Atm()
        atm.add_balance(amount = 3500, two_thousand_notes = 1, five_hundread_notes = 2, hundread_rs_notes = 5)
        self.atm = atm
        self.create_user()
    
    def create_user(self):
        self.user = User()
        self.user.set_bank_account(self.create_bank_acount())
        self.user.set_card(self.create_card(self.user.bank_acount))


    def create_bank_acount(self) -> BankAccount:
        return BankAccount(acc_no=101, acc_type=AccountType.SAVING, balance=3000)
    
    def create_card(self, bank_account: BankAccount) -> Card:
        return Card(bank_account)


atmRoom = AtmRoom()

atmRoom.atm.print_atm_state()
atmRoom.atm.state.insert_card(atmRoom.atm, atmRoom.user.card)
atmRoom.atm.state.authentication(atmRoom.atm, atmRoom.user.card, 543617)
atmRoom.atm.state.select_operation(atmRoom.atm, atmRoom.user.card, TransactionType.WITHDRAW)
atmRoom.atm.state.withdraw_operation(atmRoom.atm, atmRoom.user.card, 2700)
atmRoom.atm.print_atm_state()
