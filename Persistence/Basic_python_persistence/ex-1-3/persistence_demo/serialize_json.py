from persistence_demo.book import Book

def save_book():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    json_string = book.to_json()
    print("Serialized JSON:\n", json_string)

if __name__ == "__main__":
    save_book()
