from typing import List
from vending_machine import VendingMachine
from enums import Coin, ItemType
from item_shelf import ItemShelf
from item import Item

class Main:
    def main(self):
        vending_machine: VendingMachine = VendingMachine()
        try:
            print("|")
            print("filling up the inventory")
            print("|")
            self.fill_up_inventory(vending_machine)
            self.display_inventory(vending_machine)

            print("|")
            print("clicking on InsertCoinButton")
            print("|")

            vending_state = vending_machine.get_state()
            vending_state.click_on_insert_coin_button()

            vending_state = vending_machine.get_state()
            vending_state.insert_coin(Coin.NICKEL)
            vending_state.insert_coin(Coin.QUARTER)
            vending_state.insert_coin(Coin.NICKEL)

            print("|")
            print("clicking on ProductSelectionButton")
            print("|")
            vending_state.click_on_start_product_selection_button()

            vending_state = vending_machine.get_state()
            vending_state.choose_product(102)

            self.display_inventory(vending_machine)
        except Exception as e:
            print(e)
            self.display_inventory(vending_machine)

    def fill_up_inventory(self, vending_machine: VendingMachine):
        slots: List[ItemShelf] = vending_machine.get_inventory().get_inventory()
        for i in range(len(slots)):
            new_item = Item(ItemType.COKE, 12)
            if i >=0 and i<3:
                new_item = Item(ItemType.COKE, 12)
            elif i >=3 and i<5:
                new_item = Item(ItemType.PEPSI, 9)
            elif i >=5 and i<7:
                new_item = Item(ItemType.JUICE, 13)
            elif i >=7 and i<10:
                new_item = Item(ItemType.SODA, 7)
            slots[i].set_item(new_item)
            slots[i].set_sold_out(False)

    def display_inventory(self, vending_machine: VendingMachine):

        slots: List[ItemShelf] = vending_machine.get_inventory().get_inventory()
        for i in range(len(slots)):
            print("CodeNumber: ", slots[i].get_code(),
                    " Item: ", slots[i].get_item().item_type.name,
                    " Price: ", slots[i].get_item().price,
                    " isAvailable: ", not slots[i].is_sold_out())


Main().main()