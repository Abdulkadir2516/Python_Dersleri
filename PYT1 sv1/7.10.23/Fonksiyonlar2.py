# Fonksiyonlar Recursive Function
"""
def faktöriyel(sayi):

    if sayi <= 1:
        return 1

    
    return  sayi * faktöriyel(sayi-1)


print(faktöriyel(5))

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
        

print(fibonacci(8))
"""

import os
import math
import time


print(os.name)

print(os.getcwd())

os.chdir("../../")
print(os.listdir())

print(time.time())

time.sleep()

print("hello")








