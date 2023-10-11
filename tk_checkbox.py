from tkinter import *
# checkbox için kullanılan parametreler
# text                 'yazı'
# font                 'yazı fontu ve büyüklüğü'
# bg                   'yazı arka plan rengi'
# fg                   'yazı rengi'
# activebackground     'butona basıldığında arka plan'
# activeforeground     'butona basıldığında yazı rengi'
# height               'yükseklik'
# width                'genişlik'
# padx                 'çerçeve boşluğu'
# pady                 'çerçeve boşluğu'
# wraplenght           'yazı sığmazsa aşağıya at'
# cursor               'üstüne geldiğinde mouse ikonu değişir'
# anchor               'ne tarafta gözüksün ing yönler ile belirtilir n,e,s,w'
# state                'kullanılabliriği kapatıp açabiliriz disabled,normal'
# relief               'yazı çerçevesi derinlik veya yükseklik katar'
# image                'resim ikon'
# variable             'command parametresi ile kullanılır'
# command              'yukarı veya aşağı oklara basınca ne olacağını belirttiğimiz yer'
# offvalue             'tıklandığında oluşan değeri değiştirmek için(active)'
# onvalue              'tıklandığında oluşan değeri değiştirmek için(passive)'
# checkbox için kullanılan methodlar
# select               'ekran açılır açılmaz tikli halde gelsin'
# deselect             'ekran açılır açılmaz tiksiz halde gelsin'
# toggle               'yukarıdaki methodların tam tersini alır tikli ise tiksiz ,tiksiz ise tikli yapar'

window = Tk()
window.geometry('500x500')

photo = PhotoImage(file='user.png')
photoRezied= photo.subsample(2,2)
ivar = IntVar()
def sel():
    selection = 'Tıklanan val =' +str(ivar.get())
    print(selection)
chk1 = Checkbutton(window,text='checkbox widget',
            font=('Arial 12 bold'),
            bg='blue',
            fg='white',
            activebackground='red',
            activeforeground='black',
            # height=1,
            # width=25,
            # padx=15,
            # pady=15,
            # wraplength=50,
            cursor='spider',
            anchor='se',
            state=NORMAL,
            relief=GROOVE,
            image=photoRezied,
            variable=ivar,
            command=sel,
            onvalue=2,
            offvalue=1)
chk1.pack()
# chk1.select()
chk1.toggle()

window.mainloop()