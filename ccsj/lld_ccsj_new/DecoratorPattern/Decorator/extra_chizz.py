from Base.base_pizza import BasePizza
from Decorator.topping_decorator import TopingDecorator

class ExtraCheez(TopingDecorator):
    __COST = 10
    
    def cost(self):
        return self.base_pizza.cost() + ExtraCheez.__COST
