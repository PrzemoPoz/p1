# zamiana elementu największego z najmniejszym

lista = [1, 2, 3, 4, 5]

maks = lista.index(max(lista))
mini = lista.index(min(lista))
maks_n = lista[maks]
mini_n = lista[mini]
lista[maks] = mini_n
lista[mini] = maks_n
print(lista)
