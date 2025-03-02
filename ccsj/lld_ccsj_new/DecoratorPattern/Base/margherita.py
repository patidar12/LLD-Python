from Base.base_pizza import BasePizza
class Margherita(BasePizza):
    __COST = 200
    def cost(self):
        return Margherita.__COST
