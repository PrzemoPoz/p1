x = ["koszt $cena PLN", "kwota $cena brutto", "cena $cena"]


def formatowanie_opt(*args, **kwargs):
    print(args)
    print(kwargs)
    tekst_out = []
    for tekst in args:
        for k in kwargs:
            tekst = tekst.replace(f'$(k)', str(kwargs[k]))
        tekst_out.append(tekst)
    return "\n".join(tekst_out)


cena = int(input("podaj cenę do sformatowania"))
print(formatowanie_opt)

