from tkinter import *

my_app = Tk(className='Bangun Geometri')

L1 = Label(my_app, text='Bangun Geometri', font=('Calibri', 18, 'bold'))
L1.grid(row=0, column=0, sticky=W)
L2 = Label(my_app, text='Menurut Travers dkk(1987:6) mengatakan bahwa Geometri adalah ilmu yang membahas tentang hubungan antaratitik, garis, sudut, bidang, dan bangun-bangun ruang.')
L2.grid(row=1, column=0, sticky=W)
L3 = Label(my_app, text='Dimensi pada Geometri dibedakan menjadi 2, yaitu Dimensi dua dan Dimensi tiga')
L3.grid(row=2, column=0, sticky=W)
L4 = Label(my_app, text='Contoh benda Geometri adalah permukaan kertas, bola, topi ulang tahun, dll')
L4.grid(row=3, column=0, sticky=W)
L5 = Label(my_app, text='Bangun Geometri Persegi', font=('Calibri', 12, 'bold'))
L5.grid(row=4, column=0, sticky=W)
L6 = Label(my_app, text='Parameter panjang :')
L6.grid(row=5, column=0, sticky=W)
e1 = Entry(my_app)
e1.place(x=130, y=117)
L7 = Label(my_app, text='Parameter luas :')
L7.grid(row=6, column=0, sticky=W)
e2 = Entry(my_app)
e2.place(x=130, y=140)
L8 = Label(my_app, text='Parameter tinggi :')
L8.grid(row=7, column=0, sticky=W)
e3 = Entry(my_app)
e3.place(x=130, y=165)

def luas():
    a = float(e1.get())
    b = float(e2.get())
    c = float(e3.get())
    hasil = 2 * (a*b+a*c+b*c)
    L8.config(text=hasil)

b1 = Button(my_app, text='Hitung Luas', command=luas)
b1.grid(row=10, column=0, sticky=W)
L7 = Label(my_app, text='Luas =', font=('Calibri', 12, 'bold'))
L7.place(x=115, y=185)
L8 = Label(my_app, text='0', font=('Calibri', 12,'bold'))
L8.place(x=185, y=185)

my_app.mainloop
