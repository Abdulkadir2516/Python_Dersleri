# İç İçe Döngüler Uygulamalar


#Asal Sayı Tespiti
# girilen sayıların asal olup olmadığını tespit eden program

##for j in range(2,20):
##
##    sayı = j#int(input("Bir Sayı giriniz:"))
##    asalmı = True
##
##    for i in range(2,int(sayı/2),1):
##
##        if sayı % i == 0:
##            asalmı = False
##
##    if asalmı:
##        sayı2 = 2**sayı-1
##
##        asalmı2 = True
##
##        for j in range(2,int(sayı2/2),1):
##
##            if sayı2 % j == 0:
##                asalmı2 = False
##
##        if asalmı2:
##            print(sayı," sayısı Mersenne Asalıdır.")

##def asalmı(sayi):
##
##    sayı = sayi
##    asalmı = True
##
##    for i in range(2,int(sayı/2)+1,1):
##
##        if sayı % i == 0:
##            asalmı = False
##
##    if asalmı:
##        return sayı
##    else:
##        return 0
##
##    
##for i in range(2,15):
##    a = asalmı(i)
##    x = 2**a-1
##    b = asalmı(x)
##
##    if b !=0:
##        print(a,"mersenne asalıdır")
##    

##
##for i in range(1,100000):
##        
##    sayı = i #int(input("Bir Sayı Giriniz: "))
##    toplam = 0
##    tam_bolenler = []
##
##    for i in range(1,int(sayı/2)+1):
##
##        if sayı % i == 0:
##            tam_bolenler.append(i)
##            toplam += i
##
##    if toplam == sayı:
##        print(sayı, " Sayısı Mükemmel Bir Sayıdır.")
##
##
##input()
##input()


##for j in range(10000):
##        
##    sayı = str(j) #list(input("Bir Sayı Giriniz:"))
##
##    bas_count = len(sayı)
##    toplam = 0
##
##    for i in sayı:
##        toplam += int(i)**bas_count
##        
##    if toplam == int(sayı):
##        print(sayı, " Sayısı Armstrong Sayısıdır")


##for j in range(1,1000):
##        
##    sayı = str(j) #list(input("Bir Sayı Giriniz:"))
##
##    toplam = 0
##
##    for i in sayı:
##        toplam += int(i)
##
##    if int(sayı) % toplam == 0:
##        #print(sayı, " Sayısı Bir Harshad Sayısıdır.")
##        print(sayı, end="  ")


##for i in range(1,380):
##        
##    sayı = i #int(input("Bir Sayı Giriniz: "))
##    toplam = 0
##    tam_bolenler = []
##
##    for i in range(1,int(sayı/2)+1):
##
##        if sayı % i == 0:
##            tam_bolenler.append(i)
##            toplam += i
##
##    if toplam > sayı:
##        print(sayı, " Sayısı Zengin Bir Sayıdır.")
##
##
##input()
##input()

##for i in range(100):
##    print(2**(2**i)-1)

def asalmı(sayi):

    sayı = int(sayi)
    asalmı = True

    for i in range(2,int(sayı/2)+1,1):

        if sayı % i == 0:
            asalmı = False

    if asalmı:
        return True
    else:
        return False

for i in range(2,2000):
    sayı = str(i) #input("bir Sayı Giriniz:")
    sayı2 = sayı[::-1]

    if asalmı(sayı) and asalmı(sayı2):
        #print(sayı, " Sayısı Bir Lasa Sayısıdır.")
        print(sayı, end="  ")
        
