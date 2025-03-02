from abc import ABC

class keyBoard(ABC): pass

class WiredKeyBoard(keyBoard): pass

class BluetoothKeyBoard(keyBoard): pass

class Mouse(ABC): pass

class WiredMouse(Mouse): pass

class BluetoothMouse(Mouse): pass


class MackBook:
    def __init__(self):
        self.keyboard: WiredKeyBoard = WiredKeyBoard()
        self.mouse: WiredMouse = WiredMouse()


