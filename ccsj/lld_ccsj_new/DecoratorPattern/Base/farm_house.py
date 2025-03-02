from Base.base_pizza import BasePizza
class FarmHouse(BasePizza):
    __COST = 200
    def cost(self):
        return FarmHouse.__COST
