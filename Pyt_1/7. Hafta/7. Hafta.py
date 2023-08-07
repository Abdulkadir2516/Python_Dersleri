# Döngüler
# For While
#For = İçin 
#While = İken
# Range = Aralık

##for i in range(10):
##    print(i)
##
##for i in range(-8,20): # Start, Stop, Step
##    print(i)
##
##for i in range(0,50,2): # Start, Stop, Step
##    print(i)

##for i in range(50): #Start=0, Stop=50, Step=1
##    print(i)
##
##for i in range(50,6,-1): #Start=50, Stop=6, Step=-1
##    print(i)
##
##for i in range(100):
##
##    if i%2 ==0:
##        print(i)


#0-100 arasındakı 5e ve 11e bölünebilen tüm tam sayıları bastıralım

##for i in range(200):
##
##    if i%5 ==0 and i%11 == 0:
##        print(i)

##Faktöriyel
##5! => 5*4*3*2*1
##
##sayi = int(input("Faktöriyeli alıncak sayıyı giriniz:"))
##sonuc = 1
##for i in range(sayi,0,-1):
##    sonuc = sonuc*i
##    print(sonuc)
##
### 0 1 1 2 3 5 8 13 21 34 55 89 144 233
##
##a = 0
##b = 1
##c = 0
##for i in range(20):
##    c = a+b
##    a = b
##    b = c
##    print(c)
##    
##    


##kosul = True
##while kosul : # bu koşul doğru olduğu surece döngü tekrar etmeye devam eder
##
##    print("hello world")
##
##    a = input("Q tuşuna basarsanız çıkar")
##
##    if a == "Q":
##        kosul = False


for i in range(50,6,-1): #Start=50, Stop=6, Step=-1
    print(i)

sayi = 50
while sayi > 6:
    print(sayi)
    sayi = sayi-1
else:
    


