class Bookstore:
    def __init__(self):
        self.books = []
    
    def add_book(self, id, title, author, year, genre):
        new_book = {
            "id": id,
            "title": title,
            "author": author,
            "year": year,
            "genre": genre
        }
        self.books.append(new_book)
        return new_book
    
    def get_book_by_id(self, id):
        for book in self.books:
            if book["id"] == id:
                return book
        return None
    
if __name__ == "__main__":
    bookstore = Bookstore()

    book1 = bookstore.add_book(id=1, title= "The Sceret", author= "F. Scott Fitzgerald", year = 1925, genre= "Fiction")

    print(bookstore.get_book_by_id(1)["title"])