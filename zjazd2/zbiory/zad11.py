liczby=set()
parz=set(range(2,101,2))
while True:
    komenda = input("Dawaj liczby dziadu - wpisz [koniec], by przerwać: ")
    if komenda == 'koniec':
        break
    else:
        komenda=int(komenda)
        liczby.add(komenda)
iloczyn=set(liczby & parz)
print(f"""Oto liczby parzyste: {iloczyn} """)
print(f"""Liczb parzystych jest: {len(iloczyn)}""")