from arithmetic_expression import ArithmeticExpression

class Number(ArithmeticExpression):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self):
        print(f"Value is: {self.value}")
        return self.value

