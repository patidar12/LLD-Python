from Elements.room_element import RoomElement
from Visitors.room_visitor import RoomVisitor

class SingleRoom(RoomElement):
    PRICE: float = 0
    def accept(self, visitor: RoomVisitor):
        visitor.visit_single_room(self)
