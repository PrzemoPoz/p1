liczby={}
parzyste={}

while True:
    komenda = input("Dawaj liczby dziadu - wpisz [koniec], by przerwać: ")
    if komenda == 'koniec':
        break
    else:
        komenda=int(komenda)
        liczby[komenda]=liczby.get(komenda,0)+1
        if komenda%2==0:
            if  komenda<=100:
                parzyste[komenda] = "jest to liczba parzysta"
            else:
                parzyste[komenda] = "jest to liczba większa od 100"
        else:
            parzyste[komenda] = "jest to liczba nieparzysta"
for xx in liczby:
    print(f"""Liczba {xx} wystąpiła {liczby[xx]}.""")