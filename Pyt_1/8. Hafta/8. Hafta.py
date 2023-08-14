# Döngüler
# While

##while True:
##        
##    sayi = int(input("Faktöriyeli Alınacak sayıyı giriniz:"))
##
##    sonuc = 1
##    while sayi > 0:
##        sonuc *= sayi
##        print(sayi , "   ", sonuc)
##        sayi -= 1
        

##
##first = 0
##second = 1
##result = 0
##
##x = 251567489
##print(1, ". terimi =>" ,first)
##print(2, ". terimi =>" ,second)
##
##sayac = 3
##while result < x:
##    result = first + second
##    first = second
##    second = result
##    print(sayac , ". terimi =>" ,result)
##    sayac += 1


first = 0
second = 1
result = 0

x = 251567489
print(1, ". terimi =>" ,first)
print(2, ". terimi =>" ,second)

sayac = 3
while True:
    result = first + second
    first = second
    second = result

    if sayac == 15:
        sayac +=1
        continue
    
    print(sayac , ". terimi =>" ,result)
    sayac += 1

    if result > x :
        break
    






