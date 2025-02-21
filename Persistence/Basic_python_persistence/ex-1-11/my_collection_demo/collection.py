import pickle

class MyCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def deserialize(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)
