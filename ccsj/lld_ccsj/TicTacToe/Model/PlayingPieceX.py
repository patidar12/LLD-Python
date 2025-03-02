from Model.PieceType import PieceType
from Model.PlayingPiece import PlayingPiece

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)
