# import math

# print(math.pi)
'''pi sayısı otomatik gözükür import ettiğimiz math kütüphanesinde hazır bulunmakta'''
import q

# print(math.factorial(5))
'''factoriel değerini alırız'''

# from datetime import datetime
#
# print(datetime.now())
'''2023-09-21 14:38:42.235364'''

# import random
# print(random.randint(1,100))
'''1 ile 100 arasında random bir sayı üretir'''

# import numpy as np
'''Terminal = pip install numpy'''

# dizi = np.arange(15).reshape(3, 5)
# print(dizi)
# print(dizi.shape)
'''üç boyutlu dizi 
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
(3, 5)'''

# import cv2 #Görüntü işleme
#
# cap = cv2.VideoCapture(0) #Bilgisayarımın kamerasına eriş
# while True:#Sonsuz döngüye gir
#     ret, frame = cap.read()#Capture dan iki methodu kullan
#     if frame is not None:#Görüntü elde edebildiysem
#         cv2.imshow('Camera', frame)#Frame burada bas ekrana
#
#     q = cv2.waitKey(1)#Görüntüden çıkmak için
#     if q == ord('q'):# q' ya basınca çıkılsın
#         break
# cap.release()#Döngüden çıktıktan sonra kameramı serbest bırak
# cv2.destroyAllWindows()#Tüm pencereleri kapat

# import cv2
#
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)# Üstteki kod bende uyarı verdi bunu da kullanabiliriz
# while True:
#     ret, frame = cap.read()
#     if frame is not None:
#         cv2.imshow('Camera',frame)
#     x = cv2.waitKey(1)
#     if x == ord('x'):
#         break
# cap.release()
# cv2.destroyAllWindows()