from Elements.room_element import RoomElement
from Visitors.room_visitor import RoomVisitor

class DoubleRoom(RoomElement):
    PRICE: float = 0
    def accept(self, visitor: RoomVisitor):
        visitor.visit_double_room(self)
