from abc import ABC, abstractmethod

class WaiterInterface(ABC):

    @abstractmethod
    def serve_customer(self):
        pass

    @abstractmethod
    def take_order(self):
        pass

class ChefInterface(ABC):

    @abstractmethod
    def cook_food(self):
        pass

    @abstractmethod
    def decide_menu(self):
        pass


class Waiter(WaiterInterface):

    def serve_customer(self):
        print("serving food")

    def take_order(self):
        print("taking order")

'''
Here we have given the correct implemantation of ISP.

Here we created small interfaces according to responsibility. So different client not need to implement functions that is not required to them.
Only relavent information should be shared with client.


'''