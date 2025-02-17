class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author})"


book = Book("1984", "George Orwell")


print(str(book))  
print(repr(book))  