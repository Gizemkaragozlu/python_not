# Dictionary sırasız,değiştirilebilir,indexli(key mantığı bulunmakta),yenilenemez
# Dictionary {} ile gösterilir key ve value mantığı ile tanımlanır.

personelDic = {'isim' : 'Gizem',
               'yaş':'22',
               'meslek':'Abap'}
# print(personelDic)
# isimVal = personelDic['isim'] = ismin valuesını verir
# print(isimVal)

# personelDic['meslek'] = 'İşletmeci' = meslek İşletmeci olarak değiştirilir
# print(personelDic)

# Kullanılır Method
# # get
# isimVal = personelDic.get('isim') = isim keyinin valuesını verir
# print(isimVal)
# len
# print(len(personelDic)) = Kaç veriolduğunu gösterir
# pop
# silinenVal = personelDic.pop('yaş') = yaş keyini ve valuesini silip ekranda gösterir
# print(silinenVal)
# popitem
# soneklenenVal = personelDic.popitem() = Son ekleneni slip gösterir
# print(personelDic)
# print(soneklenenVal)
#
# print(personelDic)
# del personelDic = Silindi hata verdi
# print(personelDic)
# clear
# personelDic.clear() = Bütün veriyi temizledi
# print(personelDic)
# dict
# personelDic2 = dict(
#     isim= 'Gizem',
#     yaş= '22',
#     meslek= 'Abap'
# )
# print(personelDic2) = Listeyi olduğu gibi gösterir
