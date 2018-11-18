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
dyst_l.grid(row=0,column=0)
dyst = tkinter.Entry(master=root)
dyst.grid(row=0,column=1)
spal_l = tkinter.Label(master=root, text="Spalanie l/km")
spal_l.grid(row=1,column=0)
spal = tkinter.Entry(master=root)
spal.grid(row=1,column=1)
cen_l = tkinter.Label(master=root, text="Cena beny")
cen_l.grid(row=2,column=0)
cen = tkinter.Entry(master=root)
cen.grid(row=2,column=1)

wynik_l = tkinter.Label(master=root, text="Koszt porzejazdu")
wynik_l.grid(row=3,column=0)
wynik = tkinter.Label(master=root, text="-")
wynik.grid(row=3,column=1)
but = tkinter.Button(master=root, text="kliknij ziom", command=oblicz)
but.grid(row=4,column=0)

root.title("SPALANKO")

root.mainloop()
