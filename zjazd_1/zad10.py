a=float(input("podaj pierwszą liczbę  "))
b=float(input("podaj drugą liczbę  "))
c=input("podaj rodzaj operacji ")

if type(a)==str or type(b)==str:
    print("wpisałeś jakieś pierdy")
else:
    if c=='+':
        print(f"""Wynik: {a+b}""")
    elif c=='-':
        print(f"""Wynik: {a-b}""")
    elif c=='*':
        print(f"""Wynik: {a*b}""")
    elif c=='/':
        if b==0:
            print("nie dziel cholero przez zero")
        else:
            print(f"""Wynik: {a/b}""")
    else:
        print("spitoliłeś operację")