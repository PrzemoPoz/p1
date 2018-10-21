# Napisz program "odsetki.py", który obliczy stan konta za N lat,
# # gdzie stan początkowy konta wynosi SPK, a stopa oprocentowania P % rocznie (obowiązuje roczna kapitalizacja odsetek). N, SPK i P podaje użytkownik programu.

def odsetki(spk, n, p):
    konto = round(spk * (1 + p) ** n, 2)
    print(f"""Dla stanu początkowego {spk} PLN, przy stope oprocentowania {p}, za {n} lat będziesz miał na koncie""")
    return konto


spk = float(input("Podaj stan początkowy konta: "))
n = int(input("Podaj okres w latach: "))
p = float(input("Podaj stopę oprocentowania: "))
print(odsetki(spk, n, p))
