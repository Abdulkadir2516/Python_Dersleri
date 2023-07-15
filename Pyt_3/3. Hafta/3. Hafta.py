"""
operatörler
"""

# aritmatiksel / matematiksel operatörler
# atama operatörleri
# ilişkisel operand
# mantıksal operand
# bellek operand
# bitsel operand

print("Aritmetiksel Operatörler" )

a = """
Operator	Name	                    Example
+	Addition	                    x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	                    x / y	
%	Modulus	                    x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""
print(a)

print("Atama operatörleri")

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


print("İlişkisel operatörleri") # sadece True False değer döndürürler

a = """
Operator	Name	                                            Example	
==	Equal	                                            x == y	
!=	Not equal	                                            x != y	
>	Greater than                                         x > y	
<	Less than	                                            x < y	
>=	Greater than or equal to                    x >= y	
<=	Less than or equal to	                        x <= y
"""
print(a)

print("Mantıksal operatörler") # sadece True False değer döndürürler

a="""
Operator	Description	                                                            Example
and 	Returns True if both statements are true	                    x < 5 and  x < 10	
or	Returns True if one of the statements is true	                    x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""
print(a)


ortalama = 50
final = 45

print("Geçme Durumu : ", ortalama > 45 or ortalama == 45 and final > 50 )

print("Geçme Durumu : ", ortalama >= 45 and final > 50 )

print("Geçme Durumu : ", (ortalama > 45 or ortalama == 45) and final > 50 )


print("Bitsel operatörler") 
a="""

Operator	Name	Description	Example	Try it
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

"""

print(a)

print(22&25)
