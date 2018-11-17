import zjazd4.mathematica.geometry.figures as geo

def test_square_area1():
    assert geo.square_area(3)==9

def test_square_area2():
    assert geo.square_area(4)==16

def test_square_triangle1():
    assert geo.triangle_area(2,2)==2

def test_square_triangle2():
    assert geo.triangle_area(1,6)==3

