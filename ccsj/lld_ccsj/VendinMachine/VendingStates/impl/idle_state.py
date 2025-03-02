from VendingStates.state import State
from VendingStates.impl.has_money_state import HasMoneyState

class IdleState(State):
    NAME: str = "idle"

    def __init__(self, machine):
        machine.set_coins([])

    def click_on_insert_coin_button(self):
        print("Currently machine is in idle state!")
        self.machine.set_state(HasMoneyState())
    
    def update_inventory(self, item, code_number):
        self.machine.get_inventory().add_item(item, code_number)
