#BIBLIOTECA DE FUNCIONES DEL CAJERO
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
def despedida():
    print("------------------------------------------")
    print("| GRACIAS POR UTILIZAR NUESTROS SERVICIOS |")
    print("------------------------------------------")
def validartarjeta(tarjetacliente):
    tarjetausuario=input("Por favor introduzca su tarjeta: ")
    if tarjetausuario==tarjetacliente:
        return True
    else:
        print("Tarjeta no valida")
        return False
def validarclave(clavecliente):
    claveusuario=input("Por favor introduzca su clave: ")
    if claveusuario==clavecliente:
        return True
    else:
        print("Clave no valida")
        return False    
def consultarsaldo(saldocliente):
    print(f"Su saldo actual es: {saldocliente}")
def retirar(saldocliente):
    valorretiro=int(input("Escriba el valor a retirar:"))
    if valorretiro<=saldocliente:
        saldocliente=saldocliente-valorretiro
        print(f"Su nuevo saldo es: {saldocliente}")
    else:
        print("Fondos insufiencientes, Gracias por utilizar nuestros servicios!")    
def consignar(saldocliente):
    valorconsignar=int(input("Escriba el valor a consignar:"))
    saldocliente=saldocliente+valorconsignar
    print(f"Su nuevo saldo es: {saldocliente}")