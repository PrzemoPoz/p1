



def foo2(x,*args,**kwargs):
    # print("cena",x)
    # print("args",args)
    # print("args", kwargs)

    for tekst in args:
        print(tekst)

    for key in kwargs:
        print(key,kwargs[key])


print(foo2(10))