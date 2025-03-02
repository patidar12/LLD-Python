from typing import List, Tuple
from Model.PlayingPiece import PlayingPiece

class Board:
    def __init__(self, size):
        self.size = size
        self.board: List[List[PlayingPiece]] = [[None for i in range(size)] for j in range(size)]

    def __is_safe(self, row: int, col: int) -> bool:
        if row >= self.size or col >= self.size or self.board[row][col]:
            return False
        return True

    def add_piece(self, row: int, col: int, piece: PlayingPiece) -> bool:
        if self.__is_safe(row, col):
            self.board[row][col] = piece
            return True
        return False

    def get_free_cell(self) -> Tuple[int, int]:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    return (i, j)
        return None

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    print("    |",end="")
                else:
                    print(f"{self.board[i][j].type.name}   |", end="")
            print()
