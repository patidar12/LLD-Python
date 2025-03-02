from abc import ABC, abstractmethod

from breathe_implementer import BreatheImplementer

class LivingThings(ABC):
    def __init__(self, breathe_implementer: BreatheImplementer):
        self.breathe_implementer: BreatheImplementer = breathe_implementer
    
    @abstractmethod
    def breathe_process(self):
        pass


class Dog(LivingThings):
    def breathe_process(self):
        self.breathe_implementer.breathe()


class Fish(LivingThings):
    def breathe_process(self):
        self.breathe_implementer.breathe()

class Tree(LivingThings):
    def breathe_process(self):
        self.breathe_implementer.breathe()



