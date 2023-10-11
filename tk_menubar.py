from tkinter import *
# tearoff = alt menüde oluşan çizgili yeri yok eder
# font = yazı tipi
# bg = arka plan rengi
# fg = yazı rengi
# activebackground = tıklandığında arka planı
# activeforeground = tıklandığında yazı rengi

# add_command(options) = tıklandığında
# add_cascade(options)
# add_separator() = gruplama mantığında bir çizgi çeker
# add_checkbutton( options ) = checkbox mantığında çalışır
# add_radiobutton( options ) = radiobutton matığında çalışır
window = Tk()
window.geometry('500x500')
def donothing():
    print('donothing')
menubar = Menu(window)
filemenu = Menu(menubar,tearoff=0, font='Arial 15 bold', bg='yellow', fg='orange',
                activeforeground='white',activebackground='red')
filemenu.add_command(label='New', command=donothing)
filemenu.add_checkbutton(label='Open',command=donothing)
filemenu.add_radiobutton(label='Save1',command=donothing)
filemenu.add_radiobutton(label='Save2',command=donothing)
filemenu.add_separator()
filemenu.add_command(label='Close',command=donothing)
menubar.add_cascade(label='File',menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Cut',command=donothing)
editmenu.add_command(label='Copy',command=donothing)
editmenu.add_command(label='Paste',command=donothing)
editmenu.add_command(label='Delete',command=donothing)
menubar.add_cascade(label='Edit',menu=editmenu)
window.config(menu=menubar)
window.mainloop()