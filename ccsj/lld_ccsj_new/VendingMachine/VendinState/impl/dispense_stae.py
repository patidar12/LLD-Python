from VendinState.state import State

class DispenseState(State):
    NAME: str = "Dispense"
    def __init__(self, machine, product_code):
        super().__init__(machine)
        self.dispense_product(product_code)
        
    def dispense_product(self, product_code: int):
        from VendinState.impl.idle_state import IdleState
        print("Product has been dispensed...")
        item = self.machine.get_inventory().get_item(product_code)
        self.machine.get_inventory().update_sold_out_item(product_code)
        self.machine.set_state(IdleState(self.machine))
        return item