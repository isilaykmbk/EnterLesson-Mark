from tkinter import *
from tkinter import messagebox
import sqlite3



def ogrVerisiGoster():
    cur = baglanti.cursor()
    cur.execute("SELECT * FROM Ogrenciler")
    ogrenciler = cur.fetchall()
    print("Veritabanı kayıtları(Ogrenciler):", ogrenciler)


def dersVerisiGoster():
    cur = baglanti.cursor()
    cur.execute("SELECT * FROM Dersler")
    dersler = cur.fetchall()
    print("Veritabanı kayıtları(Dersler):", dersler)


def notVerisiGoster():
    cur = baglanti.cursor()
    cur.execute("SELECT * FROM Notlar")
    notlar = cur.fetchall()
    print("Veritabanı kayıtları(Notlar):", notlar)


def OgrEkleme():
    """ Bu kısımda dosyaya değil sadece listbox'a ekliyorum """
    Lb1.insert(END, inputOgrNo.get() + ' ' + inputAd.get() + ' ' + inputSoyad.get())
    baglanti.execute("INSERT INTO Ogrenciler VALUES(?,?,?)",
                     [inputOgrNo.get(), inputAd.get(), inputSoyad.get()])
    baglanti.commit()
    ogrVerisiGoster()


def DersEkleme():
    """ Bu kısımda  listbox ve veritabanına ekliyorum """
    Lb2.insert(END, inputDersKodu.get() + ' ' + inputDersAd.get())
    baglanti.execute("INSERT INTO Dersler VALUES(?,?)",
                     [inputDersKodu.get(), inputDersAd.get()])
    baglanti.commit()
    dersVerisiGoster()


def NotEkleme():

    seciliOgrNo = Lb1.get(Lb1.curselection()).split(' ')[0]
    seciliDersKodu = Lb2.get(Lb2.curselection()).split(' ')[0]

    Lb3.insert(END, seciliOgrNo + ' ' + seciliDersKodu + ' ' + inputVizeNotu.get() + ' ' + inputFinalNotu.get())

    baglanti.execute("INSERT INTO Notlar VALUES(?,?,?,?)",
                     [seciliOgrNo, seciliDersKodu, inputVizeNotu.get(), inputFinalNotu.get()])
    baglanti.commit()
    notVerisiGoster()


def OgrSilme():
    """ Bu kısımda  listbox ve veritabanı üzerinden silme yapıyorum"""
    if messagebox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):

        for i in range(Lb1.size(), -1, -1):
            if Lb1.select_includes(i):
                baglanti.execute("DELETE FROM Ogrenciler WHERE OgrNo=?",
                                 [Lb1.get(i).split(' ')[0]])

                baglanti.commit()
                Lb1.delete(i)
        ogrVerisiGoster()


def DersSilme():

    if messagebox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):

        for i in range(Lb2.size(), -1, -1):
            if Lb2.select_includes(i):
                baglanti.execute("DELETE FROM Dersler WHERE DersKodu=?",
                                 [Lb2.get(i).split(' ')[0]])

                baglanti.commit()
                Lb2.delete(i)
        dersVerisiGoster()


def NotSilme():
    """ Bu kısımda  listbox ve veritabanı üzerinden silme yapıyorum"""
    if messagebox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):

        for i in range(Lb3.size(), -1, -1):
            if Lb3.select_includes(i):
                baglanti.execute("DELETE FROM Notlar WHERE OgrNo=? AND DersKodu=?",
                                 Lb3.get(i).split(' ')[0:2])

                baglanti.commit()
                Lb3.delete(i)
        notVerisiGoster()

pencere = Tk()
pencere.title("Işılay tk")

Ogrframe = Frame(pencere, highlightcolor="grey", highlightthickness=5, width=150, height=100, bd=4, relief=GROOVE)
Dersframe = Frame(pencere, highlightcolor="grey", highlightthickness=5, width=350, height=100, bd=4, relief=GROOVE)
Notframe = Frame(pencere, highlightcolor="grey", highlightthickness=5, width=150, height=100, bd=4, relief=GROOVE)

Ogrframe.grid(row=0, column=0)
Dersframe.grid(row=0, column=1)
Notframe.grid(row=0, column=2)

baslik1 = Label(Ogrframe, text="ÖĞRENCİLER", font=("Calibri", 18, "bold"), anchor="e")
baslik1.grid(row=0, column=1)

lblOgrNo = Label(Ogrframe, text="   ÖğrNo :", font=("Calibri 11 bold"))
lblOgrNo.grid(row=1, column=0)

