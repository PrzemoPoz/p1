def przytnij(data, start, stop):
    wyj = []
    for liczba in data:
        if start(liczba):
            if not stop(liczba):
                wyj.append(liczba)
            else:
                wyj.append(liczba)
                break
    return wyj
    print(wyj)

data = [1, 2, 3, 4, 5, 6, 7]
start = lambda x: x > 3
stop = lambda x: x == 6
print(przytnij(data,start,stop))

def test_przytnij():
    assert przytnij(data=[1, 2, 3, 4, 5, 6, 7],
                    start=lambda x: x > 3,
                    stop=lambda x: x == 6
                    ) == [4, 5, 6]
