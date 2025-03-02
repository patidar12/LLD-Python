from abc import ABC, abstractmethod

class Iterater(ABC):
    def next(self): pass

    def has_next(self): pass