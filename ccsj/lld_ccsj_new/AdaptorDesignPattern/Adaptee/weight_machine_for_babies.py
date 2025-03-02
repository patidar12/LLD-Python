import random
from Adaptee.weight_machine import WeightMachine

class WeightMachineForBabies(WeightMachine):
    def get_wieght_in_pound(self):
        return round(random.uniform(3,20), 2)
