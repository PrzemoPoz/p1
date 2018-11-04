# file=open("dane/przykładowy_excel.csv")
# print(file.read())
# file.close()

with open("dane/przykładowy_excel.csv") as f:
    for line in f:
        print(line.upper(),end="")

with open("dane/nowy_plik.txt", 'w', encoding='UTF-8') as f:
    f.write('jakiś tekst')

with open("dane\\nowy_plik1.txt", 'w', encoding='UTF-8') as f:
    f.write('jakiś tekst1')
