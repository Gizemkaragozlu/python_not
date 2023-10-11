# dosya = open('yeni_not.txt', 'w', encoding='utf-8')
#
# # dosya.write('Furkan Coşgun \n')
# # dosya.write('Gizme Karagözlü')
#
# dosya.writelines(['10-matematik\n','34-fizik\n','44-tarih\n'])
# #Çoklu bir şekilde yazmamızı sağlar
#
# dosya = open('yeni_not.txt', 'a', encoding='utf-8')
# #a' aynı veriyi defalarca yazmamızı bellekte tutmamamızı sağlar.
# dosya.write('44-tarih')
#
# with open('yeni_not.txt', 'a', encoding='utf-8') as dosya:
# #close gibi çalışır with içindeki verileri yazdıktan sonra dosyayı kapa
#     dosya.write('10-matematik\n')
#     dosya.write('34-fizik\n')
#     dosya.write('44-tarih')
#
# dosya.close()