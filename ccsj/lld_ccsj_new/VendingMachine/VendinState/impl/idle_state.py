from VendinState.state import State
from VendinState.impl.has_money_state import HasMoneyState

class IdleState(State):
    NAME: str = "Idle"
    def __init__(self, machine):
        super().__init__(machine)
        machine.set_coins([])

    def click_on_insert_coin_button(self):
        self.machine.set_state(HasMoneyState(self.machine))

    def update_inventory(self, item, code_number):
        self.machine.get_inventory().add_item(item, code_number)
