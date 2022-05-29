def funcionsuma(valor1,valor2):
    resultado=valor1+valor2
    print(f"La suma de {valor1} mas {valor2} es {resultado}")
    return resultado
def funcionresta(valor1,valor2):
    resultado=valor1-valor2
    print(f"La resta de {valor1} menos {valor2} es {resultado}")    
    return resultado
def funcionmultiplicacion(valor1,valor2):
    resultado=valor1*valor2
    print(f"La multiplicacion de {valor1} por {valor2} es {resultado}")
    return resultado  
def funciondivision(valor1,valor2):
    if valor2!=0:
        resultado=valor1/valor2
        print(f"La division de {valor1} entre {valor2} es {resultado}")
    else:
        resultado=0
        print("No se puede dividir por cero")
    return resultado
numero1=float(input("Escriba el numero 1: "))
numero2=float(input("Escriba el numero 2: "))
funcionsuma(numero1,numero2)
funcionresta(numero1,numero2)
funcionmultiplicacion(numero1,numero2)
funciondivision(numero1,numero2)
#resta=funcionresta(numero1,numero2)
#suma=funcionsuma(resta,numero2)
#print(suma)
