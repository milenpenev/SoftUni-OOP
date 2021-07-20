class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.add_user(self)
            if self.username in library.rented_books:
                rented_books = library.rented_books[self.username]
                if not rented_books:
                    library.rented_books[self.username] = {book_name: days_to_return}
                else:
                    library.rented_books[self.username][book_name] = days_to_return