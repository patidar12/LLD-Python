from atm import Atm
from card import Card

from txn_type import TransactionType
from atm_states.withdraw import WithdrawState
from atm_states.check_balance import CheckBalanceState

class SelecOperationState:
    def __init__(self):
        print("ATM is in selectOPeration state!")
    
    def select_operation(self, atm: Atm, card: Card, txn_type: TransactionType):
        if txn_type == TransactionType.WITHDRAW:
            atm.set_state(WithdrawState())
        elif txn_type == TransactionType.CHECK_BALANCE:
            atm.set_state(CheckBalanceState())
        else:
            print("Invalid transaction type... Please select allowed transaction types!")
            self.exit(atm)
            from atm_states.idle_state import IdleState
            atm.set_state(IdleState())

    def exit(self, atm):
        print("Atm exit.. returning Card!")
        self.return_card()

    def return_card(self):
        print("Card returned")
