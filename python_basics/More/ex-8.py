from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    @property
    def sound(self):
        return "Woof!"

class Cat(Animal):
    @property
    def sound(self):
        return "Meow!"

# Create instances
dog = Dog()
cat = Cat()

print(f"Dog says: {dog.sound}")
print(f"Cat says: {cat.sound}")