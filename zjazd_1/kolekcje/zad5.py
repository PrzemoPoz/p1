# tablica mnożenia
i=0
j=0
# lista=[]
#
# for i in range(10):
#     print(i*j,i*(j+1),i*(j+2),i*(j+3),i*(j+4),i*(j+5),i*(j+6),i*(j+7),i*(j+8),i*(j+9))
#
# print()
#
# for i in range(10):
#     lista = []
#     for j in range(10):
#         lista.append(i*j)
#     print(lista)

print()
print(sep="\t",end="\t")

for i in range(10):
    print(i,sep=" ",end="\t")
print()
print()
for i in range(10):
    print(i,"  ", end="")
    for j in range(10):
        print(i*j, end="\t")
    print()