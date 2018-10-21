# Napisz program "prk.py", który obliczy wszystkie pierwiastki rzeczywiste równania kwadratowego o postaci ax2+bx+c=0,
# gdzie a, b i c podaje użytkownik.
# Program powinien na początku sprawdzić, czy wprowadzone równanie jest rzeczywiście kwadratowe.

def prk(a,b,c):
    delta=b**2-4*a*c
    if delta<0:
        return "brak wyników"
    elif delta>0:
        x2=(-b-delta**0.5)/(2*a)
        x1=(-b+delta**0.5)/(2*a)
        return round(x1,2),round(x2,2)
    else:
        x1=-b/(2*a)
        x2=x1
        return round(x1,2),round(x2,2)


a=int(input("podaj a, ziomku: "))
b=int(input("podaj b, ziomku: "))
c=int(input("podaj c, ziomku: "))

print(prk(a,b,c))