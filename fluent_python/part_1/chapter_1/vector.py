import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)


vector = Vector(2, 1)
vector2 = Vector(2, 2)
print(vector)
print(vector2)
print(vector + vector2)
print(vector * 3)
print(bool(vector))
print(bool(Vector(0, 0)))
