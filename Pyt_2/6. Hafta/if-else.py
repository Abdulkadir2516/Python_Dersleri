"""
İf - Else - Elif uygulamalar
"""
#kenar boyutlarının girildiği üçgenin bir üçgen oluşturulabilirmi tespit eden kodu yazınız
##import math
##
##x = int(input("1. Kenarı Giriniz: "))
##y = int(input("2. Kenarı Giriniz: "))
##z = int(input("3. Kenarı Giriniz: "))
##
##kosul0 = math.fabs(y-z) <= x <= y+z
##kosul1 = math.fabs(x-z) <= y <= x+z
##kosul2 = math.fabs(x-y) <= z <= x+y
##
##if kosul0 and kosul1 and kosul2:
##    print("Verilen Kenarlarla bir üçgen oluşturulabilir")
##else:
##    print("Verilen Kenarlarla bir üçgen oluşturulamaz")
##import math
##
##print("2. Dereceden denklemin katsayılarını giriniz:")
##
##a = float(input("a Katsayısını Giriniz:"))
##b = float(input("b Katsayısını Giriniz:"))
##c = float(input("c Katsayısını Giriniz:"))
##
##disc = b**2 - (4 *a*c)
##
##if disc > 0:
##    print("discriminant 0 dan büyük olduğu için 2 real kökü vardir.")
##    root1 = (-b + math.sqrt(disc)) / (2*a);
##    root2 = (-b - math.sqrt(disc)) / (2*a);
##    print("1. Kök =>", root1)
##    print("2. Kök =>", root2)
##
##elif disc ==0 :
##    print("discriminant 0 a eşit olduğu için tek kökü vardir.")
##    root= -b / (2*a);
##    print("Kök =>", root)
##
##else:
##    print("discriminant 0 dan küçük olduğu için real kökü yoktur.")
##    


# DÖNGÜLER
# For While
# range(-start - end -step)
for i in range(50,0,-1):
    if i%2 == 0:
        print(i,"bu sayı çifttir")
    else:
        print(i,"Bu Sayı Tektir")


#150-250 arasindaki bütün çift sayıların toplamı nedir
toplam = 0
for i in range(150,251):
    if i%2 == 0:
        toplam += i

print(toplam)


