def formatowanie(cena, *args):
    x = ("koszt $cena PLN", "kwota $cena brutto", "cena $cena")
    tekst=""
    for zmienna in x:
        i = 0
        for znak in zmienna:
            if zmienna[i:i + 5] == "$cena":
                tekst += zmienna[0:i] + f"{cena}" + zmienna[i + 5:len(zmienna)] + ", "
                break
            i = i + 1
    return tekst


cena = int(input("podaj cenę do sformatowania"))
print(formatowanie(cena))

def test_formatowanie():
    assert formatowanie(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto'
    ) == "koszt 10 PLN\nkwota 10 brutto"

    assert formatowanie(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto',
        'sumarycznie $cena'
    ) == "koszt 10 PLN\nkwota 10 brutto\nsumarycznie 10"

