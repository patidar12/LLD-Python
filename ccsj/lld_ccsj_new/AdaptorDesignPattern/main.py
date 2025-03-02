from Adaptee.weight_machine_for_babies import WeightMachineForBabies
from Adaptor.weight_machine_adaprot_impl import WeightMachineAdaptorImpl

class WeightMachineKg:
    def get_your_weight(self):
        '''
        Return weight in KG
        '''
        weight_machine = WeightMachineAdaptorImpl(WeightMachineForBabies())
        print(weight_machine.get_wieght_in_kg())


WeightMachineKg().get_your_weight()