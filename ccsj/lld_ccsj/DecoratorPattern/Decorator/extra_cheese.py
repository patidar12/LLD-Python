from Decorator.topping_decorator import ToppingDecorator
from Base.base_pizza import BasePizza

class ExtraCheese(ToppingDecorator):
    COST = 10

    def __init__(self, pizza: BasePizza):
        self.pizza = pizza
    
    def cost(self) -> float:
        return self.pizza.cost() + self.COST
