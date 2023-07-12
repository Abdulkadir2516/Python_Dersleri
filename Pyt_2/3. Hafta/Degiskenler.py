"""
Değişkenler = variable var
Değiken tipleri ve dönüşümleri
Uygulama (Alan Çevre Hacim litre VKİ hesabı)
input()
Uygulama
"""
# Yorum satırı
"""
a = 15
b = 48
yorum = "python çok güzel bir dilmiş #lovepython"
kullanici_adi = "greenrock"

print(a)
print(b)
print(yorum)
print(kullanici_adi)

# Hatalı Değişken kullanımlar
##2myvar = "John" 
##my-var = "John"
##my var = "John"
##myvar! = "John"

s1 = 5
s2 = 3
s3 = 4

print(s1+s2+s3)

s1,s2,s3 = 9,8,7

print(s1+s2+s3)

new_var = s1

print(new_var)

print(type(s1))
print(type(yorum))


my_int = 25
my_float = 12.5
my_string = "25.5"
my_boolean = False

a = float(my_string)
print("string to float =>", a)
print("float to int =>", int(a))

my_int = 0
my_float = 0.0
my_string = " "
my_boolean = True

print("string to bool =>", bool(my_string))
print("int to bool =>", bool(my_int))
print("float to bool =>", bool(my_float))

print("bool to string =>", str(my_boolean))
print("bool to int =>", int(my_boolean))
print("bool to float =>", float(my_boolean))
"""

#Beden Kitle Endeksi Hesaplama
# vki = kilo/boy * boy (m^2)

kilo = 87
boy = 1.91

vki = kilo / boy**2

print("""
18, 5 kg/m² ‘nin altındaki sonuçlar: İdeal kilonun altında
18, 5 kg/m² ile 24, 9 kg/m² arasındaki sonuçlar: İdeal kiloda
25 kg/m² ile 29, 9 kg/m² arasındaki sonuçlar: İdeal kilonun üstünde
30 kg/m² ile 39, 9 kg/m² arasındaki sonuçlar: İdeal kilonun çok üstünde (obez)
40 kg/m² üzerindeki sonuçlar: İdeal kilonun çok üstünde (morbid obez)
""")

print("Beden Kitle Endeksiniz => ", vki)

print("########################################################")
print("########################################################")

kilo = input("Kilonuzu Giriniz:")
boy = float(input("Boyunuzu Giriniz: (örn: 1.72)"))

vki = int(kilo) / boy**2

print("""
18, 5 kg/m² ‘nin altındaki sonuçlar: İdeal kilonun altında
18, 5 kg/m² ile 24, 9 kg/m² arasındaki sonuçlar: İdeal kiloda
25 kg/m² ile 29, 9 kg/m² arasındaki sonuçlar: İdeal kilonun üstünde
30 kg/m² ile 39, 9 kg/m² arasındaki sonuçlar: İdeal kilonun çok üstünde (obez)
40 kg/m² üzerindeki sonuçlar: İdeal kilonun çok üstünde (morbid obez)
""")

print("Beden Kitle Endeksiniz => ", vki)



 
