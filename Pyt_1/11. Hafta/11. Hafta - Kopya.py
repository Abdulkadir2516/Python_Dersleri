### Döngüler 2
### Listeler 1


##for i in range(1,11):
##    
##    for j in range(1,11):
##
##        print(i , " x " , j, "  =>  ", i*j)
##
##
##    print()

##
##i = 1
##while i<11:
##
##    j = a
##    while j<11:
##        print(i , " x " , j, "  =>  ", i*j)
##        j += 1
##
##    i += 1
##    print()
##    



##for i in range(1,11):
##    
##    for j in range(0,i):
##
##        print(i,end="")
##
##
##    print()
##
##
##for i in range(1,11):
##    
##    for j in range(0,i):
##
##        print(j,end="")
##
##
##    print()

##sayac = 0
##for i in range(1,6):
##    
##    for j in range(0,i):
##        sayac +=1
##
##        print(sayac,end=" ")
##
##
##    print()


##for i in range(1,6):
##
##    
##    for j in range(i,0,-1):
##        
##        print(j,end=" ")
##
##
##    print()


##for i in range(1,6):
##
##    for k in range(a-i):
##        
##        print(" ",end=" ")
##    
##    for j in range(1,i+1):
##        
##        print(j,end=" ")
##
##
##    print()


##for i in range(a):
##    
##    for j in range(a,i,-1):
##
##        print(j-i,end="")
##    print()



##for i in range(a):
##
##    for k in range(0,i):
##        print(" ",end=" ")
##        
##    for j in range(i,a):
##
##        print(j-i,end=" ")
##    print()

a =10


for i in range(a):

    for k in range(a-i,0,-1):
        print(" ",end=" ")
        
    for j in range(i):
        print(j,end=" ")

    for e in range(i-1):
        print(i-e-2,end=" ")

    print()

for i in range(a):
    for k in range(i):
        print(" ",end=" ")
        
    for j in range(a-i):
        print(j,end=" ")

    for e in range(7,-1,-1):
        print(e,end=" ")

    print()




