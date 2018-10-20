def wiecej_niz(napis,max_licz):
    napis = napis.lower()
    znaki={}
    tekst=set()
    for znak in napis:
        znaki[znak]=znaki.get(znak,0)+1
    for xx in znaki:
        if znaki[xx]>max_licz:
            tekst.add(xx)
    return tekst

#napis=input("wpisz tekst: ")
#max_licz=int(input("jaki maks? "))
#print(wiecej_niz(napis,max_licz))


#def test_wiecej_niz_dla_pustego_napisu():
#    assert wiecej_niz("",0)==set()


#def test_wiecej_niz_dla_niepustego_napisu():
#    assert wiecej_niz("aaaaabbbccd",2)==set('a','b')