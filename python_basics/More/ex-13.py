import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

class Person(JsonMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 30)
json_str = person.to_json()
print(f"JSON: {json_str}")

new_person = Person.from_json(json_str)
print(f"From JSON: {new_person.name}, {new_person.age}")