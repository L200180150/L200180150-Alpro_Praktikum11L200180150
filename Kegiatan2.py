
from tkinter import *

my_app = Tk(className='Kalkulator')

l1 = Label(my_app, text='Angka 1')
l1.grid(row=0, column=0, sticky=W)
e1 = Entry(my_app)
e1.grid(row=0, column=1, sticky=W)
L2 = Label(my_app, text='Angka 2')
L2.grid(row=1, column=0, sticky=W)
e2 = Entry(my_app)
e2.grid(row=1, column=1, sticky=W)

def tambah():
    a = float(e1.get())
    b = float(e2.get())
    jumlah = a + b
    L4.config(text=jumlah)

def kurang():
    c = float(e1.get())
    d = float(e2.get())
    jumlah2 = c - d
    L4.config(text=jumlah2)

def kali():
    e = float(e1.get())
    f = float(e2.get())
    jumlah3 = e * f
    L4.config(text=jumlah3)

def bagi():
    a = float(e1.get())
    b = float(e2.get())
    jumlah4 = a / b
    L4.config(text=jumlah4)

b1 = Button(my_app, text="+", command=tambah)
b1.grid(row=4, column=1, sticky=W)
b2 = Button(my_app, text="-", command=kurang)
b2.place(x=80, y=42)
b3 = Button(my_app, text="x", command=kali)
b3.place(x=120, y=42)
b4 = Button(my_app, text=":", command=bagi)
b4.place(x=150, y=42)
L3 = Label(my_app, text="Hasil")
L3.grid(row=5, column=0, sticky=W)
L4 = Label(my_app, text="0")
L4.grid(row=5, column=1, sticky=E)
my_app.mainloop()
