"""
İf - Else - Elif

"""

kosul = True
"""
if kosul:
    print("Koşulumuz Doğru 0")

if not(kosul):
    print("Koşulumuz Doğru değil 0")

if kosul == False:
    print("Koşulumuz Doğru değil 1")

if kosul != False:
    print("Koşulumuz Doğru 1")

if kosul == True:
    print("Koşulumuz Doğru 2")

if kosul != True:
    print("Koşulumuz Doğru değil 2")
"""
"""
kosul = True

if kosul == True:
    print("Koşul Doğru")
else:
    print("Koşul Doğru Değildir.")

sayi = 1

if sayi == 0:
    print("Sayı Sıfıra Eşittir.")
elif sayi == 1:
    print("Sayı Bire Eşittir.")
elif sayi == 2:
    print("Sayı ikiye Eşittir")
else:
    print("Sayı 0 1 2 ye eşit değil")

if sayi > 0:
    print("Sayı sıfırdan büyüktür")

"""

# girilen sayının çiftmi yoksa tekmi olduğunu hesaplayan progem
#sayi = float(input("Bir Sayı Giriniz:"))
##
##if sayi%2 == 0:
##    print("Girilen Sayı Çifttir")
##else:
##    print("Girilen Tektir")
##
##if sayi>0:
##    print("Girilen Sayı Pozitiftir")
##elif sayi<0:
##    print("Girilen Sayı Negatiftir.")
##elif sayi == 0:
##    print("Girilen Sayı Nötr.")
##else:
##    print("Bir Yanlışlık Oldu Sanırım")
"""
while True:
    sayi = float(input("Bir Sayı Giriniz:"))
    if sayi%2 == 0 and sayi>0:
        print("Girilen Sayı Çifttir ve Pozitiftir.")
    elif sayi%2 == 0 and sayi<0:
        print("Girilen Sayı Çifttir ve Negatiftir.")
    elif sayi%2 == 0 and sayi==0:
        print("Girilen Sayı Çifttir ve Nötrdür.")
    elif sayi%2 == 1 and sayi>0:
        print("Girilen Sayı Tektir ve Pozitiftir.")
    elif sayi%2 == 1 and sayi<0:
        print("Girilen Sayı Tektir ve Negatiftir.")

while True:
    sayi = float(input("Bir Sayı Giriniz:"))
    if sayi % 2 == 0:
        if sayi>0:
            print("Girilen Sayı Çift ve Pozitiftir")
        elif sayi<0:
            print("Girilen Sayı Çift ve Negatiftir.")
        else:
            print("Girilen Sayı Çift ve Nötr.")
    else:
        if sayi>0:
            print("Girilen Sayı Tek vePozitiftir")
        elif sayi<0:
            print("Girilen Sayı Tek ve Negatiftir.")

"""
a = """
HACİM HESAPLAMA PROGRAMINA HOŞGENLDİNİZ
******************************************************
Üç Boyulu Bir Cisim Seçin:

1- Küp
2- Dikdörtgenler Prizması
3- Küre
4- Silindir
5- Koni
6- Kare Piramit
"""
print(a)
while True:
    secim = int(input("\nseçmek için 1 ile 6 arasında bir sayı seçin ve entera tıklayın çıkmak için q ya basın\n"))

    if secim ==1:
        x = float(input("Küpün Bir Kenar Uzunluğunu Giriniz: "))
        print("Küpün Hacmi => ", x**3)

    elif secim == 2:
        x = float(input("Nesnenin Enini Giriniz: "))
        y = float(input("Nesnenin Yüksekliğini Giriniz: "))
        z = float(input("Nesnenin Genişliğini Giriniz: "))
        print("Cismin Hacmi => ", x*y*z)

        















