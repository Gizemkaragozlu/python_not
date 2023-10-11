from tkinter import *
# bg               'arka plan rengi'
# height           'yükseklik'
# width            'genişlik'
# dash             'kesikli çizgi'
# fill             'olşturulan örneğin ovalin içini boyar'
# outline          'çerçeve rengi'
# cursor
# highlightthickness
# gighlightbackground
#
# line              'çizgi'
# oval
# arc
# polygon
# image
window = Tk()
window.geometry('500x500')

cv = Canvas(window,bg='green',height=400,width=300)

# cv.create_line(0, 0, 100, 100,dash=(13,13))
# cv.create_line(100, 200, 100, 100)
# cv.create_line(100, 100, 200, 100)
# cv.create_line(200, 200, 100, 200)
# cv.create_line(100, 300, 100, 100)

# cv.create_oval(10, 10, 150, 150,fill='pink',outline='white',width=2)

# cv.create_arc(10, 10, 150, 150, start=0, extent=120,fill='red')# start= açının başlagıcı, extent= açının bitişi

# cv.create_polygon(0, 75, 75, 0, 150, 75, 75, 150, fill='blue',outline='black',width=3)

photo = PhotoImage(file='user.png')
photoRezised = photo.subsample(6,6)
cv.create_image(150,150, image= photoRezised)

cv.pack()
window.mainloop()