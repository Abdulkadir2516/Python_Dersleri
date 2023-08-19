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

sayac = 0
for i in range(0,10):

    for j in range(10-i):
        print(" ", end=" ")

    for j in range(i,0,-1):
        print(j, end="")

    print()














