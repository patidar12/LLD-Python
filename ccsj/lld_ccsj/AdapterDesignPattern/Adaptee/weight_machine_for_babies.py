import random
from Adaptee.weight_machine import WeightMachine

class WeightMachineForBabies(WeightMachine):
    def get_weight_in_pounds(self) -> float:
        # assuming babies have weight b/w 3 to 20.
        return round(random.uniform(3, 20), 2)
