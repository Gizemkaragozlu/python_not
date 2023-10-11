# class Ogrenci():
#     def __init__(self , gelenAd , gelenVize1 , gelenVize2 , gelenFinal):
#         # __init__ bu metot ile nesnelere atanır
#         # self Ogrencinin içinde tutulan değişkeni değiştirir.
#         self.ad = gelenAd       #Değişkenlerin sabit aynı kalmaması için değiştirilebilir olması için self yazıyoruz.
#         self.vize1 = gelenVize1
#         self.vize2 = gelenVize2
#         self.final = gelenFinal
#
#     # not_hesaplama = (vize1 * 30 / 100) + (vize2 * 30 / 100) + (final * 40 / 100)
#     def not_hesaplama(self):
#         return (self.vize1 * 30 / 100) + (self.vize2 * 30 / 100) + (self.final * 40 / 100)
#
#      def bilgileri_yazdir(self):
#          print('{} İsimli öğrencinin,1.Vizesi:{},2.Vizesi:{},Final:{}'
#                .format(self.ad,self.vize1,self.vize2,self.final,Ogrenci.not_hesaplama(self)))
#
# ogr1 = Ogrenci('Ayşe',30,64,72)
# ogr2 = Ogrenci('Mehmet',83,39,92)
#
# ogr1.bilgileri_yazdir()
#
