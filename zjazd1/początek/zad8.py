print("podaj wymiary opakowania w cm ")

a=float(input("wysokość: "))
b=float(input("szerokość: "))
c=float(input("głębokość: "))

xxx=round(a*b*c/1000,2)

if xxx>1:
    print(f"""
    Objętość wynosi {xxx} L i jest większa od 1. litra - nie wierzysz? - wejdź na http://wwww.google.pl
    """)
else:
    print(f"""
    Objętość wynosi {xxx} L i nie jest większa od 1. litra
    """)
