from abc import ABC, abstractmethod

class Bike(ABC):
    @abstractmethod
    def turn_on_engine(self):
        pass

    @abstractmethod
    def acelerate(self, add_speed):
        pass


class MotorCycle(Bike):
    def __init__(self):
        # default behavious of motorcycle
        self.isEngineOn = False
        self.speed = 10
    
    def turn_on_engine(self):
        self.isEngineOn = True
    
    def acelerate(self, add_speed):
        self.speed += add_speed
    

class BiCycle(Bike):
    def __init__(self):
        self.isEngineOn = False
        self.speed = 10
    
    def turn_on_engine(self):
        raise Exception("BiCycle having no engine")

    def acelerate(self, add_speed):
        self.speed += add_speed


'''
LSP: If class B is subtype of class A, then we should be able to replace object of A with B without breaking behaviour of program.
Note: Subclass should extend the capability of parent class not narrow it down.

 In abve example there is issue that if we passing Motorcycle object to any function and it is using turn_on_engine method.
 If after some time we started to send the BiCycle object then it will thorugh error. that is wrong implementation. Because
 of we are narrowing down capability of Bike class in BiCycle class.
 
'''