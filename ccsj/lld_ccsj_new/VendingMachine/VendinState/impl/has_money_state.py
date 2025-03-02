from VendinState.state import State
from VendinState.impl.selection_state import SelectionState

class HasMoneyState(State):
    NAME: str = "Has Money"

    def insert_coin(self, coin):
        print("Accepted the coin")
        self.machine.get_coins().append(coin)

    def click_on_start_product_selection_button(self):
        self.machine.set_state(SelectionState(self.machine))

    def refund_full_money(self):
        from VendinState.impl.idle_state import IdleState
        coins = self.machine.get_coins()
        self.machine.set_state(IdleState(self.machine))
        return coins
