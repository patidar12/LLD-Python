from typing import List

class Vechile:
    def number_of_wheels(self):
        return 2


class EngineVechile(Vechile):
    def has_engine(self):
        return True
    

class Bycycle(Vechile): pass

class Car(EngineVechile):
    def number_of_wheels(self):
        return 4

class MotorCycle(EngineVechile): pass

class VechileManager:
    def print_number_of_wheels(self):
        vechiles: List[Vechile] = []
        vechiles.append(Car())
        vechiles.append(MotorCycle())
        vechiles.append(Bycycle())
        for vechile in vechiles:
            print(vechile.number_of_wheels())
    
    def has_engine(self):
        vechiles: List[EngineVechile] = []
        vechiles.append(Car())
        vechiles.append(MotorCycle())
        #vechiles.append(Bycycle()) # this failes because of bycle not have engine. it's compile time error in other langugae while accesing has_engine method.
        for vechile in vechiles:
            print(vechile.has_engine())


VechileManager().print_number_of_wheels()
VechileManager().has_engine()
