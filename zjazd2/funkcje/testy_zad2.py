from .zad2opt import wiecej_niz

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0)==set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaaaabbbccd",2)=={'a','b'}