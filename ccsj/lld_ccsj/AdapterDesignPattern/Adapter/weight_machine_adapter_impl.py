from Adapter.weight_machine_adapter import WeightMachinAdapter
from Adaptee.weight_machine import WeightMachine

class WeightMachinAdapterImpl(WeightMachinAdapter):

    def __init__(self, weight_machie: WeightMachine):
        self.weight_machine: WeightMachine = weight_machie

    def get_weight_in_kg(self) -> float:
        weight_in_pound: float = self.weight_machine.get_weight_in_pounds()

        '''
        Converting pounds to kg, as required by client.
        1 pound = 0.45 kg
        Here serving what client need by adpating the available code(Adaptee), is what Adaptor pattern used for.
        '''
        return round(weight_in_pound * 0.45, 2)
