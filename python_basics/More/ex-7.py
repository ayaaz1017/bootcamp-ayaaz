class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Create instances and perform arithmetic
v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(f"Addition: {v1 + v2}")
print(f"Subtraction: {v1 - v2}")