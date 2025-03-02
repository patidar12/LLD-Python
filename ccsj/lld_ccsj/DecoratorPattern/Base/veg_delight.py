from Base.base_pizza import BasePizza

class VegDelight(BasePizza):
    COST = 120

    def cost(self):
        return self.COST
