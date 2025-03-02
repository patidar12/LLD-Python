class Sprites:
    pass


from abc import ABC, abstractmethod
from typing import Dict

class IRobot(ABC):
    @abstractmethod
    def display(self, x: int, y: int):
        pass


class HumanoidRobot(IRobot):
    def __init__(self, type_: str, body: Sprites):
        # creating private to make it immutable 
        self.__type = type_
        self.__body = body
    
    def get_type(self) -> str:
        return self.__type

    def get_body(self) -> Sprites:
        return self.__body
    
    def display(self, x: int, y: int) -> None:
        print(f"{self.__type}, {self.__body}, {x}, {y}")


class RoboticDog(IRobot):
    def __init__(self, type_: str, body: Sprites):
        # creating private to make it immutable 
        self.__type = type_
        self.__body = body
    
    def get_type(self) -> str:
        return self.__type

    def get_body(self) -> Sprites:
        return self.__body
    
    def display(self, x: int, y: int) -> None:
        print(f"{self.__type}, {self.__body}, {x}, {y}")



# now to cache the object we create a factory class

class RoboticFactory:
    robotic_obj_cache: Dict[str, IRobot] = {}
    @classmethod
    def create_robot(cls, robot_type: str)-> IRobot:
        if cls.robotic_obj_cache.get(robot_type):
            return cls.robotic_obj_cache[robot_type]
        elif robot_type == "HUMANOID":
            sprites: Sprites = Sprites()
            humanoid_robot_obj: IRobot = HumanoidRobot(type_=robot_type, body=sprites)
            cls.robotic_obj_cache[robot_type] = humanoid_robot_obj
            return humanoid_robot_obj
        elif robot_type == "ROBOTICDOG":
            sprites: Sprites = Sprites()
            robotic_dog_obj: IRobot = RoboticDog(type_=robot_type, body=sprites)
            cls.robotic_obj_cache[robot_type] = robotic_dog_obj
            return robotic_dog_obj
        return None



class Robotgame:
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

Robotgame().initialize_game()