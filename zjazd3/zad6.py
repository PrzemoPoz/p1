class Vector():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)

    def __mul__(self, liczba):
        return Vector(self.x*liczba,self.y*liczba)

    def __eq__(self, other):
        return ((self.x)**2+(self.y)**2)**0.5==((other.x)**2+(other.y)**2)**0.5

vector1=Vector(1,2)
vector2=Vector(1,2)

vector3=vector1+vector2
print(vector3.x,vector3.y)

vector3=vector1*3
print(vector3.x,vector3.y)

print(vector1==vector2)

