from Expressions.abstract_expr import AbstractExpression
from Context.context import Context


class NumberTerminalExpression:
    def __init__(self, string_value: str):
        self.string_value: str = string_value

    def interpret(self, context: Context) -> int:
        return context.get(self.string_value)
