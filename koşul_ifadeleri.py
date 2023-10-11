# intVal = 10
# print('Değişkenim ilk değeri =',intVal)

# if True:
#     False olursa da 2 eklendi ifadesine girmez direkt if bloğundan çıkar
#      if buloğunun içindeki değerin hangisinin olacağını gösterirken
#     intVal = intVal + 1 # önüne bir tab boşluk bırakmalıyız ki İfin içine girebilsin
#     print('Değişkene 1 eklendi')
# print('Değişkenin son hali =', intVal)
# ---------Not------------
# Aşağıda bulunan yapıda ifi kontrol eder .
# Sonra diğer ifi de kontrol eder ne kadar if yazılırsa teker teker kontrol eder programı yormamak için elif ifadesi önerilir.
# -----------Örnek---------

intVal1 = 10
intVal2 = 30
# if intVal1 > intVal2:
#     print('intVal1 değişkenim daha büyüktür')
# if intVal2 > intVal1:
#     print('intVal2 değişkenim daha büyüktür')

#---------Elif------------
# if intVal1 > intVal2:
#      print('intVal1 değişkenim daha büyüktür')#True ise elif'e bakma
# elif intVal2 > intVal1:
#      print('intVal2 değişkenim daha büyüktür')#False ise Elif'e bakar
# else:
#     print('İki sayı birbirine eşittir')#if ve elif doğru değilse Else bakar.


# ------Nested if------
strUser = 'Gizem'
strPass = '1234'
# if strUser == 'Gizem':
#     print('Kullanıcı adı doğru')
#     if strPass == '1234':
#         print('Şifre doğru')
#         print('Login işlemi başarılı')
#     else:
#         print('Şifre hatalı')
#         print('Login işlemi başarısız')
# else:
#     print('Kullanıcı adı yanlış')

# Mantıksal ifadeyi koşul ile birleştirelim
# if strUser == 'Gizem' and strPass == '1234':
#     print('Login işlemi başarılı')
# else:
#     print('Login işlemi başarısız kullanıcı adı veya şifre hatalı')
# 

