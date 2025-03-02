from abc import ABC, abstractmethod
from Visitors.room_visitor import RoomVisitor

class RoomElement(ABC):
    @abstractmethod
    def accept(visitor: RoomVisitor):
        pass
