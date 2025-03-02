from VendinState.state import State
from item import Item
from VendinState.impl.dispense_stae import DispenseState

class SelectionState(State):
    NAME: str = "Product Selection"

    def choose_product(self, product_code: int):
        # get item for this code number
        item: Item = self.machine.get_inventory().get_item(product_code)

        paid_by_user = 0
        # total amount paid by user
        for coin in self.machine.get_coins():
            paid_by_user += coin.value
    
        if paid_by_user < item.price:
            print("Insufficient amount...")
            self.refund_full_money()
            raise Exception("Insufficient amount...")
        else:
            if paid_by_user > item.price:
                self.get_change(paid_by_user - item.price)
            self.machine.set_state(DispenseState(self.machine, product_code))

    def get_change(self, return_change_money):
        print("Returned the change in coin dispense tray: ", return_change_money)
        return return_change_money

    def refund_full_money(self):
        from VendinState.impl.idle_state import IdleState
        coins = self.machine.get_coins()
        self.machine.set_state(IdleState(self.machine))
        return coins
