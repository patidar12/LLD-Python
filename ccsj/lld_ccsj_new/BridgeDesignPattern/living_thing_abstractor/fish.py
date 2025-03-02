from living_thing_abstractor import LivingThing
from breath_implementor import BreathImplementor

class Fish(LivingThing):
    def __init__(self, breath_implementor: BreathImplementor):
        super().__init__(breath_implementor)
    
    def breath_process(self):
        self.breath_implementor.breath()
