# Set sırasız(içeride nasıl tutulduğunu bilemeyiz),değiştirilebilir(veri çıkarılamaz ama eklenebilir),indexsiz
# Set değişkeni {} ile gösterilir
# meyveSet = {'elma','armut','kivi','muz'}
# print(meyveSet)

# print(meyveSet[2]) = Hata döner çünkü indexsizdir.

# Kullanılır methodlar
# add
# meyveSet.add('karpuz') = ekler
# print(meyveSet)
# update
# meyveSet.update(['karpuz','mandalina']) = Veri ekler
# print(meyveSet)
# len
# print(len(meyveSet)) = Kaç eleman olduğunu gösterir
# remove
# meyveSet.remove('kivi') = kiviyi göstermez, olmayan bir değişken yazılırsa hata verir
# print(meyveSet)
# discard
# meyveSet.discard('kivi') = Kiviyi göstermedi
# print(meyveSet)

# meyveSet.discard('üzüm') = Hata vermez varolan listeyi getirir
# print(meyveSet)
# pop
# silinenMeyve = meyveSet.pop() = Rastgele veriyi siler sildikten sonra silinen veriyi gösterir.
# print(silinenMeyve)
# clear
# print(meyveSet)
# meyveSet.clear() = set() yani boş olduğunu ve veriyi temizledğini gösterir
# print(meyveSet)
# del
# del meyveSet
# print(meyveSet) = Sildiği için hata verir