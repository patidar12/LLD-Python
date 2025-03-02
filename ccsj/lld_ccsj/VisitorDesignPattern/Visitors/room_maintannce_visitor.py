from Visitors.room_visitor import RoomVisitor
from Elements.double_room import DoubleRoom
from Elements.duplex_room import DuplexRoom
from Elements.single_room import SingleRoom

class RoomMaintananceVisitor(RoomVisitor):

    def visit_single_room(self, element: SingleRoom):
        print("Single room maintanance visit...")

    def visit_double_room(self, element: DoubleRoom):
        print("Double room maintanance visit...")

    def visit_duplex_room(self, element: DuplexRoom):
        print("Duplex room maintanance visit...")
