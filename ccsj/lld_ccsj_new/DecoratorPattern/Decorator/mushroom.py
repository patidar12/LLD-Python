from Base.base_pizza import BasePizza
from Decorator.topping_decorator import TopingDecorator

class Mashroom(TopingDecorator):
    __COST = 5
    
    def cost(self):
        return self.base_pizza.cost() + Mashroom.__COST
