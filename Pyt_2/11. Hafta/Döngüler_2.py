# Koleksiyonlar
# Listeler List()
# Demetler Tuple()
# Kümeler Set()
# Sözlükler Dict()
##
mytuple = ("çilek","üzüm","kavun","elma","armut","kivi")
##print(mytuple)
##
####mytuple[0] = ("karpuz")
####print(mytuple)
##
##
##print(mytuple[0:-3])
##
##new_tuple = ("karpuz",)
##print(type(new_tuple))
##
##mytuple += new_tuple
##
##print(mytuple)

myset2 = {"apple", "banana", "cherry"}
myset = set(mytuple)
print(myset)
print(type(myset))


myset2.add("kiraz")
print(myset2)

a = {1,2,6,7}
b = {1,5,7,3}
c = {1,4,5,6}

print(b.difference(a))

b.difference_update(a)
print(b)

b = {1,5,7,3}

a.add(11)
b.add(13)
c.add(15)

a.remove(11)
b.discard(13)

print(a.intersection(c))


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) 

k = (x.union(y)).difference(x.intersection(y))
print(z)
print(k)


