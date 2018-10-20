ile_d=int(input("podaj ile dni wklepiesz: "))
i=1
suma=0
temp=0
maks=-1000
mini=1000

while i<=ile_d:

    temp = float(input(f"""podaj temperaturę dniu: {i} : """))
    if temp>maks:
        maks=temp
        imaks=i
    if temp<mini:
        mini=temp
        imini=i
    suma=suma+temp
    i=i+1

print(f"""Średnia temperatura dla {i-1} dni to {round(suma/(i-1),2)}
Najzimniej było w dniu {imini}, gdy było {mini} stopni
Najcieplej było w dniu {imaks}, gdy było {maks} stopni""")

