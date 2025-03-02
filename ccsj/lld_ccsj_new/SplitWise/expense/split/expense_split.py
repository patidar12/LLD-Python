from typing import List

from abc import ABC, abstractmethod
from expense.split.split import Split

class ExpenseSplit(ABC):

    @abstractmethod
    def validate_split_request(self, split_details: List[Split], total_amount: float): pass
