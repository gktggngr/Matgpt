from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as mb
import math
işlemler = []
pencereler = []
pencere = Tk()
pgen = 200
pyuks = 200
ekrangen = pencere.winfo_screenwidth()
ekranyuks = pencere.winfo_screenheight()
x = (ekrangen - pgen) // 2
y = (ekranyuks - pyuks) // 2
pencere.geometry(f"{pgen}x{pyuks}+{x}+{y}")
pencere.title("Matgpt")
pencere.state("zoomed")
etiket = Label(text="Merhaba! Hangi işlemi yapmak istiyorsunuz?")
etiket.place(relx=0, rely=0)
etiket2 = Label(text="İşleminiz:")
etiket2.place(relx=0, rely=0.026)
def toplama():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Toplama")
    etiket2.config(text="Tamam! Hemen bir toplama işlemi yapabiliriz! Lütfen sayıları girin.")
    etiket3 = Label(pencere2, text="Birinci toplanan:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="İkinci toplanan:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = a + b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a} + {b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısı ile {b} sayısını toplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısı ile {b} sayısını toplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def çıkarma():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Çıkarma")
    etiket2.config(text="Tamam! Hemen bir çıkarma işlemi yapabiliriz! Lütfen sayıları girin.")
    etiket3 = Label(pencere2, text="Eksilen:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Çıkan:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                son = a - b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a} - {b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısından {b} sayısını çıkarırsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısından {b} sayısını çıkarırsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def çarpma():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Çarpma")
    etiket2.config(text="Tamam! Hemen bir çarpma işlemi yapabiliriz! Lütfen sayıları girin.")
    etiket3 = Label(pencere2, text="Birinci çarpan:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="İkinci çarpan:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = a * b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a} x {b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısı ile {b} sayısını çarparsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısı ile {b} sayısını çarparsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def bölme():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Bölme")
    etiket2.config(text="Tamam! Hemen bir bölme işlemi yapabiliriz! Lütfen sayıları girin.")
    etiket3 = Label(pencere2, text="Bölünen:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Bölen:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = a / b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a} ÷ {b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısını {b} sayısına bölersek {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısını {b} sayısına bölersek {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def kare():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Kare")
    etiket2.config(text="Tamam! Hemen bir kare hesaplama işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = a ** 2
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a}² = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının karesini hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının karesini hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def küp():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Küp")
    etiket2.config(text="Tamam! Hemen bir küp hesaplama işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = a ** 3
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a}³ = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının küpünü hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının küpünü hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def üslü():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Üslü İfadeler")
    etiket2.config(text="Tamam! Hemen bir üslü ifade hesaplama işlemi yapabiliriz! Lütfen sayıları girin.")
    etiket3 = Label(pencere2, text="Taban:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Üs(kuvvet):")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = a ** b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a}^{b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının {b}. kuvvetini hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının {b}. kuvvetini hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def karekök():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(penceer2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Karekök")
    etiket2.config(text="Tamam! Hemen bir karekök hesaplama işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.sqrt(a)
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"√{a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının karekökünü hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının karekökünü hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def pi_x():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Pi ile Çarpma")
    etiket2.config(text="Tamam! Hemen bir pi ile çarpma işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if not entry.get():
                    cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                    etiket2.config(text="Hata! Lütfen bir sayı girin.")
                    if cevap == "cancel":
                        pencere2.destroy()
                    else:
                        entry.delete(0, END)
                son = math.pi * a
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"π({math.pi}) x {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısını pi({math.pi}) sayısı ile çarparsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısını pi({math.pi}) sayısı ile çarparsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def euler_x():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Euler ile Çarpma")
    etiket2.config(text="Tamam! Hemen bir euler ile çarpma işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.e * a
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"e({math.e}) x {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısını euler({math.e}) sabiti ile çarparsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısını euler({math.e}) sabiti ile çarparsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def logaritma():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Logaritma")
    etiket2.config(text="Tamam! Hemen bir logaritma hesaplama işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Taban:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = math.log(a, b)
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"log {a}({b} tabanına göre) = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının {b} sayısına göre logaritmasını hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının {b} sayısına göre logaritmasını hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def kosinüs():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Kosinüs")
    etiket2.config(text="Tamam! Hemen bir kosinüs hesaplama işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.cos(math.radians(a))
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"cos {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının kosinüsünü hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının kosinüsünü hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def sinüs():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Sinüs")
    etiket2.config(text="Tamam! Hemen bir sinüs hesaplama işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.sin(math.radians(a))
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"sin {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının sinüsünü hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının sinüsünü hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def tanjant():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Tanjant")
    etiket2.config(text="Tamam! Hemen bir tanjant hesaplama işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.tan(math.radians(a))
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"tan {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının tanjantını hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının tanjantını hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def radyan():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Radyan")
    etiket2.config(text="Tamam! Hemen bir radyan hesaplama işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.radians(a)
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"rad {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının radyanını hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının radyanını hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def ar_top():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Ardışık Toplama")
    etiket2.config(text="Tamam! Hemen bir ardışık toplama işlemi yapabiliriz! Lütfen sayıları girin.")
    etiket3 = Label(pencere2, text="Küçük sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Büyük sayı:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if a > b:
                    cevap3 = mb.showerror("Hata!", "İlk sayı ikinci sayıdan küçük olmalı!", type=mb.RETRYCANCEL, parent=pencere2)
                    if cevap3 == "cancel":
                        pencere2.destroy()
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                if a == b:
                    cevap4 = mb.showerror("Hata!", "Sayılar eşit olamaz!", type=mb.RETRYCANCEL, parent=pencere2)
                    if cevap4 == "cancel":
                        pencere2.destroy()
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                else:
                    if isinstance(a, float):
                        if a.is_integer():
                            a = int(a)
                    if isinstance(b, float):
                        if b.is_integer():
                            b = int(b)
                    son = sum(range(a, b))
                    if isinstance(son, float):
                        if son.is_integer():
                            son = int(son)
                    işlemler.append(f"{a} ile {b} arası toplamı({a} dahil {b} hariç) = {son}")
                    etiket5.config(text="\n".join(işlemler))
                    mb.showinfo("Bilgi", f"{a} sayısı ile {b} sayısının arasındaki sayıları toplarsak({a} dahil {b} hariç) {son} sonucunu buluruz.")
                    etiket2.config(text=f"{a} sayısı ile {b} sayısının arasındaki sayıları toplarsak({a} dahil {b} hariç) {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def p_teoremi():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 80
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Pisagor Teoremi")
    etiket2.config(text="Tamam! Hemen bir Pisagor teoremi hesaplama işlemi yapabiliriz! Lütfen bulunacak değeri seçin.")
    def hipotenüs(): 
        pencere3 = Toplevel()
        pencereler.append(pencere3)
        pgen3 = 150
        pyuks3 = 155
        ekrangen3 = pencere3.winfo_screenwidth()
        ekranyuks3 = pencere3.winfo_screenheight()
        x3 = (ekrangen3 - pgen3) // 2
        y3 = (ekranyuks3 - pyuks3) // 2
        pencere3.geometry(f"{pgen3}x{pyuks3}+{x3}+{y3}")
        pencere3.title("Hipotenüs Bulma")
        etiket2.config(text="Tamam! Hemen bir hipotenüs bulma işlemi yapabiliriz! Lütfen sayıları girin.")
        etiket3 = Label(pencere3, text="Birinci dik kenar:")
        etiket3.pack()
        entry = ttk.Entry(pencere3)
        entry.pack()
        etiket4 = Label(pencere3, text="İkinci dik kenar:")
        etiket4.pack()
        entry2 = ttk.Entry(pencere3)
        entry2.pack()
        def gönder():
            try:
                if not entry.get() or not entry2.get():
                    cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                    etiket2.config(text="Hata! Lütfen bir sayı girin.")
                    if cevap == "cancel":
                        pencere3.destroy()
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                else:
                    a = float(entry.get())
                    b = float(entry2.get())
                    if isinstance(a, float):
                        if a.is_integer():
                            a = int(a)
                    if isinstance(b, float):
                        if b.is_integer():
                            b = int(b)
                    son = math.sqrt(a ** 2 + b ** 2)
                    if isinstance(son, float):
                        if son.is_integer():
                            son = int(son)
                    işlemler.append(f"1. Dik kenar = {a}, 2. Dik kenar = {b}, Hipotenüs = {son}")
                    etiket5.config(text="\n".join(işlemler))
                    mb.showinfo("Bilgi", f"Birinci dik kenarı {a}, ikinci dik kenarı {b} olan bir dik üçgende hipotenüsü hesaplarsak {son} sonucunu buluruz.")
                    etiket2.config(text=f"Birinci dik kenarı {a}, ikinci dik kenarı {b} olan bir dik üçgende hipotenüsü hesaplarsak {son} sonucunu buluruz.")
            except ValueError:
                cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere3)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap2 == "cancel":
                    pencere3.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
        def temizle1():
            entry.delete(0, END)
            entry2.delete(0, END)
        dgm20 = ttk.Button(pencere3, text="Temizle", command=temizle1)
        dgm20.pack(pady=5)
        dgm21 = ttk.Button(pencere3, text="Gönder", command=gönder)
        dgm21.pack()
    def dik_kenar():
        pencere3 = Toplevel()
        pencereler.append(pencere3)
        pgen3 = 150
        pyuks3 = 155
        ekrangen3 = pencere3.winfo_screenwidth()
        ekranyuks3 = pencere3.winfo_screenheight()
        x3 = (ekrangen3 - pgen3) // 2
        y3 = (ekranyuks3 - pyuks3) // 2
        pencere3.geometry(f"{pgen3}x{pyuks3}+{x3}+{y3}")
        pencere3.title("Dik Kenar Bulma")
        etiket2.config(text="Tamam! Hemen bir dik kenar bulma işlemi yapabiliriz! Lütfen sayıları girin.")
        etiket3 = Label(pencere3, text="Dik kenar:")
        etiket3.pack()
        entry = ttk.Entry(pencere3)
        entry.pack()
        etiket4 = Label(pencere3, text="Hipotenüs:")
        etiket4.pack()
        entry2 = ttk.Entry(pencere3)
        entry2.pack()
        def gönder():
            try:
                if not entry.get() or not entry2.get():
                    cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                    etiket2.config(text="Hata! Lütfen bir sayı girin.")
                    if cevap == "cancel":
                        pencere3.destroy()
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                else:
                    a = float(entry.get())
                    b = float(entry2.get())
                    if isinstance(a, float):
                        if a.is_integer():
                            a = int(a)
                    if isinstance(b, float):
                        if b.is_integer():
                            b = int(b)
                    son = math.sqrt(b ** 2 - a ** 2)
                    if isinstance(son, float):
                        if son.is_integer():
                            son = int(son)
                    işlemler.append(f"1. dik kenar = {a}, Hipotenüs = {b}, 2. dik kenar = {son}")
                    etiket5.config(text="\n".join(işlemler))
                    mb.showinfo("Bilgi", f"Birinci dik kenarı {a}, hipotenüsü {b} olan bir dik üçgende ikinci dik kenarı hesaplarsak {son} sonucunu buluruz.")
                    etiket2.config(text=f"Birinci dik kenarı {a}, hipotenüsü {b} olan bir dik üçgende ikinci dik kenarı hesaplarsak {son} sonucunu buluruz.")
            except ValueError:
                cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere3)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap2 == "cancel":
                    pencere3.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
        def temizle1():
            entry.delete(0, END)
            entry2.delete(0, END)
        dgm20 = ttk.Button(pencere3, text="Temizle", command=temizle1)
        dgm20.pack(pady=5)
        dgm21 = ttk.Button(pencere3, text="Gönder", command=gönder)
        dgm21.pack()
    etiket3 = Label(pencere2, text="Bulunacak değer:")
    etiket3.pack()
    dgm26 = ttk.Button(pencere2, text="Dik kenar", command=dik_kenar)
    dgm26.pack()
    dgm27 = ttk.Button(pencere2, text="Hipotenüs", command=hipotenüs)
    dgm27.pack()
def ç_çevresi():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Çemberin Çevresi")
    etiket2.config(text="Tamam! Hemen bir çemberin çevresini hesaplayabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Yarıçap:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = 2 * math.pi * a
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"Yarıçap = {a}, Çevre = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"Yarıçapı {a} olan bir çemberin çevresini hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"Yarıçapı {a} olan bir çemberin çevresini hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def ç_alanı():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Çemberin Alanı")
    etiket2.config(text="Tamam! Hemen bir çemberin alanını hesaplayabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Yarıçap:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.pi * a ** 2
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"Yarıçap = {a}, Alan = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"Yarıçapı {a} olan bir çemberin alanını hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"Yarıçapı {a} olan bir çemberin alanını hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def faktöriyel():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Faktöriyel")
    etiket2.config(text="Tamam! Hemen bir faktöriyel hesaplama işlemi yapabiliriz! Lütfen sayıyı girin.")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.factorial(a)
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a}! = {son}")
                etiket5.config(text="\n".join(işlemler))
                mb.showinfo("Bilgi", f"{a} sayısının faktöriyelini hesaplarsak {son} sonucunu buluruz.")
                etiket2.config(text=f"{a} sayısının faktöriyelini hesaplarsak {son} sonucunu buluruz.")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def basit():
    dgm.config(text="Bilimsel", command=bilimsel)
    dgm6.place_forget()
    dgm7.place_forget()
    dgm8.place_forget()
    dgm9.place_forget()
    dgm10.place_forget()
    dgm11.place_forget()
    dgm12.place_forget()
    dgm13.place_forget()
    dgm14.place_forget()
    dgm15.place_forget()
    dgm16.place_forget()
    dgm17.place_forget()
    dgm22.place_forget()
    dgm23.place_forget()
    dgm24.place_forget()
    dgm25.place_forget()
def bilimsel():
    dgm.config(text="Basit", command=basit)
    dgm6.place(relx=0.797, rely=0.097)
    dgm7.place(relx=0.846, rely=0.097)
    dgm8.place(relx=0.895, rely=0.097)
    dgm9.place(relx=0.944, rely=0.097)
    dgm10.place(relx=0.797, rely=0.129)
    dgm11.place(relx=0.846, rely=0.129)
    dgm12.place(relx=0.895, rely=0.129)
    dgm13.place(relx=0.944, rely=0.129)
    dgm14.place(relx=0.797, rely=0.161)
    dgm15.place(relx=0.846, rely=0.161)
    dgm16.place(relx=0.895, rely=0.161)
    dgm17.place(relx=0.944, rely=0.161)
    dgm22.place(relx=0.797, rely=0.193)
    dgm23.place(relx=0.846, rely=0.193)
    dgm24.place(relx=0.895, rely=0.193)
    dgm25.place(relx=0.944, rely=0.193)
def göster():
    dgm18.config(text="Geçmişi gizle", command=gizle)
    etiket5.place(relx=0.026, rely=0.1)
    dgm19.place(relx=0.078, rely=0.0652)
def gizle():
    dgm18.config(text="Geçmişi göster", command=göster)
    etiket5.place_forget()
    dgm19.place_forget()
def temizle():
    global işlemler
    if not işlemler:
        mb.showerror("Hata!", "İşlem geçmişi zaten boş!")
    else:
        cevap = mb.askquestion("Soru", "İşlem geçmişini temizlemek istediğinize emin misiniz?")
        if cevap == "yes":
            işlemler.clear()
            etiket5.config(text="\n".join(işlemler))
def çıkış():
    cevap = mb.askquestion("Soru", "Programdan çıkmak istediğinze emin misiniz?")
    if cevap == "yes":
        pencere.destroy()
etiket5 = Label(text="\n".join(işlemler))
menü = Menu(pencere)
pencere.config(menu=menü)
menü1 = Menu(menü, tearoff=0)
menü.add_cascade(label="Çıkış", menu=menü1)
menü1.add_command(label="Çıkış", command=çıkış)
dgm = ttk.Button(text="Bilimsel", command=bilimsel)
dgm.place(relx=0.871, rely=0.032)
dgm2 = ttk.Button(text="Toplama", command=toplama)
dgm2.place(relx=0.797, rely=0.065)
dgm3 = ttk.Button(text="Çıkarma", command=çıkarma)
dgm3.place(relx=0.846, rely=0.065)
dgm4 = ttk.Button(text="Çarpma", command=çarpma)
dgm4.place(relx=0.895, rely=0.065)
dgm5 = ttk.Button(text="Bölme", command=bölme)
dgm5.place(relx=0.944, rely=0.065)
dgm6 = ttk.Button(text="Kare", command=kare)
dgm7 = ttk.Button(text="Küp", command=küp)
dgm8 = ttk.Button(text="Üslü", command=üslü)
dgm9 = ttk.Button(text="Karekök", command=karekök)
dgm10 = ttk.Button(text="Pi x", command=pi_x)
dgm11 = ttk.Button(text="Euler x", command=euler_x)
dgm12 = ttk.Button(text="log", command=logaritma)
dgm13 = ttk.Button(text="cos", command=kosinüs)
dgm14 = ttk.Button(text="sin", command=sinüs)
dgm15 = ttk.Button(text="tan", command=tanjant)
dgm16 = ttk.Button(text="rad", command=radyan)
dgm17 = ttk.Button(text="Ar. Top", command=ar_top)
dgm22 = ttk.Button(text="Ç. Çevresi", command=ç_çevresi)
dgm23 = ttk.Button(text="Ç. Alanı", command=ç_alanı)
dgm24 = ttk.Button(text="P. Teoremi", command=p_teoremi)
dgm25 = ttk.Button(text="Faktöriyel", command=faktöriyel)
dgm18 = ttk.Button(text="Geçmişi göster", command=göster)
dgm18.place(relx=0.026, rely=0.0652)
dgm19 = ttk.Button(text="Geçmişi temizle", command=temizle)
pencere.mainloop()