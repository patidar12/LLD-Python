from Context.context import Context
from Expressions.multiply_non_terminal_expression import MultiplyNonTerminalExpression
from Expressions.number_terminal_expression import NumberTerminalExpression
from Expressions.abstract_expr import AbstractExpression

class InterpreteExpression:

    def solve_expression(self):
        context: Context = Context()
        context.put(string_value="a", number=2)
        context.put(string_value="b", number=15)
        expr1: AbstractExpression = MultiplyNonTerminalExpression(
            NumberTerminalExpression(string_value="a"),
            NumberTerminalExpression(string_value="b")
        )
        print(expr1.interpret(context))


InterpreteExpression().solve_expression()
