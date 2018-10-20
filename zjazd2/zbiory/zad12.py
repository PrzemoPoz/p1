liczby=[9,1,6,5,2,3,0]


for i in range(len(liczby)):
    indeks_min=i
    for j in range(i+1,len(liczby)):
        if liczby[j] < liczby[indeks_min]:
            indeks_min=j
    liczby[i],liczby[indeks_min]=liczby[indeks_min],liczby[i]
    print(liczby)