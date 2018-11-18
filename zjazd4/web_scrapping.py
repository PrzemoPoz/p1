from requests import get
from bs4 import BeautifulSoup

url = "https://helion.pl/search?qa=&serwisyall=&szukaj=python&wprzyg=&wsprzed=&wyczerp=#"

response = get(url)
# print(dir(response))
# print(response.text)
new=[]

html_soup=BeautifulSoup(response.text,'html.parser')

books=html_soup.find_all('div',class_="book-info")
for b in books:
    new.append(b.a.text)
    old=[
'Python 3. Kurs video. Kompendium efektywnego Pythonisty',
'Python. Wprowadzenie. Wydanie IV',
'Testy automatyczne kodu Python. Kurs video. Pisanie testów jednostkowych od podstaw',
'Python 3. Proste wprowadzenie do fascynującego świata programowania',
'Python. Kurs video. Poziom pierwszy. Podstawy programowania i tworzenia aplikacji',
'Python w analizie danych. Przetwarzanie danych za pomocą pakietów Pandas i NumPy oraz środowiska IPython. Wydanie II',
'Black Hat Python. Język Python dla hakerów i pentesterów',
'Deep Learning. Uczenie głębokie z językiem Python. Sztuczna inteligencja i sieci neuronowe',
'Python. Uczenie maszynowe',
'Python. Instrukcje dla programisty',
'Python. Rusz głową! Wydanie II',
'Python dla każdego. Podstawy programowania. Wydanie III',
'Python 3. Kolejne lekcje dla nowych programistów',
'Python na start! Programowanie dla nastolatków',
'Python. Receptury. Wydanie III',
'Tablice informatyczne. Python',
'Python dla profesjonalistów. Debugowanie, testowanie i utrzymywanie kodu',
'Python. Podstawy nauki o danych. Wydanie II',
'Efektywny Python. 59 sposobów na lepszy kod',
'Informatyka Europejczyka. Python. Programowanie na maturze',
    ]

if new==old:
    print("idento")
else:
    print("jest coś nowego")