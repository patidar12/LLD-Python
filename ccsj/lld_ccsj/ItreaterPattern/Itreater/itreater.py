from abc import ABC, abstractmethod

class Itreater(ABC):

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass
