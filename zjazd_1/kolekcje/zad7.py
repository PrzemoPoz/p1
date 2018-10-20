slowo=input("Podaj słowo, w kórym zliczę samogłoski: ")

slowo=slowo.lower()
licz=slowo.count('a')+slowo.count('e')+slowo.count('i')+slowo.count('o')+slowo.count('u')+slowo.count('y')
print(f"""W słowie {slowo} znajduje się {licz} samogłosek""")