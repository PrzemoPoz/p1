slowo = ()
slowo = input("Podaj napis z nawiasami <>, w którym policzę znaki ")

pocz = slowo.index('<') + 1
kon = slowo.index('>')
slowon = slowo[pocz:kon]
licz = len(slowon)

print(slowo)
print(f"""Ilość znaków w nawiasach to {licz}""")
