import json

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def to_json(self):
        """Convert Book object to JSON string."""
        return json.dumps(self.__dict__, indent=4)
