from persistence_demo.book import Book

def load_book():
    json_string = '{"title": "1984", "author": "George Orwell", "pages": 328}'
    book = Book.from_json(json_string)
    print(f"Deserialized Book: {book.title}, {book.author}, {book.pages} pages")

if __name__ == "__main__":
    load_book()
