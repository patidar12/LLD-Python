from Base.farm_house import FarmHouse
from Base.margherita import Margherita
from Base.veg_delight import VegDelight

from Decorator.extra_chizz import ExtraCheez
from Decorator.mushroom import Mashroom

class PizzaShopManager:
    def make_pizza(self):
        margherita = Margherita()
        mec = ExtraCheez(margherita)
        mshrm_ecz_farm = Mashroom(ExtraCheez(FarmHouse()))
        print(margherita.cost())
        print(mec.cost())
        print(mshrm_ecz_farm.cost())

PizzaShopManager().make_pizza()