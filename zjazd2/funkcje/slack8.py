# Napisz program "numer.py", który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:
# a) znaki nie będące cyframi mają być ignorowane
# b) konwertujemy cyfry, nie liczby, a zatem:
# - 911 to "dziewięć jeden jeden"
# - 1100 to "jeden jeden zero zero"

def numer(ciag):
    tekst=''
    slownik = {'1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery', '5': 'pięć', '6': 'cześć', '7': 'siedem', '8': 'osiem',
               '9': 'dziewięć'}
    for cyfra in ciag:
        tekst += slownik[cyfra] + " "
    return tekst



ciag = input("podaj ciąg znaków, ziom: ")
print(numer(ciag))
