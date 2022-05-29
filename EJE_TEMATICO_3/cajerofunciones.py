def error():
    print("¡ERROR! Esa opcion no está disponible")   
def despedida():
    print("------------------------------------------")
    print("| GRACIAS POR UTILIZAR NUESTROS SERVICIOS |")
    print("------------------------------------------")
def encabezado():
    print("-----------------------------------")
    print("| BIENVENIDO AL CAJERO AUTOMATICO |")
    print("-----------------------------------")
def menu():
    print("Seleccione una opcion:")
    print("(1) Consultar Saldo")
    print("(2) Retirar Dinero")       
    print("(3) Consignar")
    print("(4) Salir")
    opcion=input("Seleccione una opcion:")
    return opcion
def menubasico():
    print("Seleccione una opcion:")
    print("(1) Consultar Saldo")
    print("(2) Consignar")
    print("(3) Salir")
    opcion=input("Seleccione una opcion:")
    return opcion
def accesoerrado(intentosfallidos):
    oportunidades=3-intentosfallidos
    print(f"Acceso errado, intentos restantes: {oportunidades}")
    if intentosfallidos==3:
        print("LADRON! LADRON! LADRON! LADRON! LADRON!")
def validartarjeta(tarjeta):
    tarjetausuario=input("Por favor introduzca su tarjeta: ")
    if tarjetausuario==tarjeta:
        return True
def validarclave(clave):
    claveusuario=input("Por favor introduzca su clave: ")
    if claveusuario==clave:
        return True
def consultarsaldo(saldo):
    print(f"Su saldo actual es: {saldo}")
def retirar(saldo):
    valorretiro=int(input("Escriba el valor a retirar:"))
    if valorretiro<=saldo:
        saldo=saldo-valorretiro
        print(f"Su nuevo saldo es: {saldo}")
    else:
        print("Fondos insufiencientes!")
    return saldo    
def consignar(saldo):
    valorconsignar=int(input("Escriba el valor a consignar:"))
    saldo=saldo+valorconsignar
    print(f"Su nuevo saldo es: {saldo}")
    return saldo 