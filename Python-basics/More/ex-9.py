
MyClass = type('MyClass', (object,), {'x': 10, 'y': 20})


obj = MyClass()
print(f"x: {obj.x}, y: {obj.y}")