import sys

if len(sys.argv) > 1:
    nazwa_pliku = "dane/" + sys.argv[1]
    with open(nazwa_pliku) as f:
        for i, line in enumerate(f, start=1):
            print(i, line.lower(), end="")
else:
    print("podaj poprawny plik, ziomblu")
