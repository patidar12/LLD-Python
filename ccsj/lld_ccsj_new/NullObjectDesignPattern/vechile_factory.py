from vechile import Vechile
from car import Car
from null_vechile import NullVechile

class VechileFactory:
    @staticmethod
    def get_vechile(vechile_type: str) -> Vechile:
        if vechile_type == "CAR":
            return Car()
        return NullVechile()
