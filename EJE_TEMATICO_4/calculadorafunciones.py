def limpiarpantalla():
    import os
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def sumar(numero1, numero2):
    total=numero1+numero2
    return total

def restar(numero1, numero2):
    total=numero1-numero2
    return total

def multiplicar(numero1, numero2):
    total=numero1*numero2
    return total

def dividir(numero1, numero2):
    total=0
    if numero2!=0:
        total=numero1/numero2
    return total

def main():
    continuar="S"
    while continuar=="S":
        numero1=float(input("Escriba el numero 1: "))
        operador=input("Escriba el operador: ")
        numero2=float(input("Escriba el numero 2: "))    
        if operador=="+":
            print(sumar(numero1,numero2))
        elif operador=="-":
            print(restar(numero1,numero2))
        elif operador=="*":   
            print(multiplicar(numero1,numero2))
        elif operador=="/":
            print(dividir(numero1,numero2))
        else:
            print("Operador desconocido")
        continuar=input("¿Desea continuar? (S/N): ")
        continuar=continuar.upper()
        limpiarpantalla()

main()