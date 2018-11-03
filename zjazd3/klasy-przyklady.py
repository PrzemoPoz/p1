# definicja klasy
class Animal:
    nazwa = "Fauna"
    licznik = 0

    def __init__(self, gatunek):
        self.gatunek = gatunek
        self.zwieksz_licznik()

    # atrybuty instancji
    def __str__(selfself):
        return "Animal"

    # metoda klasowa
    @classmethod
    def zwieksz_licznik(cls):
        cls.licznik += 1

# tworzenie instancji danej klasy
azor = Animal("Canis lupus")
rudolf = Animal("Rangifer tarandus")

print(type(azor))
print(azor)
print(azor.gatunek)
print(rudolf.gatunek, rudolf.nazwa)

Animal.nazwa = "dupa"
print(rudolf.gatunek, rudolf.nazwa)

print(Animal.licznik)
