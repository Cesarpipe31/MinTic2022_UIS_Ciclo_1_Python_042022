saldocliente=1000000
clavecliente="12345"
tarjetacliente="1001434315"
print("-----------------------------------")
print("| BIENVENIDO AL CAJERO AUTOMATICO |")
print("-----------------------------------")
tarjetausuario=input("Por favor introduzca su tarjeta: ")
if tarjetausuario==tarjetacliente:
    claveusuario=input("Por favor introduzca su clave: ")
    if claveusuario==clavecliente:
        print("Seleccione una opcion:")
        print("(1) Consultar Saldo")
        print("(2) Retirar Dinero")       
        print("(3) Consignar")
        print("(4) Salir")
        opcion=int(input("Seleccione una opcion:"))
        if opcion==1:
            print(f"Su saldo actual es: {saldocliente}")
        elif opcion==2:
            valorretiro=int(input("Escriba el valor a retirar:"))
            if valorretiro<=saldocliente:
                saldocliente=saldocliente-valorretiro
                print(f"Su nuevo saldo es: {saldocliente}")
            else: print("Fondos insufiencientes, Gracias por utilizar nuestros servicios!")
        elif opcion==3:
             valorconsignar=int(input("Escriba el valor a consignar:"))
             saldocliente=saldocliente+valorconsignar
             print(f"Su nuevo saldo es: {saldocliente}")
        else: print("Gracias por utilizar nuestros servicios!")           
    else: print("La clave es incorrecta!, Gracias por utilizar nuestros servicios!")             
else: print("La tarjeta introducida no es valida, Gracias por utilizar nuestros servicios!")







