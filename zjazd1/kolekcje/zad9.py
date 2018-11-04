slownik = {'ziemniaki': 1.5, 'jabłka': 2.5, 'kumkwat': 1}
magazyn = {'ziemniaki': 10, 'jabłka': 10, 'kumkwat': 10}
koszyk={}
naleznosc = 0

while True:
    print("Nasz zielnik oferuje: ")
    for produkt in slownik:
        cena = slownik[produkt]
        print(f' - {produkt} - {cena} PLN na stanie jeszcze {magazyn[produkt]}')

    komenda = input("Co chcesz zrobić: [k]upić, [d]odać, [koniec] by przerwać zakupy: ")
    if komenda == 'koniec':
        break
    elif komenda == 'd':
        produkt_dod_dodania = input("Jaki produkt dod dodania: ")
        if produkt_dod_dodania not in magazyn:
            magazyn[produkt_dod_dodania] = 0
            cena_nowego_produktu = float(input("Za ile to sprzedajemy: "))
        ile_produktu_dodajemy = float(input("Ile tego dodać: "))
        magazyn[produkt_dod_dodania] += ile_produktu_dodajemy
        slownik[produkt_dod_dodania] = cena_nowego_produktu
    else:
        produkt_wybrany = input("Co chcesz kupić: ")
        if produkt_wybrany not in slownik:
            print("Nie mamy takiego artykułu")
            continue
        else:
            waga = float(input(f'ile chcesz kupić wybranego produktu:  {produkt_wybrany} : '))
            if magazyn[produkt_wybrany] < waga:
                print(f"Mamy za mało {[produkt_wybrany]}, pozostało {magazyn[produkt_wybrany]}")
                continue
            koszt = slownik[produkt_wybrany] * waga
            naleznosc += koszt
            magazyn[produkt_wybrany] -= waga
            koszyk[produkt_wybrany]=koszyk.get(produkt_wybrany,0)+koszt
print(f'Do zapłaty: ')
suma = 0
for produkt in koszyk:
    print(f" - {produkt} - {koszyk[produkt]} PLN")
    suma += koszyk[produkt]
print(f"Razem: {suma} PLN")
