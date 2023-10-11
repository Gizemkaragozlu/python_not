from tkinter import *
# Label için sık kullanılan methodlar
# text = yazı
# font = yazı fontu ve büyüklüğü
# bg = yazı arka plan rengi
# fg = yazı rengi
# cursor = yazının üstüne gelince mouse işaretim ne olsun
# height = yükseklik
# width = genişlik
# wraplength = yazı sığmazsa aşağıya at wraplength= 100
# padx = labelin çerçeve boşluğu
# pady = labelin çerçeve boşluğu
# anchor = kutupları göre yönünü belirtebiliriz
# relief = yazı çerçevesi derinlik veya yükseklik katar
# bitmap = standard bitmapler
# image
# compound
window = Tk()
window.geometry('500x500')
# label1 = Label(window, text='Label Text',font=('Arial',25),bg='pink',fg='white',cursor='plus',height=5,width=10).pack()
# label2 = Label(window, text='Label Text',font=('Helvetica 12 bold italic underline'),width=15,height=8,bg='green',anchor='n').pack()
# label3 = Label(window, text='Label Text',font=('Helvetica 12 bold '),relief=RIDGE).pack()


# label3 = Label(window,font=('Helvetica 12 bold '),bitmap='info').pack()
# bitmap kullanılacak methodlar
# "error"
# "gray50"
# "gray25"
# "gray12"
# "hourglass"
# "info"
# "question"
# "question"
# "warning"
photo = PhotoImage(file="hearts.png")
photoResized = photo.subsample(4, 4)#resmin boyutunu ayarlıyoruz
label3 = Label(window,text='Love',font=('Helvetica 12 bold '),image=photoResized,compound=TOP).pack()
window.mainloop()