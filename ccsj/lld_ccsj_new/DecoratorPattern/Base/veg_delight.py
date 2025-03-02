from Base.base_pizza import BasePizza
class VegDelight(BasePizza):
    __COST = 120
    def cost(self):
        return VegDelight.__COST
