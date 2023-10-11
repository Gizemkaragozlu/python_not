# boVal = True # <class 'bool'> tipinde
# print(type(boVal))

# boVal = bool(1) # True olarak(0 False) bool değerinde döner.
# print(boVal)
# print(type(boVal))

# == Eşittir    x == y
# != Eşit Değil x != y
# >  Büyük      x  > y
# <  Küçük      x  < y
# >= Büyük Eşit x >= y
# <= Küçük Eşit x >= y

# print(4 == 4) # True
# print(4 == 5) # False
# print(4 != 5) # True

# print('Gizem' == 'Gizem') # True
# print('Gizem' != 'Gizem') # False

#------integer ifadelerde boolen--------
# print(5 > 3) # True
# print(5 > 7) # False
# print(5 >= 5) #True

#------String ifadelerde boolen--------
# print('a' < 'a') # False
# print('a' < 'b') # True
# String ifadelerde ilk harfin alfabetik sırasına bakkar

#------- Mantıksal Operatörler---------------
# and  Her iki ifade de doğruysa true
# or   İfadelerden birisi doğruysa true
# not  Sonucu ters çevirir.Yani true ise false,false ise true yapar

# print(3 < 4 and 4 < 5) # True
# print(3 < 4 and 4 > 5) # and de her ikisi de true veya her ikiside false olmak zorunda

# print(3 < 4 or 4 < 5) # True
# print(3 < 4 or 4 > 5) # True olarak döner çünkü or da her ikisinden bir ture olsa yeterlidir.

# print(not (3 < 4)) # False
# print(not (3< 4 or 4 < 5) ) # False olarak döner not ifadesi tam tersi bir durumu ifade eder ture ise false,false ise true

# and ve or aynı anda yazılmak istenirse...

# print(3 < 2 and 4 < 5 or 2 == 1) # False
# print((3 < 2 and 4 < 5) or 1 == 1 )# Öncelik için paranteze alınmalı sonuç True