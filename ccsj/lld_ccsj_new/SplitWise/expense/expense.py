from typing import List
from expense.expense_split_type import ExpenseSplitType
from user import User
from split.split import Split

class Expense:
    def __init__(
            self,
            eid: str,
            description: str,
            amount: float,
            split_type: ExpenseSplitType,
            paid_by: User,
            split_details: List[Split]
            ):
        self.eid: str = eid
        self.description: str = description
        self.amount: float = amount
        self.split_type: ExpenseSplitType = split_type
        self.paid_by: User = paid_by
        self.split_details: List[Split] = split_details
