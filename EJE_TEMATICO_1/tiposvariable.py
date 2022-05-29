'''
x=5
print(type(x))

y=3.5
print(type(y))

w="MisitonTIC2022"
print(type(w))

z=False
print(type(z))

a=10
b=20

#MAYOR QUE
print(a>b)
#MAYOR O IGUAL QUE
print(a>=b)
#MENOR QUE
print(a<b)
#MENOR O IGUAL QUE
print(a<=b)
#IGUAL QUE
print(a==b)
#DIFERENTE DE
print(a!=b)

#NEGACION
print(not False)
print(not True)

#COMPARACION DE STRINGS
nombre1="Carlos"
nombre2="Pedro"
print(nombre1==nombre2)

x=False
y=False
z=True

#OR - O
print(x or y)
print(not(x or y))

#AND - Y
print(x and y)
print(not(x and y))

#EJERCICIO 1
print((not z) and (x or y))

'''

A=True
B=True
C=True
#     A  B  C  B V C   A ^  (B V C)
print(A, B, C, B or C,  A and (B or C))







