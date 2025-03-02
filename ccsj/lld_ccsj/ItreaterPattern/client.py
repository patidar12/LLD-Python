from typing import List
from model.book import Book
from Aggregate.librarey import Librarey
from Itreater.itreater import Itreater


class LibraryManagement:

    def manage_library(self) -> None:
        book_list: List[Book] = [
            Book(name="Maths", price=123.10),
            Book(name="Computer", price=500),
            Book(name="System Design", price=2000),
            Book(name="DSA", price=800)
        ]
        library: Librarey = Librarey(book_list=book_list)
        itrerator: Itreater = library.create_iterator()
        while itrerator.has_next():
            book: Book = itrerator.next()
            print(f"Name: {book.get_name()}, price={book.get_price()}")

LibraryManagement().manage_library()