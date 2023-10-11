from  tkinter import *
#-----Frame kullanılacak parametreler-------------
# height
# width
# bg
# highlightbackground = çerçeve rengi
# highlightthickness = çerçeve kalınlığı
# cursor = mouse üzerine gelince mose şekli ne olsun
# padx
# pady

window = Tk()
window.geometry('500x500')
frame1 = Frame(window,height=100,width=150,bg='red',
               highlightbackground='black',highlightthickness=5,cursor='heart')#Frame oluşturuldu
frame1.pack()
window.mainloop()