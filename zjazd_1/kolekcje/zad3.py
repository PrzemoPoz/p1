lista=[-1,2,-3,4,-5,6,-7,8,-9,10]
uj=0
dod=0
zer=0
for i in lista:
    if lista[i-1]<0:
        uj=uj+1
    elif lista[i-1]>0:
        dod=dod+1
    else:
        zer=zer+1

print(f"""
{uj} ujemnych
{dod} dodatnich
{zer} zer""")