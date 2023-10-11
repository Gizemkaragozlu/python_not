from tkinter import *
window = Tk()
window.geometry('500x500')
# Radiobutton parametreler
# variable
# value
# font
# bg
# fg
# activebackground
# activeforeground
# height
# width
# padx
# pady
# wraplenght
# cursor
# anchor
# state
# relief
# image
# command

#Methodlar
# select = radiobutton seçimini yakalar
# deselect = radiobutton seçimini kaldırır
photo = PhotoImage(file='user.png')
photoRezised = photo.subsample(1,1)

iVar = IntVar()
def sel():
    selection = 'Selected radio val =' + str(iVar.get())
    print(selection)
rd1 = (Radiobutton(window, text='Seçim 1',
            variable=iVar,
            value=1,
            font=('Times 15 bold'),
            bg='green',
            fg='white',
            activebackground='red',
            activeforeground='black',
            # height=3,
            # width=10,
            wraplength=30,
            cursor='man',
            anchor='nw',
            image=photoRezised,
            command=sel,))
rd1.pack()

Radiobutton(window, text='Seçim 2',
            variable=iVar,
            value=2,
            font=('Times 15 bold'),
            bg='green',
            fg='white',
            activebackground='red',
            activeforeground='black',
            padx=1,
            pady=5,
            command=sel,
            ).pack()
# text,variable ve value yazmamız gerek value gruplama matığından çıksın tek tek seçmek için yazılır.
Radiobutton(window, text='Seçim 3',
            variable=iVar,
            value=3,
            state=DISABLED,
            relief=RAISED,
            command=sel,
            ).pack()

rd1.select()

window.mainloop()