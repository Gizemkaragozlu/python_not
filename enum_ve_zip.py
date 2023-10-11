# ------enumerate-----------
# meyveList = ['elma', 'armut', 'Karpuz']
# for meyve in enumerate(meyveList):
#     print(meyve)

# indexi başa ekleyip tuple değişken olarak döner.
# (0, 'elma')
# (1, 'armut')
# (2, 'Karpuz')

# ------zip-----------
# iki değişkeni birleştirip tek bir loop da dönememizi sağlayan yapı.

# meyveList = ['elma', 'armut', 'karpuz']
# sayiList = [1, 2, 3]
# for val in zip (sayiList, meyveList):  # iki list'i birleştirdik
#     print(val)

# kisiList = ('Gizem', 'Furkan', 'Ayşe', 'Mehmet')
# puanList = ('95', '85', '55', '68')
# harfList = ('AA', 'AB', 'CC', 'BB')
#
# for kisi, puan, harf in zip(kisiList, puanList, harfList):
#     print('{} kişisi {} puan aldı. {} harf notu'.format(kisi, puan, harf))

# -------------Console------------------
# Gizem kişisi 95 puan aldı. AA harf notu
# Furkan kişisi 85 puan aldı. AB harf notu
# Ayşe kişisi 55 puan aldı. CC harf notu
# Mehmet kişisi 68 puan aldı. BB harf notu
