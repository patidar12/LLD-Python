from models.playng_piece import PlayingPiece
class Player:
    def __init__(self, name, piece: PlayingPiece):
        self.piece = piece
        self.name = name
