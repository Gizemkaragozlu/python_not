# num1 = 10 #Global
# # Global değişkene her yerde erişebiliriz.
#
# def func(num2):
#     num2 = 20 # Local
#     print(num1) # Erişebiliyoruz
#     print(num2)
#
# print(num1)
# print(num2) # Local olduğu için erişemeyiz

# num = 10
# print('Num =', num) # Num = 10
# def func():
#     global num # fonksiyondaki değer olduğu gibi kalması için global yazıyoruz.
#     num = 20
#     print('Num =', num) # Num = 20
#
# func()
# print('Num =', num) # Num = 20

# CONSOLE
# Num = 10
# Num = 20
# Num = 20
