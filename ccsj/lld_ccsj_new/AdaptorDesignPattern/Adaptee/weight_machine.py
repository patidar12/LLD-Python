from abc import ABC, abstractmethod

class WeightMachine(ABC):

    @abstractmethod
    def get_wieght_in_pound(self): pass