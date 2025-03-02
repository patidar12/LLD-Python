from model import Book
from aggregator import Library

class LibraryManager:

    def manage(self):
        books = [
            Book("RD Sharma", 1200),
            Book("ML Khanna", 800),
            Book("HLD", 2000),
            Book("LLD", 1400)
        ]
        library = Library(books)
        book_iterator = library.create_iterator()
        while book_iterator.has_next():
            book = book_iterator.next()
            print(f"Name: {book.get_name()}")
        # book_iterator.next() -> raise eception if no book present, as iterator comes at the end form above loop.

LibraryManager().manage()