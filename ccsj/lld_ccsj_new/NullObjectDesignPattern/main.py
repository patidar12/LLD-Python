from vechile_factory import VechileFactory
from vechile import Vechile

class VechileManager:
    def operations(self):
        vechile: Vechile = VechileFactory.get_vechile("BIKE")
        print(vechile.get_seating_capacity())
        print(vechile.get_tank_capacity())

VechileManager().operations()