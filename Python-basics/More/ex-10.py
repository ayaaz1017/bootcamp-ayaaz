def add_method(cls):
    def new_method(self):
        return "This is a new method!"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass


obj = MyClass()
print(obj.new_method())