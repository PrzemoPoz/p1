i = 1
suma = 0
liczba = 0

print(f"""Wpisz kolejną liczbę do obliczenia statystyk - zakończ wpisując x""")
while True:
    liczba = input(f"""Podaj {i}-tą liczbę: """)
    if liczba == "x":# or type(liczba)!=float or type(liczba)!=int:
        liczba = 0
        break
    else:
        liczba = float(liczba)
        if i == 1:
            maks = liczba
            mini = liczba
            imaks = i
            imini = i
        elif liczba >= maks:
            maks = liczba
            imaks = i
        elif liczba <= mini:
            mini = liczba
            imini = i
        suma = suma + liczba
        i=i+1

print(f"""Średnia dla {i-1} liczb to {round(suma/(i-1),2)}
Największa liczba była w pisania przez Ciebie w {imini} iteracji, gdy podałeś {mini}
Największa liczba była w pisania przez Ciebie w {imaks} iteracji, gdy podałeś {maks}""")
