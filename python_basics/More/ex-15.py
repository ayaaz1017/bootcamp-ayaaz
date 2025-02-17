class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

point = Point(1, 2)
print(point)


try:
    point.x = 3
except AttributeError as e:
    print(e)