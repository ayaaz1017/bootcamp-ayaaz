import pickle

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Reference to another node

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return f"Node({self.value})"

def serialize_nodes(filename, node):
    with open(filename, "wb") as file:
        pickle.dump(node, file, protocol=pickle.HIGHEST_PROTOCOL)

def deserialize_nodes(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
