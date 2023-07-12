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
input()

 
