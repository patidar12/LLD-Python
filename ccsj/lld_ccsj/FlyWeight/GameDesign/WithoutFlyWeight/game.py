# this clas is responsible to create robot body that can use more memory.
class Sprites:
    pass



class Robot:
    def __init__(self, cordinate_x, cordinate_y, type, body: Sprites):
        self.cordinate_x: int = cordinate_x
        self.cordinate_y: int = cordinate_y
        self.type: str = type
        self.body: Sprites = body




# now for exmaple for ower game we need to create lots of robot
        
class Robotgame:
    def initialize_game(self):
        x: int = 0
        y: int = 0
        for i in range(500000):
            sprites: Sprites = Sprites()
            humanoid_robot_obj = Robot(cordinate_x=x+i, cordinate_y=x+y, type="HUMANOID", body=sprites)

        for i in range(500000):
            sprites: Sprites = Sprites()
            robotic_dog_obj = Robot(cordinate_x=x+i, cordinate_y=x+y, type="ROBOTIC_DOG", body=sprites)

        '''
        Here we are creating total 10 LAC objects and every object is using huge memory. SO we may ran out of memory.
        To solve this. we use flywight pattern.

        Observer and understand, when to use this pattern:
         When Memory is Limited
         When Object shared data:
            - Intrinsic data: shared among objects and remain same once defined one value.
                 ex: type, body
            - Extrinsic data: changed based on client input and differs from one object to another.
                 ex: cordinate_x, cordinate_y
         Creation of object is expensive.

         This is how it resolve the issue:
            - From object, remove all the Extrinsic data and keep Intrinsic Data (this is called Flyweight Object)
            - This Fliweight can be immutable.
            - Extrinsic data can be passed to the Flyweight class as method parameter.
            - Once the Flyweight Object is created, it is cached and reused whenever required.
        
        To correctly implement this, please check WithFlyewight folder.
        '''
