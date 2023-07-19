"""
Opertörler
"""

print("1- Matematiksel Aritmetik Opertörler")

a = """
Operator	Name	                    Example 
+	Addition	                    x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	                    x / y	
%	Modulus	                    x % y	
**	Exponentiation	x ** y
"""

print(a)

print("2 Atama Operatörleri")

s1,s2 = 5,10

s1 = s1 + 48
print(s1)

s2 += 40
print(s2)

a = """
Operator	Example	Same As
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3
"""
print(a)

print("3- İlişkisel Karşılaştırma Operatörleri") # Boolean veri tipi yani çıktı olarak true false

s1,s2,s3 = 1,2,3

a = """
Operator	Name	                                            Example
==	Equal	                                            x == y	
!=	Not equal	                                            x != y	
>	Greater than	                        x > y	
<	Less than	                                            x < y	
>=	Greater than or equal to	    x >= y	
<=	Less than or equal to	                        x <= y
"""
print(a)

print("4- mantıksal operatörler")# Boolean veri tipi yani çıktı olarak true false
# and / or / not

s1,s2,s3,s4 = 4,9,7,s2

sorgu = s1>s2 or s4 <= s1

print(sorgu)








