import json
while True:
    co = input("co chcesz zrobić? [d - dodaj, w - wypisz ")
    dane_zb = {}
    prac_baza = []
    try:
        with open("pracownicy.json") as f:
            prac_baza = json.load(f)
    except FileNotFoundError:
        praca_baz = []
    if co == "d":
        imie = input("Imię: ")
        nazwisko = input("Nazwisko: ")
        rok = int(input("Rok urodzenia: "))
        pensja = float(input("Pensja: "))
        dane_zb = {
            "imie": imie,
            "nazwisko": nazwisko,
            "rok": rok,
            "pensja": pensja}
        with open("pracownicy.json") as f:
            prac_baza = json.load(f)
            prac_baza.append(dane_zb)
        with open("pracownicy.json", "w") as f:
            json.dump(prac_baza, f)
    elif co == "w":
        print("Pracownicy:")
        for i, pracownik in enumerate(prac_baza, start=1):
            print(
                f''' - [{i}] {pracownik['imie']} {pracownik['nazwisko']}, rok {pracownik['rok']}, pensja {pracownik['pensja']} PLN''')
        break
    elif co=="k":
        break
    else:
        "idź na grzyby"
        break