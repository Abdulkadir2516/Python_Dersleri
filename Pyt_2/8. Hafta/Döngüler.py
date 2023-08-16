# DÖNGÜLER
# LİSTELER

##a = 0
##while a < 5:
##    a += 1
##    print(a)
##else:
##    print(a)

# Koleksiyonlar => Listeler (List), Demetler (Tuple), Kümeler (Set), Sözlük (Dict)
##
##liste = ["deneme2"]
##print(liste)
##print(type(liste))
##liste = list(["deneme"])
##print(liste)


##fruits = ["Elma","Armut","Karpuz","Kavun","Mandalina","Domates","Şeftali"]
##asallar = [2,3,5,7,11,17,19,23,29,31,37,41,43]
##
##print(fruits)
##print(asallar)
##
##
##print(fruits[3])
##print(asallar[3])
##print(asallar[-3])
##
##düzenli_liste = list(range(10,100,7))
##print(düzenli_liste)
##
##print(fruits[5:10])
##print(asallar[5:10])
##
##print(fruits[5:10:2])
##print(asallar[5:10:2])
##print(düzenli_liste[5:20:2])
##
##
##print(asallar[-5])
##print(asallar[-10:-3])
##
##print(düzenli_liste[::-1])
##
##print(len(asallar))

fruits = ["Elma","Armut","Karpuz","Kavun","Mandalina","Domates","Şeftali"]
asallar = [2,3,5,7,11,17,19,23,29,31,37,41,43]

fruits += ["Kayısı"]

fruits[2] ="Erik"

##print(fruits)

##fruits.append("Çilek")
##print(fruits)
##
##fruits.insert(3,"Üzüm")
##print(fruits)
##
##fruits.pop()
##print(fruits)
##
##fruits.pop(5)
##print(fruits)
##
##fruits.remove("Üzüm")
##print(fruits)
##
##fruits.sort(reverse=False)
##print(fruits)
##
##fruits.sort(reverse=True)
##print(fruits)
##
##random = [15,6,4,848,29,15,155,24,152,15,25,54,57,48,39,58,184,65,245,5,778,545,75,758,75,45,744,]
##print(random)
##
##random.sort(reverse=False)
##print(random)
##
##random.sort(reverse=True)
##print(random)
##
##print(random.count(15))
##print(random.count(75))
##
##random = [15,6,4,848,29,15,155,24,152,15,25,54,57,48,39,58,184,65,245,5,778,545,75,758,75,45,744,]
##
##random.reverse()
##print(random)
##
##random = [15,6,4,848,29,15,155,24,152,15,25,54,57,48,39,58,184,65,245,5,778,545,75,758,75,45,744,]
##
##random = random[::-1]
##print(random)

random = [15,6,4,-75,758,75,45,744,]

a = random
b = random.copy()

print(a)
print(b)
print(random)

a.append(6)
b.append(48)


print(fruits.index("Kavun"))

x = [1,2,3]
y = [4,5,6]
x.extend(y)
print(x)
x += y
print(x)


