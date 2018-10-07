#wypisz liczby od 0 do 100, il podzielne przez 3
j=0
print(f"""Liczby podzielne przez 3 lub 5:""")
for i in range(101):
    if int(i%3)==0 or int(i%5)==0:
        j=j+1
        print(i)

print(f"""W przedziale 0-100 jest {j} liczb podzielnych przez 3 lub 5""")