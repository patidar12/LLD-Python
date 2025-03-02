from Adapter.weight_machine_adapter_impl import WeightMachinAdapterImpl
from Adaptee.weight_machine_for_babies import WeightMachineForBabies

class WeightMachineInKg:

    def weight(self):
        weight_machine = WeightMachinAdapterImpl(WeightMachineForBabies())
        return weight_machine.get_weight_in_kg()


print("You weight: ", WeightMachineInKg().weight())
