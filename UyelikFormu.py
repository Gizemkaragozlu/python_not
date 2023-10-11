from tkinter import * # tkinter versiyonlara göre kendiliğinden gelebiliyor yoksa da pip install diyip indirebiliriz.
from tkinter import messagebox
import os

window = Tk()#pencere oluştur
window.title('Üyelik Formu')#başlık
window.geometry('500x500+300+100')#pencerenin genişlkik ve yüksekliği
window.resizable(height=False,width=False)#yükseklik ve genişlik sabit kalsın
window.iconbitmap('key.ico')#icon
window.configure(bg='#45B39D')#renk
#----------Frame Satır Kolon Belirleme Alanı------------------------------
frame1 = Frame(window,bg='#45B39D')
frame1.grid(row=0, column=0)#hangi kolonda veya satırda olduğunu gösterir
frame2 = Frame(window,bg='#45B39D')
frame2.grid(row=0, column=1)
frame3 = Frame(window,bg='#45B39D')
frame3.grid(row=0, column=2)
frame4 = Frame(window,bg='#45B39D')
frame4.grid(row=1, column=2)
#-------------Canvas------------------------------
frame5 = Frame(window,bg='#45B39D')
frame5.place(x=0, y=230)
cv = Canvas(frame5,bg='#45B39D', highlightthickness=10, highlightbackground='#45B39D')
cv.create_line(100, 10, 500, 10)
cv.pack()

#----------------Label Alnı------------------------
Label(frame1,text='Ad', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()# text,font,arkaplan ve x y konumu
Label(frame1,text='Soyad', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()
Label(frame1,text='Yaş', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()
Label(frame1,text='Doğum', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()
Label(frame1,text='Cinsiyet', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()
#--------------Label Arasında :--------------------------
Label(frame2,text=':', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()
Label(frame2,text=':', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()
Label(frame2,text=':', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()
Label(frame2,text=':', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()
Label(frame2,text=':', font=('Arial 12 bold'),bg='#45B39D',padx=5,pady=5,).pack()
#---------------Ad Soyad İnput Alanı----------------------------
Entry(frame3,font=('Arial 12 bold'),bg='#ECE8F0',justify='left').pack(padx=5,pady=5)# input alanı
Entry(frame3,font=('Arial 12 bold'),bg='#ECE8F0',justify='left').pack(padx=5,pady=5)
#--------------Kaydet Temizle Butonu--------------------------
def clickSave():
    messagebox.askokcancel('Dikkat', 'Verileri Kaydedildi')
btnKaydet=Button(window,text='Kaydet', font='Arial 13 bold',bg='green',width=12,command=clickSave).place(x=100,y=270)
Button(window,text='Temizle', font='Arial 13 bold',bg='yellow',width=12).place(x=260,y=270)
#------------- Yükle Butonu----------------------------
photo = PhotoImage(file='user.png')
photoResized = photo.subsample(1,1)
def clickLoad():
     os.startfile(r'C:\Users\Teampro\Desktop')#masaüstünde dosyayı çekmemizi sağlar
Button(window,text='Yükle',image=photoResized,compound=TOP,command=clickLoad).place(x=325,y=11)
#-----------Yaş-----------------------------
Spinbox(frame3,from_=18,to=60,font=('Arial 12 bold'), bg='#ECE8F0',justify='center',width=19).pack(padx=5,pady=5)
#-----------Aylar-----------------------------
optionList= [
    'Ocak',
    'Şubat',
    'Mart',
    'Nisan',
    'Mayıs',
    'Haziran',
    'Temmuz',
    'Ağustos',
    'Eylül',
    'Ekim',
    'Kasım',
    'Aralık'
]
sval = StringVar(frame3)
sval.set(optionList[0])
opm1 = OptionMenu(frame3,sval,*optionList)
opm1.config(width='24',bg='#ECE8F0')
opm1.pack(padx=5,pady=5)
#------------Cinsiyet--------------------
iVar = IntVar()
def sel():
    selection = 'Selected radiobutton val =' + str(iVar.get())
    print(selection)
rd1 = Radiobutton(frame3,text='Erkek',variable=iVar,value=1,command=sel,font=('Arial 12'),bg='#45B39D',width=7 )
rd2 = Radiobutton(frame3,text='Kadın',variable=iVar,value=2,command=sel,font=('Arial 12'),bg='#45B39D',width=7)
rd1.pack(side='left')
rd2.pack(side='left')
#-------------Checkbox------------------------------
chk = Checkbutton(frame4,text='Formu okudum onaylıyorum.')



chk.pack()
window.mainloop()#ekranda sürekli kalsın

# Not: Python dosyasını EXE dönüştürmek için Terminalde pip install pyinstaller kütüphanesi indirilmelidir,
# Terminalde : pyinstaller --onefile UyelikFormu.py (EXE dönüştürülmek istenenen py uzantılı proje yazılır),
# Projenizin olduğu klasüre dist klasörün altına oluşturulur.
# Klasör olarak indirilmek istenirse Terminale: pyinstaller --onedir UyelikFormu.py yazmak yeterli olacaktır.
# Resimli,ikonlu olan projelerde Exe oluşturduğunuz klasörün içine resimleri atmalısınız aksi halde hata alırsınız.

