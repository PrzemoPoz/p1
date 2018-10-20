def czy_jest_pierwsza(liczba):
    i=0
    for x in range(1, liczba):
        if liczba%x==0:
            i+=1
            if i>2:
                break
    if i>2:
        print(f"{liczba} nie jest liczbą pierwszą")
    else:
        print(f"{liczba} jest liczbą pierwszą")

czy_jest_pierwsza(int(input("podaj liczbę ")))




def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(7)
    assert czy_jest_pierwsza(17)
    assert czy_jest_pierwsza(23)