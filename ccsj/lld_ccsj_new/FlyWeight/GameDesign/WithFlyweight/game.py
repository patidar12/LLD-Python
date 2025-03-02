class Sprites: pass


from abc import ABC, abstractmethod
from typing import Dict

class IRobot(ABC):
    @abstractmethod
    def display(self, x: int, y: int): pass


class HumanoidRobot(IRobot):
    def __init__(self, type: str, body: Sprites):
        self.__type: str = type
        self.__body: Sprites = body

    def get_type(self):
        return self.__type
    
    def get_body(self):
        return self.__body

    def display(self, x, y):
       print(f"{self.__type}, {self.__body}, {x}, {y}")


class RoboticDog(IRobot):
    def __init__(self, type: str, body: Sprites):
        self.__type: str = type
        self.__body: Sprites = body

    def get_type(self):
        return self.__type
    
    def get_body(self):
        return self.__body

    def display(self, x, y):
       print(f"{self.__type}, {self.__body}, {x}, {y}")


class RoboticFactory:
    robotic_obj_cache: Dict[str, IRobot] = {}
    @classmethod
    def create_robot(cls, type: str):
        if cls.robotic_obj_cache.get(type):
            return cls.robotic_obj_cache[type]
        elif type == "HUMANOID":
            sprites: Sprites = Sprites()
            humanoid_obj: HumanoidRobot = HumanoidRobot(type, sprites)
            cls.robotic_obj_cache[type] = humanoid_obj
            return humanoid_obj
        elif type == "ROBOTICDOG":
            sprites: Sprites = Sprites()
            robotic_dog_obj: IRobot = RoboticDog(type, sprites)
            cls.robotic_obj_cache[type] = robotic_dog_obj
            return robotic_dog_obj
        return None




class RobotGame:
    def initialize_game(self):
        humanoid_robot1: IRobot = RoboticFactory.create_robot("HUMANOID")
        humanoid_robot1.display(x=1, y=10)

        # so here it is not creatig object again, instead it is just using the cache
        # Also while creating object, it is just using memory for intinsic variable
        humanoid_robot2: IRobot = RoboticFactory.create_robot("HUMANOID")
        humanoid_robot2.display(x=4, y=15)

        robo_dog1: IRobot = RoboticFactory.create_robot("ROBOTICDOG")
        robo_dog1.display(x=2, y=5)

        # so here it is not creatig object again, instead it is just using the cache
        # Also while creating object, it is just using memory for intinsic variable
        robo_dog2: IRobot = RoboticFactory.create_robot("ROBOTICDOG")
        robo_dog2.display(x=5, y=20)


RobotGame().initialize_game()
