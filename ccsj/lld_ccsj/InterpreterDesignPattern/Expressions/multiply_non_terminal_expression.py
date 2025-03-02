from Expressions.abstract_expr import AbstractExpression
from Context.context import Context


class MultiplyNonTerminalExpression:
    def __init__(self, left_expr: AbstractExpression, right_expr: AbstractExpression):
        self.left_expr: AbstractExpression = left_expr
        self.right_expr: AbstractExpression = right_expr

    def interpret(self, context: Context) -> int:
        return self.left_expr.interpret(context) * self.right_expr.interpret(context)
