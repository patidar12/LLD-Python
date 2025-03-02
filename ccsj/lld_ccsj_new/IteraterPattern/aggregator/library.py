from typing import List

from aggregator import Aggregator
from model import Book
from iterater import BookIterater

class Library(Aggregator):
    def __init__(self, books: List[Book]):
        self.books: List[Book] = books
    
    def create_iterator(self):
        return BookIterater(self.books)
