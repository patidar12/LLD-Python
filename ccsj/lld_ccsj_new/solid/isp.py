from abc import ABC, abstractmethod

class WaiterInterface(ABC):
    @abstractmethod
    def serve_customer(self): pass

    @abstractmethod
    def take_order(self): pass

class ChefInterface(ABC):
    @abstractmethod
    def cook_food(self): pass

    @abstractmethod
    def decide_menu(self): pass

class Waiter(WaiterInterface):
    def serve_customer(self):
        print("Serving to customer...")

    @abstractmethod
    def take_order(self):
        print("Taking order...")
    