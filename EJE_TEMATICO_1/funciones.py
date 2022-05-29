numero1 = float(input("Escriba el numero 1:"))
numero2 = float(input("Escriba el numero 2:"))

def suma(numero1, numero2):
    suma = numero1 + numero2
    print(f"La suma de {numero1} + {numero2} es: {suma}")

def resta(numero1, numero2):
    resta = numero1 - numero2
    print(f"La resta de {numero1} - {numero2} es: {resta}")

def multiplicacion(numero1, numero2):
    multiplicacion = numero1 * numero2
    print(f"La multiplicación de {numero1} * {numero2}  es: {multiplicacion}")

def division(numero1, numero2):
    if numero2 == 0:
        print("No se puede dividir por cero")
    else:
        division = str(numero1 / numero2)
        print(f"La división de {numero1} / {numero2}  es: {division}")

def calculadora():
    suma(numero1, numero2)
    resta(numero1, numero2)
    multiplicacion(numero1, numero2)
    division(numero1, numero2)

calculadora()

