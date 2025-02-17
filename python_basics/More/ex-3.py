class Book:
    num_books = 0  

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.num_books += 1  

    @classmethod
    def get_num_books(cls):
        return cls.num_books

# Create instances of Book
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Get the number of books created
print(f"Total books created: {Book.get_num_books()}")