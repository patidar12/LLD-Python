from typing import List
from models.playng_piece import PlayingPiece

class Board:
    def __init__(self, size: int):
        self.size: int = size
        self.board: List[List[PlayingPiece]]= [[None]*size for _ in range(size)]
    
    def __is_safe(self, row, col):
        if row >= self.size or col >= self.size or self.board[row][col]:
            return False
        return True
    
    def add_piece(self, row: int, col: int, piece: PlayingPiece):
        if self.__is_safe(row, col):
            self.board[row][col] = piece
            return True
        return False
    def get_free_cell(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == None:
                    return (row, col)
        return None

    def print_board(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == None:
                    print("    |", end = "")
                else:
                    print(f"{self.board[row][col].piece_type.name}   ", end = "")
            print()
