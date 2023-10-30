# Fonksiyon = Metodlar

# f(x) = x+1

# f(x,y) = x+y

# definition = Tanımlama
def topla(x,y):
    print(x+y)

    return x+y

def hello():# parametresiz geri değer döndürmeyen
    print("merhaba fonksiyonlar")
    

def hi(x):#parametreli geri değer döndürmeyen
    print("x parametreli merhaba", x)


##def alan(genislik, uzunluk):
##
##    x = genislik * uzunluk
##    return x
##
##g = int(input("genişlik giriniz:"))
##u = int(input("uzunluk giriniz:"))
##
##alan = alan(g,u)
##
##print(alan)



def fonk(a,b,c=5):

    return a+b+c


def liste_olustur(start=0,stop=10,step=1):

    my_list = []

    
    while start<stop:

        my_list.append(start)

        start += step

    return my_list


def liste_olustur2(*parametre):
    start = 0
    stop = parametre[0]
    step = 1

    if len(parametre) == 2:
        start = parametre[0]
        stop = parametre[1]
    elif len(parametre) == 3:
        start = parametre[0]
        stop = parametre[1]
        step = parametre[2]


    my_list = []

    while start<stop:

        my_list.append(start)

        start += step

    return my_list



def fonksiyon(x):

    if x>500:
        return 500

    print(x)

    return fonksiyon(x+1)
    




x = "Programımıza Hoşgeliniz"

a = """
Açıklama: aşağıda gördühünüz cisimlerin hacimlerini hesaplayabiliyoruz

1 : Küp
2 : Silindir
3 : Dikdörtgenler Prizması
4 : Küre

"""
print(x,"\n",a)



def kup(a):
    return a*a*a

def silindir(r,h,pi=3.1415):
    return pi*h*(r**2)

def dikdortgen(a,b,c):
    return a*b*c

def küre(r,pi=3.1415):
    return 4/3*pi*(r**3)


secim = input("Lütfen Bir Cisim Seçiniz: ")

if secim == "1" or secim.lower() == "küp":

    a = int(input("Kübün Bir Kenarının Uzunluğunu Giriniz: "))
    print(kup(a))

elif secim == "2" or secim.lower() == "silindir":
    r = int(input("Silindirin Yarı çapını giriniz: "))
    h = int(input("Silindirin Yüksekliğini giriniz: "))
    print(silindir(r,h))

































