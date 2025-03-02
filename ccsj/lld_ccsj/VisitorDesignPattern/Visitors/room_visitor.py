from abc import ABC, abstractmethod


class RoomVisitor(ABC):
    @abstractmethod
    def visit_single_room(self, element):
        pass

    @abstractmethod
    def visit_double_room(self, element):
        pass

    @abstractmethod
    def visit_duplex_room(self, element):
        pass
