import json

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @classmethod
    def from_json(cls, json_string):
        """Convert JSON string to Book object."""
        data = json.loads(json_string)
        return cls(**data)
