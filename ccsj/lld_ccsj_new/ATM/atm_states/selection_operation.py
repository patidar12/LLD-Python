from atm_states.state import State
from atm import Atm
from card import Card
from atm_states.withdraw import WithDrawState
from atm_states.check_balance import CheckBalanceState
from atm_states.idle import IdleState
from enums import TransactionType

class SelectOperationState(State):
    def select_operation(self, atm: Atm, card: Card, txn_type):
        if txn_type == TransactionType.WITHDRAW:
            atm.set_state(WithDrawState())
        elif txn_type == TransactionType.CHECK_BALANCE:
            atm.set_state(CheckBalanceState())
        else:
            print("Txn type not supported...")
            self.exit(atm)

    def exit(self, atm: Atm):
        self.return_card()
        atm.set_state(IdleState())

    def return_card(self):
        print("Card returned...")