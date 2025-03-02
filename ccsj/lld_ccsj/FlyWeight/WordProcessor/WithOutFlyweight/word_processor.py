class Charator:
    def __init__(self, char: str, font_type: str, size: int, row: int, col: int):
        self.char = char
        self.font_type = font_type
        self.size = size
        self.row = row
        self.col = col
    
class WordProcessor:
    def write_word(self):
        '''
        this is the data we want to write into the word processor

        Total: 58 chars
        t: 7 times
        h: 3 times
        a: 3 times ans so on...
        '''

        obj1 = Charator(char='t', font_type="Arial", size=10, row=0, col=0)
        obj2 = Charator(char='h', font_type="Arial", size=10, row=0, col=1)
        obj3 = Charator(char='i', font_type="Arial", size=10, row=0, col=2)
        obj4 = Charator(char='s', font_type="Arial", size=10, row=0, col=3)

        '''
        Memory issue:
            for same char, same font_type, size we are creatig objects that can use more memory.
        
            It can be solved using FlyWeight pattern.
        '''