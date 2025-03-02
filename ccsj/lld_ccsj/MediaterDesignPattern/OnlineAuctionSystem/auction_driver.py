from Colleages.bidder import Bidder
from Mediaters.auction import Auction



class AuctionManager:

    def create_and_start_auction(self):
        # create auction
        auction: Auction = Auction()

        # create bidder
        bidder1: Bidder = Bidder(name="bidder1", mediator=auction)
        bidder2: Bidder = Bidder(name="bidder2", mediator=auction)

        # add bidder in auction
        auction.add_bidder(bidder1)
        auction.add_bidder(bidder2)

        # start bidding...
        bidder1.place_bid(2000)
        bidder2.place_bid(3500)
        bidder1.place_bid(4000)


AuctionManager().create_and_start_auction()