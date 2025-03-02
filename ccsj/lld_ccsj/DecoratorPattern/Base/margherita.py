from Base.base_pizza import BasePizza

class Margherita(BasePizza):
    COST = 100

    def cost(self):
        return self.COST

