import os
import pickle
from persistence_demo.person import Person
from persistence_demo.serialize import save_person

def test_serialization():
    filename = "test_person.pkl"
    save_person(filename)
    assert os.path.exists(filename)
    with open(filename, "rb") as file:
        person = pickle.load(file)
    assert isinstance(person, Person)
    assert person.name == "Alice"
    os.remove(filename)
