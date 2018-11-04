nazwa_pliku = "dane/emails.txt"

mejle=[]
with open(nazwa_pliku) as f:
    for line in f:
        line=line.lower()
        line=line.replace(" ","")
        if mejle.count(line)==0 and line.count('@')==1:
            mejle.append(line)

with open("dane/adresy.txt", 'w', encoding='UTF-8') as f1:
    for x in sorted(mejle):
        f1.write(x)