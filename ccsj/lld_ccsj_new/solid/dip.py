from abc import ABC

class keyBoard(ABC): pass

class WiredKeyBoard(keyBoard): pass

class BluetoothKeyBoard(keyBoard): pass

class Mouse(ABC): pass

class WiredMouse(Mouse): pass

class BluetoothMouse(Mouse): pass


class MackBook:
    def __init__(self, keyboard: keyBoard, mouse: Mouse):
        self.keyboard: keyBoard = keyboard
        self.mouse: Mouse = mouse
