# DÖNGÜLER
# For While
# range(-start - end -step)
##for i in range(50,0,-1):
##    if i%2 == 0:
##        print(i," sayısı çifttir")
##    else:
##        print(i," sayısı Tektir")
##
##
###150-250 arasindaki bütün çift sayıların toplamı nedir
##toplam = 0
##for i in range(150,251):
##    if i%2 == 0:
##        toplam += i
##
##print(toplam)
"""
import math
#Faktöriyel kullanıcının giridiği sayının faktöriyelini alan programı yazınız

sayi = int(input("Faktöriyeli alınacak sayıyı giriniz:"))

print(math.factorial(sayi))

sonuc = 1
for i in range(sayi,0,-1):
##    print(i)
    sonuc *= i
print(sonuc)

"""
# Fibonacci 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 

terim_sayisi = 1000

a = 0
b = 1

c = 0

for i in range(terim_sayisi):
    c = a+b
    a = b
    b = c
    print(c)


input()






