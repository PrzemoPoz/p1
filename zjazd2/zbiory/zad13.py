lista1={}
lista1=[x/10 for x in range(1,11)]
print(lista1)

lista2=[(x,x**2,x**3) for x in range (-10,11)]
print(lista2)



napisy=('jędrzej','przemektusz','vejderova')
lista3=[(slowo,len(slowo)) for slowo in napisy]

print(lista3)