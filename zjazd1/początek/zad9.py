import datetime
a=float(input("Podaj rok urodzenia: "))


dzis=datetime.datetime.now().year


if dzis-a>=18:
    print(f"""
    Jesteś pełnoletni
    """)
else:
    print(f"""
    Jesteś młody i g(ł)upi
    """)
