#DÖNGÜLER
# while => iken 

##sayac =0
##while sayac < 50:
##    sayac = sayac + 1
##    print(sayac)
##
##    if sayac == 25:
##        sayac = 51

# faktöriyel

##sayı = int(input("Faktöriyeli alınacak sayıyı giriniz:"))
##result = 1
##while sayı>0:
##    result *= sayı
##    sayı -= 1
##
##print(result)
##
##
##a = 0
##b = 1
##res = 0
##sayac = 0
##
##while sayac <20:
##    sayac +=1
##
##    res = a+b
##    a = b
##    b = res
##
##    print(res)
##
##
##sayac = 0
##while sayac < 120:
##    sayac += 1
##
##    if  78 <sayac < 90:
##        continue
##
##    print(sayac, end="  ")
##else:
##    print("döngü bitti")

## Koleksiyonlar => Listeler - Tupleler - Kümeler Set - Sözlük Dict
## LİSTELER


new_list = ["makarna","süt","ekmek"]
new_list = list(("Makarna","Süt","Su","Un","Şeker","Tuz"))

print(type(new_list))

print(new_list)

new_list.append("yumurta")
new_list += ["Cips"]

print(new_list)

print(new_list[1])

print(new_list[1:6:2])

print(new_list[5::])
print(new_list[::5])

print(new_list[::-1])


print(new_list.count("yumurta"))

print(len(new_list))

new_list.remove("Cips")
print(new_list)

new_list.pop(0)
print(new_list)

new_list.insert(3,"Çay")

print(new_list)

print(new_list.index("Tuz"))

print(new_list.index("Tuz",2,6))

a = new_list
b = new_list.copy()

a += ["deneme"]
b += ["deneme2"]
print(new_list)
new_list.remove("deneme")
print(new_list)

new_list.extend(["sabun","çekirdek"])

print(new_list)

new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)

new_list.clear()
print(new_list)






