class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def validate_isbn(isbn):

        return len(isbn) in [10, 13] and isbn.isdigit()


isbn = "1234567890"
print(f"Is {isbn} a valid ISBN? {Book.validate_isbn(isbn)}")