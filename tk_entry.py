from tkinter import *

window = Tk()
window.geometry('500x500')

#----PARAMETRELER-----------
# bd = derinlik
# width = input alanını genişliğini belirler
# cursor = mouse ikonu değişir
# relief = çerçeve şekli
# relief (FLAT,RAISED,SUNKEN,GROOVE,RIDGE)
# show = password alanı gibi kullanılır
# justify = yazının hangi tarafta olacağı right, left vb..
# selectbackground = yazıyı mousel ile seçince hangi renk olsun
# selectborderwidth = border kalınlığı ne olsun
# selectforeground = seçili yazı rengi ne olsun
# state(disabled,normal) = kullanılabilirliği kapatıp açmamızı sağlar
# textvariable = ekran açılır açılmaz bir text vermemizi sağlar.

# Entry(window, font=('Arial 14 bold'), bg='pink',fg='white',bd=5,width=15,show='*',justify='right').pack()#input alanı
# Entry(window,selectbackground='red',selectborderwidth=8,selectforeground='white').pack()
# Entry(window).pack(pady=20)
# Entry(window, state='disabled').pack(pady=20)# disabled input olarak veri girilemez pady ise entr alanı alt  alta olsun
# svar = StringVar(window, value='Adınızı giriniz..')
# Entry(window,textvariable=svar).pack()

#-----METHODLAR------
# get() = veriyi yakalar
# delete() = yazıyı silmeye nereden başlanacğı
# insert(index, s) = belirtilen indexden başlayıp belirtilen string ifadeyi ekler
# select_to(index) = belitilen indexden başlanıp o texti seçili yapar
# select_range(start, end) = iki indekx arasından seçili yap başlangıç ve bitiş indexi
# select_present() = herhangi seçili bir text varsa true döner yoksa da false döner
# icursor(index) = imleci seçili indexe atar

ent1 = Entry(window)
ent1.pack(pady=20)

# def clicked_button():
#     print(ent1.get())
def clicked_button():
    # print(ent1.delete(0,1))
    # ent1.insert(3,'z')
    # ent1.select_to(3)
    # ent1.select_range(3,6)
    # print(ent1.select_present())
    ent1.icursor(5)

Button(window, text='Tıkla', command=clicked_button).pack(pady=10)


window.mainloop()