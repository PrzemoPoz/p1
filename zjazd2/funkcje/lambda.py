def podzielna_przez_2(x):
    return x%2==0

def podzielna_przez_3(x):
    return x%3==0

print(podzielna_przez_2(12))
print(podzielna_przez_2(11))

y=lambda x: x%2==0
print(y(12))
print(y(11))

y=podzielna_przez_2
print(y(12))
print(y(11))

def wieksze_niz_7(x):
    if x<7:
        return True
    else:
        return False

def wybierz(dane,warunek):
    """
    :param dane:lista liczb
    :param warunek: jakaś funkcja sprawdzająca coś
    :return: przefiltrowana lista
    """
    out=[]
    for element in dane:
        if warunek(element):
            out.append(element)
    return(out)

lista=[1,2,3,4,5,6,7,8,9,122,123]
print(wybierz(lista,podzielna_przez_2))
print(wybierz(lista,wieksze_niz_7))
print(wybierz(lista,lambda x: x%3==0))
print(wybierz(lista,podzielna_przez_3))


