from expense.split import (
    ExpenseSplit,
    EqualExpenseSplit,
    UnEqualExpenseSplit,
    PercentageExpenseSplit
)

from expense_split_type import ExpenseSplitType

class SplitFactory:
    @staticmethod
    def get_split_object(self, split_type: ExpenseSplitType) -> ExpenseSplit:
        if split_type == ExpenseSplitType.EQUAL:
            return EqualExpenseSplit()
        if split_type == ExpenseSplitType.UNEQUAL:
            return UnEqualExpenseSplit()
        if split_type == ExpenseSplitType.PERCENTAGE:
            return PercentageExpenseSplit()
        raise Exception("requested split type not supported...")
