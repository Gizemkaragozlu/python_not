'Örnek 1'
# print(1)
# print(2)
# print(x) '''Bu şekilde yazarsak x hata verir ve sonraki koda girmez'''
# print(3)
# print(4)
'Örnek 2'
# print(1)
# print(2)
# try:
#     print(x)
# except:
#     print('x değişkeni tanımlanmamış')#Hatalı olan için mesaj ver ve devam et
# print(3)
# print(4)

#Console
# 1
# 2
# x değişkeni tanımlanmamış
# 3
# 4
'Örnek 3'
# num1 = 10
# try:
#    num2 = int(input('Bölen sayıyı giriniz:'))
#    result = num1 / num2
#    print(result)
# except ZeroDivisionError: # Eror mesaj tipi de girilebilir
#      print('0 değeri girilemez') # try except içine almasaydık 0 değeri girilince hata verir ve devam edemezdik.
# except ValueError:
#     print('string ifade girilemez.')
# except:
#     print('Tanımlanamayan hata')
# else:
#     print('Hiç bir hata yok')
'Raise Except = Hata mesajı verip koda devam etmesin diyorsan bu kalıbı kullanıyoruz.'
# num1 = 0
# if num1 == 0:
#     raise Exception('Değer 0 olamaz!!!')
'Örnek 2'
# num1 = 'ASD'
# if not type(num1) is int:
#     raise Exception('Lütfen sayısal bir ifade giriniz!!!')
