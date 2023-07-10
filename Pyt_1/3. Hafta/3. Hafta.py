"""
Değişkenler = variable
Değiken tipleri ve dönüşümleri
Uygulama (Alan çevre hesabı)
input()
Uygulama
"""
"""
degisken = "bu bir yazı"
print(degisken)

degisken = "deneme" # değişkenin değerini deneme yaptık
print(degisken)

myvar = "merhaba" # true
myvar2 = "merhaba" # false

sayibir = 25
sayi_bir = 25
#sayi.Bir = 25 hatalı
#sayi-Bir = 25 hatalı

gecici = myvar2
print(myvar)
print(gecici)

dogrumu = True
basıldımı = False

ondalıklı = 48/7 #50.5 ,   

print("myvar değikeninin tipi =>", type(myvar))
print("doğrumu değikeninin tipi =>", type(dogrumu))
print("sayibir degiskeninin tipi =>", type(sayibir))
print("ondalıklı degiskeninin tipi =>", type(ondalıklı))

s1 = 3
s2 = 4
s3 = 5

print(s1+s2+s3)
s1,s2,s3 = 6,7,8
print(s1+s2+s3)

#Tip Dönüşümleri :
# int(deger), float(deger), str(deger), bool(deger)

deger = 5

print("inti boole çevirme => ", bool(deger))
print("inti float çevirme => ", float(deger))
print("inti stringe çevirme => ", str(deger))

deger = "88"

print("str to bool => ", bool(deger))
print("str to float => ", float(deger))
print("str to float int => ", int(deger))

deger = 0.0

print("float to bool => ", bool(deger))
print("float to str => ", str(deger))
print("float to int => ", int(deger))

"""
# Dikdörtgenler prizmasi için hacim ve litre hesabı
en,boy,h = 17.7,11.3,4.5
hacim = en*boy*h
print(hacim)

print("cisim toplamda =>", hacim/1000, " litredir.")

# input() kulanıcdan veri alma işlemi
en = input("cismin enini giriniz: ")
boy = input("cismin boyunu giriniz: ")
h = float(input("cismin yüksekliğini giriniz: "))

hacim = float(en)*float(boy)*h
print(hacim)

print("cisim toplamda =>", hacim/1000, " litredir.")

"""*Ödev:*
Kullanıcı boy ve kilosunu girdiğinde Beden Kitle Endeksine göre
kilolumu yoksa zayıfmı olduğunu hesaplaya python programını yazınız
"""
print("20 den küçükse zayıfsınız")

kilo = 72
boy = 1.72

print(kilo/(boy*boy))
