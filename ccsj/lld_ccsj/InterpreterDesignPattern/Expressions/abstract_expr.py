from abc import ABC, abstractmethod
from Context.context import Context

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context: Context) -> int:
        pass
