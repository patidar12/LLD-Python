from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self): pass
