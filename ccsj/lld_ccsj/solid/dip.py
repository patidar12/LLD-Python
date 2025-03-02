
from abc import ABC, abstractmethod

class KeyBoard(ABC):
    pass

class WiredKeyBoard(KeyBoard):
    pass

class BlutoothKeyBoard(KeyBoard):
    pass


class Mouse(ABC):
    pass

class WiredMouse(Mouse):
    pass

class BlutoothMouse(Mouse):
    pass



class MacBook:
    def __init__(self, keyboard: KeyBoard, mouse: Mouse):
        self.keyboard: KeyBoard = keyboard
        self.mouse: Mouse = mouse


'''
DIP: classes should depends on interfaces rather then concrete classes

Above we used interfaces directly so it is provide flexibility to use both wired or Bluetooth keyboard or mouse without breaking any changes.

TODO: How to implement DIP in python correctly.

'''