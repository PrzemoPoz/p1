slowo = input("Podaj słowo, w kórym policzę znaki: ")
slowo = slowo.lower()
slownik={}

for znak in slowo:
    slownik[znak] = slowo.count(znak)
for rzeczy in slownik:
    print(rzeczy, slownik[rzeczy])