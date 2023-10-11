# *********************String Output Format****************************
# print('hello')
# String ifade
# print('{}'.format('hello'))
# İnt ifade
# print('{}'.format(3))

# print('hello Python World')

# print('hello {} {}'.format('Python',' World'))

# print('{:.15}'.format('Hello Pyhon World')) #İlk 15 karakteri istedik

# print('{:^40}'.format('Hello')) # 40 karakterlik bir string bas ve ^ Ortada göster dedik
# print('{:*^40}'.format('Hello')) # Console: *****************Hello******************
# print('{:>40}'.format('Hello')) # Sağa dayalı
# print('{:<40}'.format('Hello')) # Sola dayalı

# *********************Integer Output Format****************************
# print('{:d}'.format(3)) # d ifadesi integer ifadeyi temsil eder.
# print('{:d}'.format(-3))
# print('{:+d}'.format(3)) # Önüne artı ifadesini ekler

# iVal = 123456
# print('{:020d}'.format(iVal)) # Console: 00000000000000123456 " 20 karakterlik 0 ekle dedik.

# print('{:,d}'.format(iVal)) # Console: 123,456 " Üç basamakta bir , koy

# fVal = 1234.5678
# print('{:f}'.format(fVal))
# print('{:,f}'.format(fVal)) # Console: 1,234.567800
# print('{:20f}'.format(fVal)) # 20 karakter boşuk at önüne

