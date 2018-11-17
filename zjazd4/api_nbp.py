import json
import urllib.request

with urllib.request.urlopen('http://api.nbp.pl/api/exchangerates/tables/a/?format=json') as nbp:
    kursy = json.loads(nbp.read())
    rates = kursy[0]['rates']
for r in rates:
    print(f"- {r['code']} {r['mid']}")

waluta = input("podaj walutę: ")
ilosc = float(input("ile wymieniasz: "))
for r in rates:
    if r['code']==waluta:
        kurs=r['mid']
kwota=ilosc*kurs

print(f'''Do zapłaty: {kwota} PLN''')
