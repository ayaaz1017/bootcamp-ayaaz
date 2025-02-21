import pickle
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from person import Person  # Now it should work


from persistence_demo.person import Person

def save_person(filename):
    person = Person("Alice", ["MIT", "Harvard"], ["Bob", "Charlie"])
    with open(filename, "wb") as file:
        pickle.dump(person, file)
    print(f"Serialized and saved Person object to {filename}")

if __name__ == "__main__":
    save_person("person.pkl")
