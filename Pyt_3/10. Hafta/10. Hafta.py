# STRİNG Text


##metin = """
##Python,
##nesne yönelimli,
##yorumlamalı, birimsel ve
##etkileşimli yüksek seviyeli
##bir programlama dilidir.
##Girintilere dayalı basit söz dizimi,
##dilin öğrenilmesini ve akılda kalmasını kolaylaştırır."""
##
##print(metin)
##
##print(metin[0:10])
##
##metin2 = metin#input("Bir Metiniz:")
##
##key = input("aranan sözcük giriniz:")
##toplam =0
##
##print(metin2.find(key))
##        
##print(key in metin2)   

##print(metin[::-1])
##
##print(metin.capitalize)
##

x = """
Programııza hoş geldiniz:

Giriş Yapmak için 1e:
Üye olmak için 2ye Basınız:

"""

print(x)
sec = input()

if sec == "2":

    k_ad = input("Kullanıcı Adınızı Giriniz:")
    sifre = input("Şifrenizi Giriniz:")

    data = open("kullanıcı.txt", "w")
    yazı = f"{k_ad},{sifre}\n"
    data.write(yazı)
    
    data = open("kullanıcı.txt", "r")
    data.read()














