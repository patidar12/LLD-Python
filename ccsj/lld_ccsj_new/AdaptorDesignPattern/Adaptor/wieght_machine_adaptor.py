from abc import ABC, abstractmethod

class WeightMachineAdaptor(ABC):

    @abstractmethod
    def get_wieght_in_kg(self): pass