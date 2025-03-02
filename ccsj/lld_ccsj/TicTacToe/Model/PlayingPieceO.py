from Model.PieceType import PieceType
from Model.PlayingPiece import PlayingPiece

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)
