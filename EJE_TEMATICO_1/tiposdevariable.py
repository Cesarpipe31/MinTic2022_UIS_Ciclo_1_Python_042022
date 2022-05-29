'''
#VARIABLE INT - ENTERA
x=5
print(type(x))

# VARIABLE FLOAT - FLOTANTE
y=5.5
print(type(y))

# VARIABLE STRING - CADENA DE TEXTO
w="Camilo"
print(type(w))

# VARIABLE BOOLEANA - (VERDADERO O FALSO)
z=True
print(type(z))


a=10
b=20
# MAYOR QUE
print(a>b)
# MAYOR O IGUAL QUE
print(a>=b)
# MENOR QUE
print(a<b)
# MENOR IGUAL QUE
print(a<=b)
# IGUAL QUE
print(a==b)
# DIFERENTE QUE
print(a!=b)
# NEGACION
print(not False)
print(not True)

nombre1="Pedro"
nombre2="Carlos"
print(nombre1==nombre2)

x=True
y=False

# OR
print(x or y)
print(not(x or y))

# AND
print(x and y)
print(not(x and y))
'''

A = True
B = True
C = True

#     A  B  C   B V C     A ^  (B V C)
print(A, B, C, (B or C), (A and (B or C)))
A = True
B = True
C = False
print(A, B, C, (B or C), (A and (B or C)))

