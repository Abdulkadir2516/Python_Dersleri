# STRİNG Metodları
# regex import re

##met = "Python Girintiler dayalı modüler bir programlama dilidir."
##
##met = met.replace(" ", ",")
##
##a = met.split(",")
##
##print(met)


x = """
Programımıza hoş geldiniz:

Giriş Yapmak için 1e:
Üye olmak için 2ye Basınız:

"""

print(x)
sec = input()

# w => dosya yoksa oluştur ve sıfırdan yaz
# x => sadece dosya oluştur.
# a => dosyaya ekleme yap
# r => dosyayı oku

import os

if sec == "2":

    k_ad = input("Kullanıcı Adınızı Giriniz:")
    sifre = input("Şifrenizi Giriniz:")

    if not(os.path.exists("kullanıcı.txt")):
        data = open("kullanıcı.txt", "w")
        yazı = "Kullanıcı Adı,Şifre\n"
        data.write(yazı)

    data = open("kullanıcı.txt", "r")
    data = data.read()
    
    if k_ad in data and sifre in data:
        print("böyle bir kullanıcı bulunmaktadır")

    else:
        data = open("kullanıcı.txt", "a")
        yazı = f"{k_ad},{sifre}\n"
        data.write(yazı)

        data = open("kullanıcı.txt", "r")
        data.read()

elif sec == "1":

    k_ad = input("Kullanıcı Adınızı Giriniz:")
    sifre = input("Şifrenizi Giriniz:")
    
    data = open("kullanıcı.txt", "r")
    data = data.read()
    data = data.replace("\n",",")
    new_data = data.split(",")

    for i in range(0,len(new_data),2):

        if k_ad == new_data[i] and sifre == new_data[i+1]:

            print("Giriş Başarılı")
            break
                











