class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"p1 == p2: {p1 == p2}")
print(f"p1 < p3: {p1 < p3}")