# definicja klasy
class Animal:
    nazwa = "Fauna"
    licznik = 0

    def __init__(self, gatunek):
        self.gatunek = gatunek
        self.zwieksz_licznik()
        self.stan = "nic nie robi"
        self.pasza = None

    # atrybuty instancji
    def __str__(selfself):
        return "Animal"

    # metoda klasowa
    @classmethod
    def zwieksz_licznik(cls):
        cls.licznik += 1

    def idz(self):
        self.stan = "idzie"

    def stoj(self):
        self.stan = "stoi"


class LeniweZwierzeta(Animal):
    pass

# tworzenie instancji danej klasy
azor = Animal("Canis lupus")
rudolf = Animal("Rangifer tarandus")

print(type(azor))
print(azor)
print(azor.gatunek)
print(rudolf.gatunek, rudolf.nazwa)

Animal.nazwa = "Fiona"
print(rudolf.gatunek, rudolf.nazwa)

print(Animal.licznik)

azor.idz()
print(azor.stan)
azor.stoj()
print(azor.stan)


garfield=LeniweZwierzeta("Felis Catus")
LeniweZwierzeta.idz(garfield)


print(garfield.stan)


