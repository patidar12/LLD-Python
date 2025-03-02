from abc import ABC, abstractmethod
from typing import Dict

class ILetter(ABC):
    @abstractmethod
    def display(self, row: int, col: int):
        pass


class DocumentCharacter(ILetter):
    def __init__(self, char: str, font_type: str, size: int):
        self.char: str = char
        self.font_type: str = font_type
        self.size: int = size
    
    def display(self, row, col):
        print(f"{self.char} {self.font_type} {self.size} {row} {col}")


class LetterFactory:
    letter_obj_map: Dict[str, ILetter] = {}
    @classmethod
    def create_letter(cls, char: str): 
        if cls.letter_obj_map.get(char):
            return cls.letter_obj_map[char]
        else:
            letter: DocumentCharacter = DocumentCharacter(char, font_type="Arial", size=10)
            cls.letter_obj_map[char] = letter
            return letter


class WordProcess:
    def create_sentance(self):
        obj1 = LetterFactory.create_letter("t")
        obj1.display(10, 20)

        obj2 = LetterFactory.create_letter("t")
        obj2.display(12, 20)


WordProcess().create_sentance()