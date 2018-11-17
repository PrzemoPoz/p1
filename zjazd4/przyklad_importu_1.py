import sys

print(sys.path)

import zjazd3.klasy.zad6 as pt

v1 = pt.Vector(1, 2)
v2 = pt.Vector(1, 2)
v3 = v1 + v2

print(v3.x, v3.y)
l