from Base.margherita import Margherita
from Base.farm_house import FarmHouse
from Decorator.extra_cheese import ExtraCheese
from Decorator.mashroom import Mashroom

class PizzaShop:

    def order(self):
        pizaa = FarmHouse()
        print(f"farm house: {pizaa.cost()}")
        extra_cheese = ExtraCheese(pizaa)
        print(f"farm house + extra cheese: {extra_cheese.cost()}")
        mashroom = Mashroom(extra_cheese)
        print(f"farmHouse + extraCheese + Mashroom: {mashroom.cost()}")
        frm_mashroom = Mashroom(pizaa)
        print(f"farmHouse + Mashroom: {frm_mashroom.cost()}")
        mashroom_cheese = ExtraCheese(mashroom)
        print(f"farmHouse + extraCheese + Mashroom + ExtraCheese: {mashroom_cheese.cost()}")

PizzaShop().order()
