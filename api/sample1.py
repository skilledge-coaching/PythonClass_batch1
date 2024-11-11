# form folder_name import sample

from sample import Bookstore

class libraryManager:
    def __init__(self, bookstore):
        self.bookstore = bookstore

    def add_book_to_store(self, id, title, author, year, genre):
        new_book = self.bookstore.add_book(id, title, author, year, genre)
        return new_book
    
if __name__ == "__main__":
    bookstore = Bookstore()
    manager = libraryManager(bookstore)

    manager.add_book_to_store(id=2, title= "The Sceret", author= "F. Scott Fitzgerald", year = 1925, genre= "Fiction")
    print(bookstore.get_book_by_id(2))

