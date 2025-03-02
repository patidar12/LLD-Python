from arithmetic_expression import ArithmeticExpression
from expression import Expression
from number import Number
from operation import Operation

class Calculator:

    @classmethod
    def enter_expression(self):
        super()
        '''
        2 * (1+7)

        
                *
              /  \
            2     +
                /   \
               1      7

        '''
        left_expression: ArithmeticExpression = Number(2)
        one: ArithmeticExpression = Number(1)
        seven: ArithmeticExpression = Number(7)
        right_expression: ArithmeticExpression = Expression(one, seven, Operation.ADD)
        expression: ArithmeticExpression = Expression(left_expression, right_expression, Operation.MULTIPLY)
        return expression

    @classmethod
    def evaluate(self, expression: ArithmeticExpression) -> int:
        return expression.evaluate()

print("Result: ", Calculator.evaluate(Calculator.enter_expression()))
