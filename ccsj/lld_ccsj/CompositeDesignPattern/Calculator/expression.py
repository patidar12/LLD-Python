from operation import Operation
from arithmetic_expression import ArithmeticExpression

class Expression(ArithmeticExpression):
    def __init__(self, left_expression: ArithmeticExpression, right_expression: ArithmeticExpression, operation: Operation):
        self.left_expresion: ArithmeticExpression = left_expression
        self.right_expression: ArithmeticExpression = right_expression
        self.operation: Operation = operation
    

    def evaluate(self):
        left_result = self.left_expresion.evaluate()
        right_result = self.right_expression.evaluate()
        result = 0
        if self.operation == Operation.ADD:
            result = left_result + right_result
        elif self.operation == Operation.SUBTRACT:
            result = left_result - right_result
        elif self.operation == Operation.MULTIPLY:
            result = left_result * right_result
        elif self.operation == Operation.DIVIDE:
            result = left_result // right_result
        return result
