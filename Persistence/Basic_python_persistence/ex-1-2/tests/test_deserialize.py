import os
import pickle
from persistence_demo.person import Person
from persistence_demo.deserialize import load_person

def test_deserialization():
    filename = "test_person.pkl"
    person = Person("Alice", ["MIT", "Harvard"], ["Bob", "Charlie"])
    with open(filename, "wb") as file:
        pickle.dump(person, file)
    
    loaded_person = load_person(filename)
    assert isinstance(loaded_person, Person)
    assert loaded_person.name == "Alice"
    os.remove(filename)
