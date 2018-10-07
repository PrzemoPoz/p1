#zebranie liczb (nie więcej niż 10)
#obliczenie średniej
lista=[]
i=0
while len(lista)<10:
    lista.append(int(input("Podaj kolejną liczbę do przetwarzania: ")))
print(lista)
print("Średnia wynosi", round(sum(lista)/len(lista),2))
