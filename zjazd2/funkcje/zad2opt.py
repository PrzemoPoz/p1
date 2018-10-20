def wiecej_niz(napis,max_licz):
    napis = napis.lower()
    return {znak for znak in napis if napis.lower().count(znak)>max_licz}
    print({znak for znak in napis if napis.lower().count(znak)>max_licz})
#napis=input("wpisz tekst: ")
#max_licz=int(input("jaki maks? "))
#print(wiecej_niz(napis,max_licz))

