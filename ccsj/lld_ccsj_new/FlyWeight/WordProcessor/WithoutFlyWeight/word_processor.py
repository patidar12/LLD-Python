class Character:
    def __init__(self, char: str, font_type: str, size: int, row: int, col: int):
        self.char: str = char
        self.fornt_type: str = font_type
        self.size: int = size
        self.row: int = row
        self.col: int = col


class WordProcess:
    def create_sentance(self):
        t = Character("t", "Arial", 10, 0, 1)
        t = Character("t", "Arial", 10, 11, 11)
