from typing import List

from iterater import Iterater
from model import Book

class BookIterater(Iterater):
    def __init__(self, books: List[Book]):
        self.books: List[Book] = books
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.books)
    
    def next(self):
        if not self.has_next():
            raise Exception("No book present....")
        book = self.books[self.index]
        self.index += 1
        return book
