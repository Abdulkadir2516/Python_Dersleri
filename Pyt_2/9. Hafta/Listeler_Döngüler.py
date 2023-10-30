# DÖNGÜLER 2
# LİSTELER 2

##count()	Returns the number of elements with the specified value
##index()	Returns the index of the first element with the specified value

##random = [15, 6, 4, -75, 758, 75, 45, 744,4,6,15,4,4]
##
##print(random)
##
##eleman = 6
##toplam = 0
##
##for i in range(len(random)):
##
##    if random[i] == eleman:
##        toplam += 1
##
##print(toplam)
##
##
##
###range(10) # [0,1,2,3,4,5,6,7,8,9]
##
##x = list(range(10))
##print(x)
##
##random = [15, 6, 4, -75, 758, 75, 45, 744,4,6,15,4,4]
##
##print(random)
##
##eleman = 758
##index = 0
##
##for i in random:
##    
##    if i == eleman:
##        break
##    
##    index +=1
##    
##print(index)

# İç İçe Döngüler
##
##for i in range(2):
##    
##    for j in range(2):
##
##        for k in range(5):
##            print(i, "  ", j, "  ", k)
##
##    print()
##
##s1 = 0
##while s1<5:
##    s1+=1
##    s2 = 0
##    while s2<5:
##        s2 +=1
##        s3 = 0
##        while s3< 5:
##            s3 += 1
##            print(s1,"  ", s2, " " , s3)

#UYGULAMALAR
##            1-Asal Sayı Bulma
##            2-İki Sayı Aralığındaki asal Sayılar

# asal nedir?
# 1 ve kendinden başkasına kalansız bölünemeyen 1den büyük sayma sayıları denir
##while True:
##        
##    sayi = int(input("Bir Sayı Giriniz:"))
##    asalmı = True
##
##    for i in range(2,sayi):
##
##        if sayi % i == 0:
##            asalmı = False
##            break
##            
##    if asalmı:
##        print("bu sayı asaldır.")
##    else:
##        print("Asal Değildir.")
##

##
##for j in range(2,100000):
##
##    sayi = j #int(input("Bir Sayı Giriniz:"))
##    asalmı = True
##
##    for i in range(2,int(sayi/2)):
##
##        if sayi % i == 0:
##            asalmı = False
##            break
##            
##    if asalmı:
##        print(sayi, end="  ")
##        #print("bu sayı asaldır.")
####    else:
####        print("Asal Değildir.")
##
##
##
##input()


# Çarpım Tablosu

##for i in range(1,11):
##
##    for j in range(1,11):
##
##        print(i ," x ", j , " => ", i*j)
##
##    print()
##



for j in range(2,14000):

    sayi = j #int(input("Bir Sayı Giriniz:"))
    asalmı = True

    for i in range(2,int(sayi/2)):

        if sayi % i == 0:
            asalmı = False
            break
            
    if asalmı:
        
        x = 2**sayi - 1

        sayi2 = x #int(input("Bir Sayı Giriniz:"))
        asalmı2 = True

        for i in range(2,int(sayi2/2)):

            if sayi2 % i == 0:
                asalmı2 = False
                break

        if asalmı2:
            print(sayi, "Mersenne Asalıdır")
        
        #print("bu sayı asaldır.")
##    else:
##        print("Asal Değildir.")



input()






