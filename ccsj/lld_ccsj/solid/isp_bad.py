from abc import ABC, abstractmethod

class RestruantEmployee(ABC):
    @abstractmethod
    def wash_dishes(self):
        pass

    @abstractmethod
    def serve_customer(self):
        pass

    @abstractmethod
    def cook_food(self):
        pass


class Waiter(RestruantEmployee):

    def wash_dishes(self):
        print("Not my job")

    def serve_customer(self):
        print("serving the food")

    def cook_food(self):
        print("Not my job")


'''
ISP: interfaces should be such, that client should not implement unneccasary functions they do not need.

Issue in above examples is that we have created RestruantEmployee interface with 3 different method.
Now when waiter class extends RestruantEmployee it need to define all the method, even there is no use of that method in waiter class.
So according to ISP interfaces should be small.
'''