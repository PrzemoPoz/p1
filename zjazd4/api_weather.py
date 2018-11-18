import json
import urllib.request
import datetime
import tkinter

def oblicz():
    miasto = city.get()
    texxt=""
    data1 = f'''{datetime.datetime.today().year}/{datetime.datetime.today().month}/{datetime.datetime.today().day}'''

    with urllib.request.urlopen(f'''https://www.metaweather.com/api/location/search/?query={miasto}''') as link:
        szuk = json.loads(link.read())
        idmiasta = szuk[0]['woeid']

    with urllib.request.urlopen(f'''https://www.metaweather.com/api/location/{idmiasta}/{data1}''') as link:
        szuk = json.loads(link.read())
        i = 0
        for i, s in enumerate(szuk[0], start=1):
            if i > 1:
                 try:
                    # print(s, round(szuk[0][s] * 1, 2))
                    texxt += f'''{s} {round(szuk[0][s] * 1,2)}\n'''
                 except:
                     # print(s, szuk[0][s])
                     texxt += f'''{s} {szuk[0][s]}\n'''
            wynik.configure(text=texxt)

root = tkinter.Tk()
city_l = tkinter.Label(master=root, text="Wpisz nazwę miasta")
city_l.pack()
city = tkinter.Entry(master=root)
city.pack()

wynik_l = tkinter.Label(master=root, text="Pogoda: ")
wynik_l.pack()
wynik = tkinter.Label(master=root, text="-")
wynik.pack()
but = tkinter.Button(master=root, text="kliknij ziom", command=oblicz)
but.pack()

root.title("POGODYNKA")

root.mainloop()
