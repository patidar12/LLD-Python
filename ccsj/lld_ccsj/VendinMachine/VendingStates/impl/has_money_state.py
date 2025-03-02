from coin import Coin

from VendingStates.state import State
from VendingStates.impl.selection_state import SelectionState

class HasMoneyState(State):
    NAME: str = "Has Money"
    
    def insert_coin(self, coin: Coin):
        print("Accepted the coin")
        self.machine.get_coins().append(coin)

    def click_on_start_product_selection_button(self):
        self.machine.set_state(SelectionState())

    def refund_full_money(self):
        from VendingStates.impl.idle_state import IdleState
        self.machine.set_state(IdleState())
        return self.machine.get_coins()

