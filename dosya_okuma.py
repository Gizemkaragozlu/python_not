# dosya = open('ders_notlari_txt' , 'r' , encoding='utf-8')
# dosya okumak için yazılır 'r' okumasını sağlar encoding türkçe karakter için yazdık

# dosya.read()
#Oku
# print(dosya.read())
# dosyayı oku ve yazdır.
# print(dosya.read(2))
# # 5 karaketerini al
# print(dosya.tell())
# # imlecin hangi indexte olduğunu göster
# dosya.seek(14)
# imleci istediğimiz yerden başlatabiliriz.
# print(dosya.readline())
# imlecin olduğu tüm satırı al
# print(dosya.readlines()[2])# array olarak döner indexi direkt alabiliriz
# tüm satır verilerini oku

# Örnek
# print(dosya.tell())
# dosya.seek(14)
# print(dosya.read(2))
# print(dosya.tell())

dosya.close()

#okuduktan sonra dosyayı kapat
