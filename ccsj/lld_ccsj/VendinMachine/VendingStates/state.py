from vending_machine import VendingMachine

class State:
    def __init__(self, machine):
        self.machine: VendingMachine = machine
    
    def click_on_insert_coin_button(self):
        raise Exception(f"insert coin button opration not allowed in {self.machine.state.name} state.")
    
    def insert_coin(self, coin):
        raise Exception(f"Coin insertion not allowed in {self.machine.state.name} state.")
    
    def click_on_start_product_selection_button(self):
        raise Exception(f"Product selection action not allowed in {self.machine.state.name} state.")
    
    def choose_product(self, product_code: int):
        raise Exception(f"Product selection not allowed in {self.machine.state.name} state.")
    
    def dispense_product(self, product_code: int):
        raise Exception(f"Product dispense not allowed in {self.machine.state.name} state.")
    
    def get_change(self, return_change_money):
        raise Exception(f"Change money not allowed in {self.machine.state.name} state.")

    def refund_full_money(self):
        raise Exception(f"Refund not allowed in {self.machine.state.name} state.")
    
    def update_inventory(self, item, code_number):
        raise Exception(f"Inventory updation not allowed in {self.machine.state.name} state.")
