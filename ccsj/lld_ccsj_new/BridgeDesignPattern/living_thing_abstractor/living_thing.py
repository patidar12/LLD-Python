from abc import ABC, abstractmethod
from breath_implementor import BreathImplementor

class LivingThing(ABC):
    def __init__(self, breath_implementor: BreathImplementor):
        self.breath_implementor: BreathImplementor = breath_implementor
    
    @abstractmethod
    def breath_process(self): pass