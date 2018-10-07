from random import randint
i = 1
skarbx = randint(0, 9)
skarby = randint(0, 9)
userx = randint(0, 9)
usery = randint(0, 9)
odl = abs(userx - skarbx) + abs(usery - skarby)

print(f"""Poszukiwania skarbu 3D - copyright by Przemo""")
print(f"""Jesteś w punkcie ({userx},{usery}), skarb jest w ({skarbx},{skarby})""")
while True:
    wejscie = input(f"""Wciśnij a/w/s/d, by dojść do skarbu: """)
    odl <= 0
    if wejscie == "a":
        if userx > 0:
            userx = userx - 1
        else:
            userx = 0
    elif wejscie == "d":
        if userx < 9:
            userx = userx + 1
        else:
            userx = 9
    elif wejscie == "s":
        if usery > 0:
            usery = usery - 1
        else:
            usery = 0
    elif wejscie == "w":
        if usery < 9:
            usery = usery + 1
        else:
            usery = 9
    if abs(userx - skarbx) + abs(usery - skarby) == 0:
        print(f"""Brawo - znalazłeś skarb ukryty w punkcie ({skarbx},{skarby})
        Ogarnąłęś to w {i} ruchów""")
        break
    elif i == 20:
        print(f"""Wyczerałeś możliwą ilość ruchów. NARKA""")
        break
    elif abs(userx - skarbx) + abs(usery - skarby) < odl:
        print(f"""Jesteś w punkcie ({userx},{usery}). Przybliżasz się""")  # (skarb jest w ({skarbx},{skarby})""")
        odl = abs(userx - skarbx) + abs(usery - skarby)
    else:
        print(f"""Jesteś w punkcie ({userx},{usery}). Oddalasz się""")  # (skarb jest w ({skarbx},{skarby})""")
        odl = abs(userx - skarbx) + abs(usery - skarby)
    i = i + 1