import math

class Sfera:
    def __init__(self, r):
        self.promien = r

    def pole(self):
        return math.pi * 4 * (self.promien) ** 2

    def objetosc(self):
        return (4 / 3) * math.pi * math.pow(self.promien, 3)


s = Sfera(10)
print("Pole wynosi ", round(s.pole(),2))
print("Objętość wynosi ", round(s.objetosc(),2))

# stwórz klasę sfera
# s=Sfera(10)
# s.promien==10
# s.objetosc()
# s.pole_powierzchni()
