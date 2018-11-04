nazwa_pliku = "dane/logs.txt"

kto_ost_in={}
kto_total={}
with open(nazwa_pliku) as f:
    for line in f:
        kto, co, czas = line.split(";")
        czas=int(czas)
        if co=="LOGIN":
            kto_ost_in[kto] = czas
        if co=="LOGOUT":
            kto_total[kto]=kto_total.get(kto,0)+czas-kto_ost_in[kto]
for item in sorted(kto_total.items(),key=lambda x:x[1], reverse=True):
    print(f'''- {item}''')