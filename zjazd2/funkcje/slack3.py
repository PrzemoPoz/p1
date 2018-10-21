# Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli kwadrat z gwiazdek o długości boku X, np.: 4 ->
# ****
# *  *
# *  *
# ****
def kwadrat(x):
    i = 1
    while i <= x:
        j = 1
        napis = ''
        while j <= x:
            if i == 1 or j==1 or j == x or i == x:
                napis += '* '
            else:
                napis += '  '
            j += 1
        i += 1
        print(napis)
    return ''


x = int(input("podaj X, ziomku: "))
print(kwadrat(x))
