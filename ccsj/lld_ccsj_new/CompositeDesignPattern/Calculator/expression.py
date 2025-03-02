from arithmetic_expression import ArithmeticExpression
from operation import Operation

class Expression(ArithmeticExpression):
    def __init__(self, left: ArithmeticExpression, right: ArithmeticExpression, operation: ArithmeticExpression):
        self.left: ArithmeticExpression = left
        self.right: ArithmeticExpression = right
        self.operation: Operation = operation
    
    def evaluate(self):
        left_result = self.left.evaluate()
        right_result = self.right.evaluate()
        if self.operation == Operation.ADD:
            result = left_result + right_result
        elif self.operation == Operation.SUBTRACT:
            result = left_result - right_result
        elif self.operation == Operation.MULTIPLY:
            result = left_result * right_result
        elif self.operation == Operation.DIVIDE:
            result = left_result // right_result
        return result
