from Adaptor.wieght_machine_adaptor import WeightMachineAdaptor
from Adaptee.weight_machine import WeightMachine

class WeightMachineAdaptorImpl(WeightMachineAdaptor):
    def __init__(self, weight_machine: WeightMachine):
        self.weight_machine: WeightMachine = weight_machine

    def get_wieght_in_kg(self):
        weight_in_pound = self.weight_machine.get_wieght_in_pound()
        weight_in_kg = round(weight_in_pound * 0.45, 2)
        return weight_in_kg
