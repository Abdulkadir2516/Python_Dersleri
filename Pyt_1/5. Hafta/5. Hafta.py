## İf Else Elif
"""
if eğer ise

else  değil ise

else if => elif
"""
#dışarı çıkmak istiyorum
"""
ödev_yaptınmı = True #1. koşul

etrafı_topladınmı = False # 2. koşul


if ödev_yaptınmı == True or etrafı_topladınmı ==True:
    print("Dışarıya Çıkabilirsin")
"""
"""
print("Ehliyet Başvurusuna Hoş Geldiniz: ")

yas = int(input("Kaç Yaşındasınız:"))

soru = input("İlk Okul Mezunu musunuz (E,e/H,h) ")

if yas>=18 and (soru=="E" or soru == "e"):
    print("Ehliyet Alabilirsiniz1")
else:
    print("Ehliyet Alamazsınız1")

print("############")
"""
##soru = input("İlk Okul Mezunu musunuz (E,e/H,h) ")
##soru = soru[0].lower()
##
##if yas>=18 and soru == "e":
##    print("Ehliyet Alabilirsiniz2")
##else:
##    print("Ehliyet Alamazsınız2")


s1,s2,s3 = 480,111,196

if s1>s2 and s1>s3:
    print("Sayı Bir ", s1 ," diğer Sayılardan büyüktür. ")
    if s2>s3:
        print("Sayı2 ", s2 ," Sayi 3 ten ",s3," büyüktür. ")
    else:
        print("Sayı 3 ", s3 ," Sayi 2 den ",s2," büyüktür. ")

if s1>s2 and s1>s3 and s2>s3:
    print("S1 > S2 >S3")
elif s1>s2 and s1>s3 and s3>s2:
    print("S1 > S3 >S2")


if s2>s1 and s2>s3:
    print("Sayı İki ", s2 ," diğer Sayılardan büyüktür. ")

if s3>s1 and s3>s2:
    print("Sayı Üç ", s3 ," diğer Sayılardan büyüktür. ")




