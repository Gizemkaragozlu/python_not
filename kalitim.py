class Insan():
    def __init__(self,gelenAd, gelenSoyad):
        self.ad = gelenAd
        self.soyad = gelenSoyad

    def bilgileri_yazdir(self):
        return """
---------Kişi Bilgileri-------
Ad: {}
Soyad: {}""".format(self.ad, self.soyad)

insan1 = Insan('Gizem','Karagözlü')
print(insan1.bilgileri_yazdir())
