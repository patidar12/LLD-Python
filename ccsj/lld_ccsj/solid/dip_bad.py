
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
    def __init__(self):
        self.wired_keyboard: WiredKeyBoard = WiredKeyBoard()
        self.wired_mouse: WiredMouse = WiredMouse()


'''
DIP: classes should depends on interfaces rather then concrete classes

IN above scenario we have use wiredKeyBoard and WiredMOuse classes directly. So if later we wan't to provide functionality of bluetooth

keyboard or moue in Macbook Then we can't do it.

To resolve this instead of using classes as depndency we should use interfaces. So later if inplace of WiredKeyBoard we wan;t to use
Buletooth Keyboard then we don't need to change anything. It is provide flexibility in inplementation or changes.
'''