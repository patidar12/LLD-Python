from Elements.double_room import DoubleRoom
from Elements.duplex_room import DuplexRoom
from Elements.single_room import SingleRoom

from Visitors.room_maintannce_visitor import RoomMaintananceVisitor
from Visitors.room_pricing_visitor import RoomPricingVisitor

class HotelManagement:

    def hotel_system(self):
        single_room = SingleRoom()
        double_room = DoubleRoom()
        duplex_room = DuplexRoom()

        visitor = RoomPricingVisitor()
        single_room.accept(visitor)
        double_room.accept(visitor)
        duplex_room.accept(visitor)

        visitor = RoomMaintananceVisitor()
        single_room.accept(visitor)
        double_room.accept(visitor)
        duplex_room.accept(visitor)    


HotelManagement().hotel_system()