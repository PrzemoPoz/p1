skad=str(input("podaj skąd wyjeżdżasz: "))
dokad=str(input("podaj dokąd jedziesz: " ))
dyst=float(input(f'''podaj dystans w km pomiędzy {skad} oraz {dokad}: '''))
spal=float(input("podaj spalanie l/km: "))
cena=float(input("podaj cenę beny za litr: "))
kwota=int(round(dyst/100*spal*cena,))

print(f'''
Miasto A: {skad}
Miasto B: {dokad}
Koszt przejazdu {skad} - {dokad} to {kwota} PLN''')
