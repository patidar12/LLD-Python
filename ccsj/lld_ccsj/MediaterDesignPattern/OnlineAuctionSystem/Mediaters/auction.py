from typing import List

from Mediaters.auction_mediator import AuctionMediator
from Colleages.colleage import Colleage


class Auction(AuctionMediator):
    def __init__(self):
        self.bidders: List[Colleage] = []
    

    def add_bidder(self, bidder: Colleage):
        self.bidders.append(bidder)
    

    def place_bid(self, bidder: Colleage, bid_amount: float):
        print(f"Bidder: {bidder.get_name()} place the bid for amount: {bid_amount}...")
        for colledge in self.bidders:
            # skip the notification for bidder it self. and send to all the college in auction...
            if bidder.get_name() != colledge.get_name():
                colledge.receive_notification(bid_amount)
