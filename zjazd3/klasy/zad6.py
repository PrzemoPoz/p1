class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, liczba):
        return Vector(self.x * liczba, self.y * liczba)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.dlugosc() < other.dlugosc()

    def dlugosc(self):
        return ((self.x) ** 2 + (self.y) ** 2) ** 0.5


vector1 = Vector(1, 2)
vector2 = Vector(1, 2)

# vector3 = vector1 + vector2
# print(vector3.x, vector3.y)
#
# vector3 = vector1 * 3
# print(vector3.x, vector3.y)


def test_dlugosc():
    vector1 = Vector(1, 2)
    vector2 = Vector(1, 2)
    assert vector1.dlugosc() == vector2.dlugosc()

def test_eq():
    vector1 = Vector(1, 2)
    vector2 = Vector(1, 2)
    assert vector1 == vector2

def test_lt():
    vector1 = Vector(1, 2)
    vector2 = Vector(1, 2)
    vector3 = Vector(3, 5)
    assert not vector1 < vector2
    assert vector1 < vector3
