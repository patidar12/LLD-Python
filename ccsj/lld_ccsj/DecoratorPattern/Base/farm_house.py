from Base.base_pizza import BasePizza

class FarmHouse(BasePizza):
    COST = 200

    def cost(self):
        return self.COST
