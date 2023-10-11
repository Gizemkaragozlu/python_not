from tkinter import *
#----Spinbox parametreler---
# from_              'başlanılacak index no'
# to                 'bitiş index no'
# increment          'kaçar kaçar artsın'
# font               'yazı tipi ve kaınlığı'
# bg                 'arka plan rengi'
# fg                 'yazı sayı rengi'
# cursor             'mouse şekli'
# bd                 'çerçeve derinlik'
# width              'genişlik'
# justify            'yazı,sayı hangi yönde olacağını belirtiriz'
# relief             'çerçeve derinlik, dışa dönük vb...'
# state              'disabled, normal'
# textvariable       'ekran açılır açılmaz ne gözükmesi isteniyorsa o sabit kalır'
# command            'yukarı veya aşağı oklara basınca ne olacağını belirttiğimiz yer'
# disabledbackground 'disabled olduğunda arka plan ne olsun'
# disabledforeground 'disabled olduğunda yazı,sayı rengi ne olsun'
# format             'sayısal ifadenin formatını değiştirmemizi sağlar'
# get()              'get bir methoddur, ekrana verileri yazdırmamızı sağlar'

window = Tk()
window.geometry('500x500')
def command_value():
    print(sp1.get())

sVal = StringVar(value=22)
sp1 = Spinbox(window,from_=18,to=30,
        increment=3,
        font='Arial 12 bold',
        bg='red',
        fg='white',
        cursor='plus',
        bd=7,
        width=32,
        justify=RIGHT,
        relief=RAISED,
        state='normal',
        textvariable=sVal,
        command = command_value,
        format='%02.03f'   # decimal olarak gösterdik virgülden sonra 3 sıfır koy
        )
sp1.pack()

# Spinbox(window,from_=18,to=30,
#         increment=3,
#         font='Arial 12 bold',
#         bd=7,
#         width=32,
#         justify=RIGHT,
#         relief=RAISED,
#         state='disabled',
#         disabledbackground='pink',
#         disabledforeground='red'
#         ).pack()

window.mainloop()