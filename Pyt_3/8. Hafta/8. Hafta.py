# İç İçe Döngüler


##for i in range(5):
##
##    for j in range(5):
##
##        print("i değeri => " , i , "j değeri =>", j)
##
##    print()

##for i in range(0,11):
##    print(11-i, end="    ")
##    for j in range(0,i):
##
##        print(i, end=" ")
##
##    print()
##    

##print("*\n")
## 
##for i in range(1,10):
##
##    print("*", end=" ")
##     
##    for j in range(1,i+1):      
##        print("     ",end=" ")
##              
##    print("*\n");
##    
##
##sayac = 0
##for i in range(0,10):
##
##    for j in range(10-i):
##        print(" ", end=" ")
##
##    for j in range(i,0,-1):
##        print(j, end="")
##
##    print()


#Asal Sayı Tespiti
# girilen sayıların asal olup olmadığını tespit eden program

##for j in range(2,10000):
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
##        print(j,end="  ")
##

#7,121,393,555,888,777,6446
for k in range(10000):
    
    sayi = list(str(k))#list(input("bir sayı giriniz"))
    uzunluk = len(sayi)

    if uzunluk % 2 ==0:
        uzunluk2 = int(uzunluk / 2 )
    else:
        uzunluk2 = int(uzunluk / 2 )

    if uzunluk == 1:
        kosul = True

    for i,j in zip(range(0,uzunluk2),range(uzunluk-1,uzunluk2-1,-1)):
        kosul = sayi[i] == sayi[j]

        if not(kosul):
            #print(k, end="  ")
            break

    if kosul:
        print(k, end="  ")


input()
input()









