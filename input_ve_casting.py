# input() # Consolda veri girmemiz istenir

# val = input()
# print(val) # Girilen değer yazdırılır.

# inpVal = input('Lütfen adınızı giriniz:') #Consolda bu yazı çıkar ve bir değer istenir
# print('Girilen ad:',inpVal) #Girilen değer ekrana basılır.

# inpAd = input('Adınızı Giriniz:')
# inpSoyad = input('Soyadınızı giriniz:')
# inpYas = input('Yaşınızı giriniz:')
# print('Ad:{}'.format(inpAd))
# print('Soyad:',inpSoyad)
# print('Yas:',inpYas)
# ***** Console********
# Adınızı Giriniz:Gizem
# Soyadınızı giriniz:Karagözlü
# Yaşınızı giriniz:22
# Ad:Gizem
# Soyad: Karagözlü
# Yas: 22

# inpVal = input('Lütfen bir değer giriniz:')
# print(type(inpVal)) # <class 'str'> input değişkeni ile alınan bütün değerler stringtir.

#------------- Veri Dönüştürme-------------------

# val1 = '22'
# val2 = int(val1)
# print(type(val1)) # '' işareti ile yazdığım için str döner
# print(type(val2)) # int yazıp değeri alınca str olan değişkeni int olarak dönüştürürüz.

# val1 = 22
# val2 = str(val1) veya float da yazabiliriz hangi tipe dönüştürmek istenirse o yazılır
# print(type(val1))
# print(type(val2))

# inpVal1 = input('Birinci sayıyı giriniz:')
# inpVal2 = input('İkinci sayıyı giriniz:')
# print('İki sayıyının toplamı = ',inpVal1+inpVal2) # 5 ve 8 girdim 58 olarak yazar çünkü str değer olarak alır.

# inpVal1 = int(input('Birinci sayıyı giriniz:')) # int olarak al dediğimiz için girilen değeri direkt olarak toplar
# inpVal2 = int(input('İkinci sayıyı giriniz:'))
# print('İki sayıyının toplamı = ',inpVal1+inpVal2)

#Bir tanesini tek dönüştürürsek int ve str olarak bu ifadeyi hesaplamaz ve hata verir.

# inpVal = input('Lütfen bir sayı giriniz:')
# print('Girilen sayının 2 katı =', 2*float(inpVal)) #Float olarak yazmazsak 2 ile çarpmaz 2 yi yanına yazar * ifadesi yanına anlamına gelir.
