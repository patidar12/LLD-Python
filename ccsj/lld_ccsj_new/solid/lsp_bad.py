from abc import ABC, abstractmethod

class Bike:
    @abstractmethod
    def turn_on_engine(self): pass    

    @abstractmethod
    def accelerate(self): pass


class MoterCycle(Bike):
    def __init__(self):
        self.is_engine_on = False
        self.speed = 0

    def turn_on_engine(self):
        self.is_engine_on = True

    def accelerate(self):
        self.speed += 10

class ByCycle(Bike):
    def __init__(self):
        self.speed = 0

    def turn_on_engine(self):
        raise Exception("No engine present")

    def accelerate(self):
        self.speed += 5
