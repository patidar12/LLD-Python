from models.PieceType import PieceType

class PlayingPiece:
    def __init__(self, piece_type: PieceType):
        self.piece_type = piece_type


class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)


class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)
