import pickle
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from person import Person 


from persistence_demo.person import Person

def load_person(filename):
    with open(filename, "rb") as file:
        person = pickle.load(file)
    print(f"Deserialized Person object: {person}")
    return person

if __name__ == "__main__":
    load_person("person.pkl")
