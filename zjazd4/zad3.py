import tkinter

def oblicz():
    try:
        a = float(dyst.get())
        b = float(spal.get())
        c = float(cen.get())
        wynik.configure(text=round(a/100*b*c,2))
    except:
        wynik.configure(text="Ty pajacu!")


root = tkinter.Tk()
dyst_l = tkinter.Label(master=root, text="Dystans w km")
dyst_l.pack()
dyst = tkinter.Entry(master=root)
dyst.pack()
spal_l = tkinter.Label(master=root, text="Spalanie l/km")
spal_l.pack()
spal = tkinter.Entry(master=root)
spal.pack()
cen_l = tkinter.Label(master=root, text="Cena beny")
cen_l.pack()
cen = tkinter.Entry(master=root)
cen.pack()

wynik_l = tkinter.Label(master=root, text="Koszt porzejazdu")
wynik_l.pack()
wynik = tkinter.Label(master=root, text="-")
wynik.pack()
but = tkinter.Button(master=root, text="kliknij ziom", command=oblicz)
but.pack()

root.title("SPALANKO")

root.mainloop()
