from car import Car
from null_vechile import NullVechile

class VechilFactory:
    def get_vechile_by_type(self, vechile_type: str):
        if vechile_type.lower() == "car":
            return Car()
        return NullVechile()
