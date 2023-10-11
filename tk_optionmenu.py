from tkinter import *
# ---OptionMenu----
# font         'yazı tipi kalınlığı'
# bg           'arka plan rengi'
# fg           'yazı sayı rengi'
# cursor       'mouse şekli'
# width        'genişlik'
# height       'yükseklik'
# padx  # pady 'yukarıdan ve aşağıdan verilen boşluk'
# anchor       'yazının konumu'
# relief       'çerçeve derinlik, dışa dönük vb...'
# image        'resim ikon eklenir'
# compound     'yazı resmin hangi yönünde olacağı'

# get()        'get bir methoddur, ekrana verileri yazdırmamızı sağlar'
# set()

window = Tk()
window.geometry('500x500')
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
# sval = StringVar(value='Ocak') # ilk açıldığında ne gözükeceği
# sval = StringVar(value=optionList[0]) # optionList 0. indexi
sval = StringVar()
sval.set(optionList[2]) # ekran açılır açılmaz hangi indexdeki değeri görmek isteneceği
opm1 = (OptionMenu(window, sval,*optionList))
# listenin açık halini alt alta sıralı bir şekilde görmek için önine * katıyoruz.
# variable ve value

# opm2 = (OptionMenu(window, sval,*optionList))

photo = PhotoImage(file='user.png')
photoResized = photo.subsample(5,5)
opm1.config(font=('Times 15 bold'),
            bg='pink',
            fg='white',
            cursor='spider',
            anchor='sw',
            relief=GROOVE,
            image= photoResized,
            compound=LEFT
            ) #config yazmadan direkt font kullanılamaz
opm1.pack()

# opm2.config(font=('Times 15 bold'),
#             bg='pink',
#             fg='white',
#             cursor='spider',
#             padx=10,
#             pady=10
#             ) #config yazmadan direkt font kullanılamaz
# opm2.pack()

def clicked_button():
     print(sval.get()) #terminal ekranında seçilen değerleri gösterir

Button(window,text='Tıklandı', command=clicked_button).pack(pady=20)





window.mainloop()