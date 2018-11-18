import tkinter


def sumuj():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        wynik.configure(text=a + b)
    except:
        wynik.configure(text="Ty pajacu!")


root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Parametr a")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
b_label = tkinter.Label(master=root, text="Parametr b")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()
wynik_l = tkinter.Label(master=root, text="Wynik")
wynik_l.pack()
wynik = tkinter.Label(master=root, text="-")
wynik.pack()
but = tkinter.Button(master=root, text="kliknij ziom", command=sumuj)
but.pack()
root.pr
root.title("SIEMA")

root.mainloop()
