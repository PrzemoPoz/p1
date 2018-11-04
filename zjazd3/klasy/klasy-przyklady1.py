""""Stwórz klasę Dog wedgług następującej specyfikacji:
•pies zużywa energię szczekając (bark) i zyskuje śpiąc (sleep).
•nowa instancja klasy Dog ma 10 jednostek energii
•Dog ma metodę sleep która dodaje mu 2 jednostki energii
•Dog ma metodę bark która konsumuje mu 1 jednostkę energii
•Dog ma metodę get_energy która zwraca wartość energii instancji
"""

class Dog():
    nazwa = "psyyyyyyyyy"

    def __init__(self):
        self.energia=10

    def get_energy(self):
        return self.energia

    def sleep(self):
        self.energia+=2

    def bark(self):
        self.energia-=1

azor=Dog()
print(Dog.get_energy(azor))
azor.bark()
print(Dog.get_energy(azor))
azor.sleep()
print(Dog.get_energy(azor))
