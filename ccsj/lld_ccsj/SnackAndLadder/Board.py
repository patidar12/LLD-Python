import random
from Cell import Cell
from Jump import Jump

class Board:
    def __init__(self, size: int, snaks: int, ladders: int):
        self.size = size
        self.board = self.initialize_board()
        self.create_snaks_and_ladders(snaks, ladders)

    def initialize_board(self):
        board = [[None] * self.size for row in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                board[i][j] = Cell()
        return board

    def get_cell(self, pos):
        row = pos//self.size
        col = pos%self.size
        return self.board[row][col]

    def create_snaks_and_ladders(self, snaks: int, ladders: int):
        starts = set()
        while snaks > 0:
            snack_head: int = random.randint(0, (self.size * self.size)-1)
            snack_tail: int = random.randint(0, (self.size * self.size)-1)
            if snack_head <= snack_tail or snack_head in starts:
                continue
            starts.add(snack_head)
            snack_obj: Jump = Jump(name="Snack", start=snack_head, end=snack_tail)
            cell: Cell = self.get_cell(snack_head)
            cell.jump = snack_obj
            snaks -= 1

        while ladders > 0:
            ladder_start: int = random.randint(0, (self.size * self.size)-1)
            ladder_end: int = random.randint(0, (self.size * self.size)-1)
            if ladder_start >= ladder_end or ladder_start in starts:
                continue
            starts.add(ladder_start)
            ladder_obj: Jump = Jump(name="Ladder", start=ladder_start, end=ladder_end)
            cell: Cell = self.get_cell(ladder_start)
            cell.jump = ladder_obj
            ladders -= 1





