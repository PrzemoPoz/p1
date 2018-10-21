# Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w dwóch linijkach naprzemiennie, np.: HELLO STRANGER! ->
# H L O S R N E !
# E L   T A G R

def przestawka(napis):
    i = 0
    napis1=""
    napis2=""
    for znak in napis:
        if i % 2 == 0:
            napis1 += znak
            napis1+=" "
        else:
            napis2 += znak
            napis2 += " "
        i += 1
    print(napis1)
    print(" ",napis2)
    return ''

napis = input("podaj tekst, ziomku: ")
print(przestawka(napis))