# def func(num):
#     return num * 2
# print(func(2))

# Lambda kullanarak aynı işlemi yapıyoruz.

# func = lambda num : num * 2 # Lambda yanında varsa paramtere yazılır
# print(func(2))
# func = lambda num1,num2 : num1 * num2 # Birden fazla parametre girilebilir.
# print(func(num1=3,num2=6))

# Rastgele gelen sayıları toplamını bulan lambda
# total = lambda *numbers : sum(numbers) #Toplamını almamızı sağlar.
# print(total(1,2,3,4,5,6,7,8))
# print(total(23,35,12,67,24))

# def ve lambda mix
#
# def func (num1):
#     return lambda num2: num2 *num1
# funcDoubler = func(2) # lambda num2: num2 * 2
# funcTribler = func(3) # lambda num2: num2 * 3
#
# print(funcDoubler(10))
# print(funcTribler(10))

# mailFunc = lambda num, subFunc: num + subFunc(num)
# print(mailFunc(2,lambda x: x * 2))

