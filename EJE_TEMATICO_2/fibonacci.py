n = int(input("ingrese un numero: "))
for numero in range(0, n):
    cuadrado = 1/2
    fn= ( (((1 + 5**cuadrado) / 2) **numero ) - (((1 - 5**cuadrado) / 2) **numero)) / ( 5**cuadrado )
    print(int(fn))
    