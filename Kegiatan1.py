from tkinter import *

my_app = Tk(className='Aplikasi penjawab otomatis')
L1 = Label(my_app, text="Nama mahasiswa")
L1.grid(row=0, column=0)
E1 = Entry(my_app)
E1.grid(row=0, column=1)
L2 = Label(my_app, text="NIM")
L2.grid(row=1, column=0)
E2 = Entry(my_app)
E2.grid(row=1, column=1)
L3 = Label(my_app, text="Buku favorit")
L3.grid(row=2, column=0)
E3 = Entry(my_app)
E3.grid(row=2, column=1)
L4 = Label(my_app, text="Idola di kalangan sahabat")
L4.grid(row=3, column=0)
E4 = Entry(my_app)
E4.grid(row=3, column=1)
L5 = Label(my_app, text="Motto")
L5.grid(row=4, column=0)
E5 = Entry(my_app)
E5.grid(row=4, column=1)

def tampil_pesan():
            my_app.destroy()

B = Button(my_app, text ="Tutup", command=tampil_pesan)
B.grid(row=6, column=1)
my_app.mainloop()

