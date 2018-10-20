def przywitanie(imie, wiek, wzrost, waga):
    print("Witaj", imie)
    if wzrost>178:
        print("Wysoki jak brzoza")
    if waga>50:
        print("przestasń jeść")
    if wiek>50:
        "czas zamykać sprawy"

lista = [
    {'imie': "Przemek", 'wiek' : 50, 'wzrost' : 200, 'waga' : 100},
    {'imie': "Bogdan", 'wiek' : 80, 'wzrost' : 180, 'waga': 50}
]

for osoba in lista:
    przywitanie(osoba['imie'],osoba['wiek'],osoba['wzrost'],osoba['waga'])


    def czy_wieksza_niz_3(liczba):
        if liczba>3:
            return True
        else:
            return False


def test_wieksza_niz_3_dla_wiekszej_niz_3():
    assert czy_wieksza_niz_3(4)