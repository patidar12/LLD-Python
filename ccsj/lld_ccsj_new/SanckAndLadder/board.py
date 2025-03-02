import random
from cell import Cell
from jump import Jump

class Board:
    def __init__(self, size, snaks, ladders):
        self.size = size
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]
        self.create_snaks_and_ladders(snaks, ladders)
    
    def create_snaks_and_ladders(self, snaks, ladders):
        starts = set()
        while snaks > 0:
            shead = random.randint(0, self.size * self.size - 1)
            stail = random.randint(0, self.size * self.size - 1)
            if shead <= stail or shead in starts:
                continue
            cell = self.get_cell(shead)
            cell.jump = Jump("snack", shead, stail)
            snaks -= 1

        while ladders > 0:
            lstart = random.randint(0, self.size * self.size - 1)
            lend = random.randint(0, self.size * self.size - 1)
            if lstart >= lend or lstart in starts:
                continue
            cell = self.get_cell(lstart)
            cell.jump = Jump("ladder", lstart, lend)
            ladders -= 1

    def get_cell(self, pos):
        row = pos // self.size
        col = pos % self.size
        return self.board[row][col]