from Base.base_pizza import BasePizza

class TopingDecorator(BasePizza):
    def __init__(self, base_pizza: BasePizza):
        self.base_pizza = base_pizza
