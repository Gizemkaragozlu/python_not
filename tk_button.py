from tkinter import *
#--PARAMETRELER----
# text
# font
# bg
# fg
# activebackground = butona basıldığında arka plan
# activeforeground = butona basıldığında yazı rengi
# cursor = butonun üstüne gelince mouse ifadem ne olacağı
# height
# width
# wraplength = karakterler sığmazsa alt alta yazar
# bd = border kalınlığı
# command = tıklandığında ne olsun
# padx
# pady
# relief = Buton derinlik, çerçeve (FLAT,RAISED,SUNKEN,GROOVE,RIDGE)
# state  = buton kullanılır olup olmadığını belirtiriz disabled,normal
# compound = yazı nerede olsun LEFT,BOTTOM vb..

window = Tk()
window.geometry('500x500')
# def clicked_button():
#     print('Click mee!')
# Button(window, text='Clic',font=('Times 15 bold'),bg='lightgreen',fg='white'
#        ,activebackground='pink',activeforeground='orange',cursor='plus',
#        height=3,width=5,bd=5,command=clicked_button).pack()


# reliefList =[
#     FLAT,
#     RAISED,
#     SUNKEN,
#     GROOVE,
#     RIDGE
# ]
# for reliefItem in reliefList:
#     Button(window, text='Tıkla',relief=reliefItem).pack(pady=10)

photo = PhotoImage(file='hearts.png')
resizedPhoto = photo.subsample(5,5)
Button(window,text='Click',image=resizedPhoto,compound=BOTTOM).pack()
window.mainloop()