inputOgrNo = Entry(Ogrframe, font="Calibri")
inputOgrNo.grid(row=1, column=1)

lblAd = Label(Ogrframe, text="       Adı  :", font="Calibri 11 bold")
lblAd.grid(row=2, column=0)

inputAd = Entry(Ogrframe, font="Calibri")
inputAd.grid(row=2, column=1)

lblSoyad = Label(Ogrframe, text="  Soyadı :", font=("Calibri 11 bold"), bd=5)
lblSoyad.grid(row=3, column=0)

inputSoyad = Entry(Ogrframe, font="Calibri")
inputSoyad.grid(row=3, column=1)

cmdOgrEkle = Button(Ogrframe, text="Ekle", relief=RAISED, command=OgrEkleme)
cmdOgrEkle.grid(row=4, column=1)

Lb1 = Listbox(Ogrframe, font="Calibri", selectmode="single", exportselection=0)
Lb1.grid(row=5, column=1)

cmdOgrSil = Button(Ogrframe, text="Seçili olanları sil", relief=RAISED, command=OgrSilme)
cmdOgrSil.grid(row=6, column=1)

baslik2 = Label(Dersframe, text="DERSLER", font=("Calibri", 18, "bold"))
baslik2.grid(row=0, column=1)

dersKodu = Label(Dersframe, text="   Ders Kodu :", font=("Calibri 11 bold"))
dersKodu.grid(row=1, column=0)

inputDersKodu = Entry(Dersframe, font="Calibri")
inputDersKodu.grid(row=1, column=1)

lbldersAd = Label(Dersframe, text="       Ders Adı  :", font="Calibri 11 bold")
lbldersAd.grid(row=2, column=0)

inputDersAd = Entry(Dersframe, font="Calibri")
inputDersAd.grid(row=2, column=1)

cmdDersEkle = Button(Dersframe, text="Ekle", relief=RAISED, command=DersEkleme)
cmdDersEkle.grid(row=4, column=1)



Lb2 = Listbox(Dersframe, font="Calibri", selectmode="single", exportselection=0)
Lb2.grid(row=5, column=1)

cmdDersSil = Button(Dersframe, text="Seçili olanları sil", relief=RAISED, command=DersSilme)
cmdDersSil.grid(row=6, column=1)

baslik3 = Label(Notframe, text="NOTLAR", font=("Calibri", 18, "bold"))
baslik3.grid(row=0, column=1)

vizeNotu = Label(Notframe, text="   Vize Notu :", font=("Calibri 11 bold"))
vizeNotu.grid(row=1, column=0)

inputVizeNotu = Entry(Notframe, font="Calibri")
inputVizeNotu.grid(row=1, column=1)

lblFinalNotu = Label(Notframe, text="       Ders Adı  :", font="Calibri 11 bold")
lblFinalNotu.grid(row=2, column=0)

inputFinalNotu = Entry(Notframe, font="Calibri")
inputFinalNotu.grid(row=2, column=1)

cmdNotEkle = Button(Notframe, text="Ekle", relief=RAISED, command=NotEkleme)
cmdNotEkle.grid(row=4, column=1)

Lb3 = Listbox(Notframe, font="Calibri", selectmode="single", exportselection=0)
Lb3.grid(row=5, column=1)

cmdNotSil = Button(Notframe, text="Seçili olanları sil", relief=RAISED, command=NotSilme)
cmdNotSil.grid(row=6, column=1)



baglanti = sqlite3.connect("data.db")

baglanti.execute("CREATE TABLE IF NOT EXISTS Ogrenciler(OgrNo, Ad, Soyad)")
baglanti.execute("CREATE TABLE IF NOT EXISTS Dersler(DersKodu, DersAdı)")
baglanti.execute("CREATE TABLE IF NOT EXISTS Notlar(OgrNo, DersKodu, Vize, Final)")


for kayıt in baglanti.execute("SELECT * FROM Ogrenciler"):
    Lb1.insert(END, kayıt[0] + ' ' + kayıt[1] + ' ' + kayıt[2])
for kayıt in baglanti.execute("SELECT * FROM Dersler"):
    Lb2.insert(END, kayıt[0] + ' ' + kayıt[1])
for kayıt in baglanti.execute("SELECT * FROM Notlar"):
    Lb3.insert(END, kayıt[0] + ' ' + kayıt[1] + ' ' + kayıt[2] + ' ' + kayıt[3])

pencere.mainloop()
baglanti.close()

