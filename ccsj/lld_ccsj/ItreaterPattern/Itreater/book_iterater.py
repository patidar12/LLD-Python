from typing import List

from Itreater.itreater import Itreater
from model.book import Book

class BookItreater(Itreater):
    def __init__(self, book_list: List[Book]):
        self.book_list: List[Book] = book_list
        self.index = 0
    
    def has_next(self) -> bool:
        return self.index < len(self.book_list)
    
    def next(self) -> Book:
        if self.has_next():
            book = self.book_list[self.index]
            self.index += 1
            return book
