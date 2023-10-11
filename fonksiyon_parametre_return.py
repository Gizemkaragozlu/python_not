# def func(): #Fonksiyon çağırılırken def yazılmalı ve yanına bir key yazılmalı.
#     print('Hello fonksiyon') # console de böyle run edilemez
# func()# Run etmek içi fonksiyonun dışında onu çağrımalısınız.
# func()# Fonksiyonu defalarca çağırıp kullanabilirsiniz.

# Parametre ile Fonksiyon kullanımı

# def funpar(strYazilim):
#     print(strYazilim)
# funpar('Hello Py')

# def yazdir(strYazilim):
#     print('Hello {}'.format(strYazilim))#Hello Python olarak yazdırdık
#     print('Hello ' + strYazilim)#Hello Python olarak yazdırdık
# yazdir('Python')

# def topla(num1, num2):
#     print(num1 + num2)
# topla(4,8)
# topla(26,74)

# def kisi(strNAme, strAge, strJob):
#     print('Kişi Adı:{}, Kişi Yaşı:{}, Kişi Meslek: {}'.format(strNAme,strAge,strJob))
# kisi('Gizem',22,'Mühendis')

# def num_pow(num1,num2 = 2): #Sabit bir parametre girilebilir
#     print(num1**num2)
# num_pow(2)

# Return fonksiyondan bir parametre alıp kullanabildiğimiz bir keyword.

# def numreturn(num1, num2 = 2):
#      return num1**num2 # Print yazmadan aşağıda fonk çağırmamak için return ifadesi kullanılır
# print(numreturn(2)) #Fonksiyonu burada çağırmadan print ile yazdır.

# def get_greater_num(num1, num2):
#     ''' 3 tırnak ile Docstring
#     İki sayıdan büyük olanı geri dönen fonksiyon
#     :param num1: İlk girilen sayı
#     :param num2: ikinci girilen sayı
#     :return: Hangisi büyükse onu döner
#     '''
#     if num1 > num2:
#         return num1
#     elif num2 > num1:
#         return num2
#     else:
#         return num1
# print(get_greater_num(3,7))
