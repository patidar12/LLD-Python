from typing import List

from model.book import Book
from Aggregate.aggregate import Aggregate
from Itreater.book_iterater import BookItreater

class Librarey(Aggregate):
    def __init__(self, book_list: List[Book]):
        self.book_list: List[Book] = book_list
    
    def create_iterator(self) -> BookItreater:
        return BookItreater(self.book_list)
