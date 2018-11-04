liczba=float(input("podaj liczbę do weryfikacji "))

print(f"""
Podzielna przez 2, podzielna przez 3 i większa od 10 lub jest to liczba 7: {(int(liczba%2)==0 and int(liczba%3)==0 and liczba>10) or liczba==7}
""")

if (int(liczba%2)==0 and int(liczba%3)==0 and liczba>10) or liczba==7:
    print("ok")
elif liczba==100:
    print("mejbi")
else:
    print("nie ok")