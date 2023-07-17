##"""*Ödev:*
##Kullanıcı boy ve kilosunu girdiğinde Beden Kitle Endeksine göre
##kilolumu yoksa zayıfmı olduğunu hesaplayan python programını yazınız
##"""
##
##kilo = float(input("Kilonuzu Giriniz:"))
##boy = float(input("Boyunuzu Giriniz: (örn: 1.72)"))
##
##a = """
##18, 5 kg/m² ‘nin altındaki sonuçlar: İdeal kilonun altında
##18, 5 kg/m² ile 24, 9 kg/m² arasındaki sonuçlar: İdeal kiloda
##25 kg/m² ile 29, 9 kg/m² arasındaki sonuçlar: İdeal kilonun üstünde
##30 kg/m² ile 39, 9 kg/m² arasındaki sonuçlar: İdeal kilonun çok üstünde (obez)
##40 kg/m² üzerindeki sonuçlar: İdeal kilonun çok üstünde (morbid obez)
##"""
##print(a)
##print(kilo/(boy*boy))
##
##input()

# Operatörler

# 1 Matematiksel Aritmetiksel Operatörler (+-*/%**//)
# 2 Atama Operatörleri
# 3 İlişkisel Operatörler
# 4 Mantıksal Operatörler
# 5 Bitsel Operatörler
# 6 Hafıza Operatörleri


print("1 Matematiksel Aritmetiksel Operatörler")

a = """
Operator	Name	                    Example
+	Addition                        x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	                    x / y	
%	Modulus	                    x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

"""
print(a)

print("2 Atama Operatörleri")

print("""
Operator	Example	Same As
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3
""")

##x = 2
##print(x)
##x += 5
##print(x)
##x *= 3
##print(x)
##x %=2
##print(x)
##x **= 182
##print(x)
##x -= 3
##print(x)
##x **= 5
##print(x)
##x //= 5
##print(x)

print("3 İlişkisel Karşılaştırma Operatörler")

print("""
Operator	Name	                                        Example
==	Equal	                                        x == y	
!=	Not equal	                                        x != y	
>	Greater than	                    x > y	
<	Less than	                                        x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	                    x <= y
""")


print("4 Mantıksal Operatörler") #(and or not)

vize = 40#%40
final = 50#%60

ortalama = (final*0.6) + (vize*0.4)

print(("Geçme Şartı Final 50 den yüksek ve ortalama 45 ten yüksek olmak zorunda"))
print("Ortalama",ortalama)
print("Vize",vize)
print("Final",final)

sorgu = final>=50 and ortalama >=45

print("Geçme Durumu =", sorgu)

print("50ye eşit veya küçük veya 70tenbüyük bir tam sayı giriniz")

sayi = int(input("Sayınız: "))

print("Doğru Sayı Girme Durumu =>", sayi <= 50 or sayi > 70)

print("Doğru Sayı Girme Durumu =>", sayi == 50 or sayi < 50 or sayi > 70)

print(not(True))
print(not(False))

a = "hello World"

print("Wor" in a)


