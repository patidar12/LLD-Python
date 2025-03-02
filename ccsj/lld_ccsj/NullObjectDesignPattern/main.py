from vechile_factory import VechilFactory
from vechile import Vechile

class Main:
    def print_vechile_detail(self, vechile_type: str):
        vechile: Vechile = VechilFactory().get_vechile_by_type(vechile_type)
        print("Vechile seating capacity: ", vechile.get_seating_capacity())
        print("Vechile tank capacity: ", vechile.get_tank_capacity())



Main().print_vechile_detail("car")