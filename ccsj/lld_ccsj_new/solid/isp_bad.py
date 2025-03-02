from abc import abstractmethod, ABC

class RestorantEmployee(ABC):
    @abstractmethod
    def wash_dishes(self): pass

    @abstractmethod
    def serve_customers(self): pass

    @abstractmethod
    def cook_food(self): pass

class Waiter(RestorantEmployee):

    def wash_dishes(self):
        print("Not my job")

    def serve_customers(self):
        print("Serving to customer on table number: 10")

    def cook_food(self):
         print("Not my job")
