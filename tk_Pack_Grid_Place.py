from tkinter import *
window = Tk()

window.geometry('500x400')
lbl = Label(window, text='label1')
lbl.place(x=50, y=40)#50 birim sağa kaydır,40 birim aşağıya kaydır
# lbl.grid(columns=1, row=0)# kolon ve satır
# lbl.pack()# yön belirtme
""".pack(side=LEFT)
.pack(side=TOP)
.pack(side=RIGHT)
.pack(side=BOTTOM)"""


window.mainloop()