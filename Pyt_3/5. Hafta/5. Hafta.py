"""
İf - Else Uygulamalar

"""
"""
#print("5 8 den büyüktür")  if 55>8 else print("5 8 den büyük değil 48 58 den büyüktür") if 68>58 else print("48 58 ve 5 8 den büyük değildir")

# bir üçkenin 3 kenar boyutundan bu üçgenin var olup olamayacağını kontrol eden python programı

k1 = float(input("Üçgenin 1. Kenarını Giriniz:"))
k2 = float(input("Üçgenin 2. Kenarını Giriniz:"))
k3 = float(input("Üçgenin 3. Kenarını Giriniz:"))

maks =0

if k1< k3 and k3 > k2:
    maks = k3
    if k1>k2:
        second = k1
        last = k2
    else:
        second = k2
        last = k1
    
elif k1< k2 and k2 > k3:
    maks = k2
    if k1>k3:
        second = k1
        last = k3
    else:
        second = k3
        last = k1
    
else:
    maks = k1
    if k3>k2:
        second = k3
        last = k2
    else:
        second = k2
        last = k3


print("first => ", maks)
print("second =>", second)
print("last => ", last)

kosul0 = second-last <= maks <= second+last
kosul1 = maks-last <= second <= maks+last
kosul2= maks-second <= last <= second+maks
kosul3 = False

if kosul0 and kosul1 and kosul2:
    print("Bu Üçgen Boyutları Uygun")
    kosul3 = True
else:
    print("Bu Üçgen Boyutları Uygun Değil")


if kosul3:
    if k1 == k2 and k2 == k3:
        print("Eşkenar Üçgendir")
    elif k1 == k2 or k2 == k3 or k1 == k3:
        print("İkiz Kenar Üçgendir")
    elif k1 != k2 or k2 != k3 or k1 != k3:
        print("Çeşitkenar Üçgendir")
"""

## DÖNGÜLER

#For - While => iken 
"""
for i in range(20):
    if i%2 == 0:
        print(i)


for i in range(20):
    print(20-i)

"""
x = 8
y = 3
result = 0

for i in range(x):
    result +=y
    print(result , end=" " )

print()
print(result)


#Faktöriyel
#Fibonacci Dizisi

fak = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı Giriniz:"))
result = 1
for i in range(1,fak+1):
    result *= i

print(result)



a = 1
b = 1
c = 1
for i in range(20):
    print(c)
    c = a+b
    a = b
    b = c
    #print(a ," ", b ," " , c)



















