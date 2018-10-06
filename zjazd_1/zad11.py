x=float(input("podaj pozycję w poziomie  "))
y=float(input("podaj pozycję w pionie  "))


if x>=0 and x<=10:
    poz_x="lewym"
    if y >= 0 and y <= 10:
        poz_y = "dolnym rogu"
    else:
        poz_y = "górnym rogu"
elif x>=90 and x<=100:
    poz_x="prawym"
    if y >= 90 and y <= 100:
        poz_y = "górnym rogu"
    else:
        poz_y = "dolnym rogu"
elif x>10 and x<90:
    if y>10 and y<90:
        poz_x="centrum"
        if y>=0 and y<=10:
            poz_y="dolnej krawędzi"
        else:
            poz_y="górnej krawędzi"
elif y>10 and y<90:
    if x>10 and x<90:
        poz_y="centrum"
        if x>=0 and x<=10:
            poz_x="lewej krawędzi"
        else:
            poz_x="prawej krawędzi"


print (f"""Gracz znajduje się w {poz_x} {poz_y}""")
