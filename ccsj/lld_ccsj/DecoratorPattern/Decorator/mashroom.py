from Decorator.topping_decorator import ToppingDecorator
from Base.base_pizza import BasePizza

class Mashroom(ToppingDecorator):
    COST = 15

    def __init__(self, pizza: BasePizza):
        self.pizza = pizza
    
    def cost(self) -> float:
        return self.pizza.cost() + self.COST
    