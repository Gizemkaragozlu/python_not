from tkinter import *
from tkinter import messagebox

# Information messages
# showinfo()    'Başlık ve message yazılır (uyarı)'

# Warning messages
# showerror()   'Başlık ve message yazılır(error)'
# showwarning() 'Başlık ve message yazılır(warning)'

# Question messages
# askquestion()   'Başlık ve message yazılır(yes no)'
# askokcancel()   'Başlık ve message yazılır(tamam iptal)'
# askretrycancel() Başlık ve message yazılır(yeniden dene iptal message)'
# askyesno()       Başlık ve message yazılır(yes no)'
# askyesnocancel() Başlık ve message yazılır(evet hayır iptal)'

window = Tk()
window.geometry('500x500')

def clicked_button():
    # messagebox.showinfo('Show Info','Information')
    # messagebox.showwarning('Show Warning','Warning')
    # messagebox.showerror('Show Error','Error')
    # messagebox.askquestion('askquestion','yes no message')
    # messagebox.askokcancel('askokcancel','tamam iptal message')
    # messagebox.askretrycancel('askretrycancel','yeniden dene iptal message')
    # messagebox.askyesno('askyesno','yes no message')
    messagebox.askyesnocancel('askyesnocancel','evet hayır iptal message')
Button(window,text='click me!',command=clicked_button).pack()

window.mainloop()