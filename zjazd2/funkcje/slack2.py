# Napisz program, który wczyta od użytkownika tekst, a następnie podwoi w nim co drugi znak i wyświetli wynik,
# np.: ALA MA PSA -> ALLA  MAA PPSAA

def rzezba_w_tekscie(napis):
    napis1 = ''
    i = 0
    for znak in napis:
        if i % 2 != 0:
            napis1 += znak + znak
        else:
            napis1 += znak
        i += 1
    print(napis1)
    return ''


napis = input("podaj tekst, ziomku: ")
print(rzezba_w_tekscie(napis))
