slownik={'ziemniaki':1.5,'jablka':2.5,'xx':1}

co=input("wpisz co kupujesz: ")
ile=float(input("wpisz ile kilosów: "))
siano=round(float(slownik[co])*ile,2)
print(f"""Cena za {co} to {slownik[co]} za kg, zatem należność wynosi {siano} PLN""")


