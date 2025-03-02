from abc import ABC, abstractmethod
from typing import Dict

class ILetter(ABC):
    def display(self, row: int, col: int):
        pass


class DocumentCharactor(ILetter):
    def __init__(self, char: str, font_type: str, size: int):
        self.__char: str = char
        self.__font_type: str = font_type
        self.__size: int = size
    
    # only gatter method for above private variables
    def display(self, row: int, col: int):
        print(f"{self.__char}, {self.__font_type}, {self.__size}, {row}, {col}")


class LetterFactory:
    char_cache: Dict[str, DocumentCharactor] = {}
    
    @classmethod
    def create_letter(cls, char_value) -> DocumentCharactor:
        if cls.char_cache.get(char_value):
            return cls.char_cache[char_value]
        else:
            char_obj = DocumentCharactor(char=char_value, font_type="Arial", size=10)
            cls.char_cache[char_value] = char_obj
            return char_obj

    
class WordProcessor:
    def write_word(self):
        '''
        this is the data we want to write into the word processor

        Total: 58 chars
        t: 7 times
        h: 3 times
        a: 3 times ans so on...
        '''

        obj1: ILetter = LetterFactory.create_letter(char_value='t')
        obj1.display(row=0, col=1)

        obj2: ILetter = LetterFactory.create_letter(char_value='h')
        obj2.display(row=0, col=2)

        obj3: ILetter = LetterFactory.create_letter(char_value='i')
        obj3.display(row=0, col=3)

        obj4: ILetter = LetterFactory.create_letter(char_value='s')
        obj4.display(row=0, col=4)

WordProcessor().write_word()