ogrAd = 'Ayşe'
ogr1Vize1 = 30
ogr1Vize2 = 70
ogr1Final = 95
ogr1_not_hesaplama = (ogr1Vize1 * 30/100) + (ogr1Vize2 * 30/100) + (ogr1Final * 40/ 100)
print('{} İsimli öğrencinin '
      '1.Vizesi: {},'
      '2.Vizesi: {},'
      'Final notu: {},'
      'Not Ortalaması: {}'
      .format(ogrAd,ogr1Vize1,ogr1Vize2,ogr1Final,ogr1_not_hesaplama))

ogrAd = 'Mehmet'
ogr1Vize1 = 60
ogr1Vize2 = 85
ogr1Final = 100
ogr1_not_hesaplama = (ogr1Vize1 * 30/100) + (ogr1Vize2 * 30/100) + (ogr1Final * 40/ 100)
print('{} İsimli öğrencinin '
      '1.Vizesi: {},'
      '2.Vizesi: {},'
      'Final notu: {},'
      'Not Ortalaması: {}'
      .format(ogrAd,ogr1Vize1,ogr1Vize2,ogr1Final,ogr1_not_hesaplama))

'''Görüldüğü üzere birden çok öğrenci girmek istersek üste görüldüğü gibi kod kalabalığı oluşuyor
daha fazla sayıda öğrenci girilirse kon karmaşasına neden olacaktır. Bu yüzden Class ve OOP yapısı tercih edilir.'''
