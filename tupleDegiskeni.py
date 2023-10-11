# Tuple sıralanabilen,değiştirilemez(veri eklenip çıkarılamaz),indexli,yenilenebilir.
# Tuple değişkeni () işareti ile gösterilir.
# meyveTuple= ('elma','armut','kiraz','muz','armut')

# print(meyveTuple)
# print(type(meyveTuple)) <tuple>tipinde olduğunu söyler
# print(meyveTuple[2]) = Kiraz olduğunu gösterir 2.index

# meyveTuple[1] = 'kivi' = Hata verir çünkü tuple değişkeni değişime izin vermez.

# print(help(tuple)) = Hangi methodları kullanabileceğimizi görmemizi sağlar
# -----Kullanılabilir Methodlar----
# len
# print(len(meyveTuple)) = Kaç elemalı olduğunu gösterir.
# count
# print(meyveTuple.count('armut')) = Kaçıncı indexte olduğunu gösterir ilk gördüğünü alır.
# index
# print(meyveTuple.index('armut')) = İndexini gösterir.
# del
# del meyveTuple[2] = Silinemez çünkü tuple değişime izin vermez.
# del meyveTuple = Bütün değişkenleri sildirebiliriz.
