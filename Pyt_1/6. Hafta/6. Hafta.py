# İF Else uyuglamalar

x = input("Bir Harf Giriniz: ")

alfabe = "abcçdefgğhiıjklmnoöprsştuüvyz"

if x.lower() in alfabe:
    print("Bu Harf Alfabede Var")
else:
    print("Bu Harf Alfabede Yok")

# 1 ile 365 arasında bir gün verilip o günün hangi gün hangi ay olduğunu hesaplayan python programını yazınız

gun = int(input("1 ile 365 arasında bir gün seçiniz:"))
ilk_gun = input("Şuan Bulunduğunuz yılın ilk günü hangi gündü (Pazartesi, Salı)")
gunler = ["Pazartesi", "Salı", "Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]

#gunler[gunler.index(ilk_gun)%7]

x =gunler.index(ilk_gun)

kalan = gun % 7

if kalan == 1:
    print(gunler[x%7] ," Günü")
elif kalan == 2:
    print(gunler[(x+1)%7]," Günü")
elif kalan == 3:
    print(gunler[(x+2)%7], " Günü")
elif kalan == 4:
    print(gunler[(x+3)%7]," Günü")
elif kalan == 5:
    print(gunler[(x+4)%7]," Günü")
elif kalan == 6:
    print(gunler[(x+5)%7]," Günü")
elif kalan == 0:
    print(gunler[(x+6)%7]," Günü")








