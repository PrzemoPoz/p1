def kalkulator(a,b,operacja="+",opis=""):
    #domylślna operacja to dodawanie operacja="+"
    if opis:
            print(opis)
    if operacja=="+":
        return  a+b
    elif operacja=="-":
        return a-b



print(kalkulator(1,2))
print(kalkulator(1,2,"-"))
print(kalkulator(1,2,"-","przykładowy opis"))

print()
print()



def foo2(*args):
    print(args)

x={"tekst1","tekst2","tekst3"}
foo2(*x)