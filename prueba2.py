# Se requiere hacer una función llamada par_impar que reciba como parámetro un número entero. 
# La función debe retornar verdadero si el número es par, y falso de lo contrario.

def par_impar(num):
    if num % 2 == 0:
        return ("True")
    else:
        return ("False")

num = int(input())
par_impar(num)
