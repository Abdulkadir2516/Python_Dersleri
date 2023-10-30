# DÖNGÜLER 2
# LİSTELER 2

##Palindromik Sayılar
##
##Düz ve tersten (soldan ve sağdan) okunuşları aynı olan sayılara palindromik sayı denir.
##for i in range(1,10000):
##    
##    sayi = str(i) #input("Bir Sayı Giriniz: ")
##
##    bsm = len(sayi)
##
##    orta = int(bsm/2)
##
##    ilk_yarım = sayi[:orta]
##
##    if len(sayi) % 2 == 0:
##        son_yarım = sayi[:orta-1:-1]
##    else:
##        son_yarım = sayi[:orta:-1]
##
##    if ilk_yarım == son_yarım:
##        print(sayi, end="  ")
##    
##
##for j in range(1000000000):
##    sayi = j #int(input("Bir Sayı Giriniz: "))
##    toplam = 0
##    tam_bölenler = []
##
##    for i in range(1,int(sayi/2)+1):
##
##        if sayi % i == 0:
##            tam_bölenler.append(i)
##            toplam += i
##        
##    if toplam == sayi:
##        print(f"{sayi} sayısı mükemmel bir sayıdır.")
##
##
##input()


############################################
##
##for j in range(2,14000):
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
##        
##        x = 2**sayi - 1
##
##        sayi2 = x #int(input("Bir Sayı Giriniz:"))
##        asalmı2 = True
##
##        for i in range(2,int(sayi2/2)):
##
##            if sayi2 % i == 0:
##                asalmı2 = False
##                break
##
##        if asalmı2:
##            #print(sayi, "Mersenne Asalıdır")
##            
##            m_sayi = 2**(sayi-1) * sayi2
##            print(m_sayi)
##
##
##input()
##
##for j in range(1000000000):
##        
##    sayi = str(j) # input("bir sayı giriniz:")
##    toplam =0
##
##    #if "0" in sayi or "1" in sayi:
##
##        #toplam += sayi.count("0")
##        #toplam += sayi.count("1")
##
##    for i in sayi:
##
##        bsm = len(sayi)
##        toplam += int(i)**bsm
##
##    if toplam == int(sayi):
##        #print("{} bu sayı bir armstrong bir sayıdır.".format(sayi))
##        print(f"{sayi}", end="  ")
##
##
##input()


for i in range(10):
    x = (2**(2**i))+1
    print(f"F{i} => {x}")



