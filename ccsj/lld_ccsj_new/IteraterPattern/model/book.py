class Book:
    def __init__(self, name: str, price: float):
        self.__name: str = name
        self.__price: float = price
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
