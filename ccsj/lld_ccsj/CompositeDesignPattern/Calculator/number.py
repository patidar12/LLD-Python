from arithmetic_expression import ArithmeticExpression

class Number(ArithmeticExpression):
    def __init__(self, value: int):
        self.value: int = value
    
    def evaluate(self) -> None:
        print("Number: ", self.value)
        return self.value