"""
İf - Else - Elif
"""
"""
if => eğer
else => değilse 
elif => eğer değilse
"""
"""
kosul = True

if kosul == True:
    print("Koşul Doğru")

if kosul != True:
    print("Koşul Doğru değil")

if not(kosul):
    print("Koşul Doğru değil")

if kosul == False:
    print("Koşul Doğru değil")


if (kosul):
    print("doğru")
else:
    print("yanlış")


ortalama = 78

# 75 <= ortalama < 85
if ortalama >= 75 and ortalama < 85:
    print("Teşekkür Aldınız Tebrikler") 
elif 85 <= ortalama <= 100:
    print("Taktir Aldınız Tebrikler")
elif 50 <= ortalama < 75:
    print("Maalesef Belge Alamadınız:")
else:
    print("Maalesef Kaldınız")


s1,s2,s3 = 45, 19,48
#bu sayıları sıralayın

if s1 > s2 and s1 > s3 and s2 > s3:
    print("s1 > s2 > s3")
elif s1 > s2 and s1 > s3 and s3 > s2:
    print("s1 > s3 > s2")
elif s2 > s1 and s2 > s3 and s1 > s3:
    print("s2 > s1 > s3")
elif s2 > s1 and s2 > s3 and s3 > s1:
    print("s2 > s3 > s1")
elif s3 > s2 > s1:
    print("s3 > s2 > s1")
elif s3 > s1 > s2:
    print("s3 > s1 > s2")

if s1 > s2 and s1 > s3:
    if s2 > s3:
        print("s1>s2>s3")
    else:
        print("s1 > s3 >s2")


#15,48,45,39,17,48,25,9,0,4,7,195,1326

# koşul = ehliyet almak için yaş >= 18 ve ilk okul mezunu olmalısınız

yas = int(input("Yaşınızı Giriniz: "))
mezun = input("İlk Okul Mezunu musunuz (E/H)")

if yas >= 18 and (mezun == "E" or mezun == "e"):
    print("Ehliyet Aabilirsiniz: ")
else:
    print("Ehliyet Alamazsınız: ")
"""

# Girilen Sayının Çift mi yoksa Tekmi aynı zamanda pozifitmi yoksa negatifmi olduğunu hesaplayan python programını yazınız

a = """
HESAP MAKİNEMİZE HOŞGELDİNİZ

1- Topla
2- Çıkarma
3- Bölme
4- Çarpma
"""

print(a)
secim = int(input("Lütfen Bir İşlem Seçiniz:"))

s1 = float(input("1. Sayıyı Giriniz:"))
s2 = float(input("2. Sayıyı Giriniz:"))

if secim == 1:
    print("Girilen iki sayının toplamı = ", s1+s2)
elif secim == 2:
    print("Girilen iki sayının farkı = ", s1-s2)
elif secim == 3:
    print("Girilen iki sayının bölümü = ", s1/s2)
elif secim == 4:
    print("Girilen iki sayının çarpımı = ", s1*s2)




