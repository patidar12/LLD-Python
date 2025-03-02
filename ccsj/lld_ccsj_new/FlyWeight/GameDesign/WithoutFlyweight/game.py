class Sprits: pass


class Robot:
    def __init__(self, x: int, y: int, type: str, body: Sprits):
        self.cordinate_x: int = x
        self.cordinate_y: int = y
        self.type: str = type
        self.body: Sprits = body



class RobotGame:
    def initialize_game(self):
        x: int = 0
        y: int = 0
        for i in range(500000):
            sprit: Sprits = Sprits()
            humunoid_robot = Robot(x=x+i, y=y+i, type="HUMANOID", body=sprit)

        for i in range(500000):
            sprit: Sprits = Sprits()
            robotic_dog = Robot(x=x+i, y=y+i, type="ROBOTIC_DOG", body=sprit)

