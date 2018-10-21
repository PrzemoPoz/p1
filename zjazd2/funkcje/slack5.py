# Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli TRÓJKĄT prostokątny o długości przyprostokątnej X,np.: 5 ->
# *
# * *
# *   *
# *     *
# * * * * *

def trojkat_prostokatny(x):
    i = 1
    while i <= x:
        j = 1
        napis = ''
        while j <= x:
            if i == x or j==1 or i == j:
                napis += '* '
            else:
                napis += '  '
            j += 1
        i += 1
        print(napis)
    return ''


x = int(input("podaj X, ziomku: "))
print(trojkat_prostokatny(x))
