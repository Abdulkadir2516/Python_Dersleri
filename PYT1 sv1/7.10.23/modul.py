

pi = 3.1415

class hacim_hesapla():

    def kup(a):
        """
        girdi a değeri integer bir kenar uzunluğu
        çıktı a ya bağlı olan bir küpün hacmi
        """
        return a*a*a

    def silindir(r,h,pi=3.1415):
        return pi*h*(r**2)

    def dikdortgen(a,b,c):
        return a*b*c

    def küre(r,pi=3.1415):
        return 4/3*pi*(r**3)

class alan_hesapla():

    
    def kare(a):
    
        return a*a

    def daire(r,pi=3.1415):
        return pi * (r**2)

    def dikdortgen(a,b):
        return a*b

    def ücgen(t,h):
        return (t*h)/2


