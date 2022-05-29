arroz=300
cafe=400
azucar=250
sal=1000
harina=600

#print("Listado de productos\n1. Arroz\n2. Cafe\n3. Azucar\n4. Sal\n5. Harina\n6. Salir") 
print("---------------------------------------")
print("| BIENVENIDO AL SISTEMA DE INVENTARIO |")
print("---------------------------------------")
print("*** Movimientos de inventario ***")
print("E. ENTRADA")
print("S. SALIDA")
print("B. BAJA")
print("X. Salir")
movimiento=input("Seleccione un movimiento de inventario: ")
if movimiento=="X":
    print("Hasta pronto!")
else:
    cantidad=int(input("Escriba la cantidad de productos: "))
    print("*** Listado de productos ***")
    print("1. Arroz")
    print("2. Cafe")
    print("3. Azucar")
    print("4. Sal")
    print("5. Harina")
    print("6. Salir")
    producto=input("Seleccione un producto: ")
    if producto=="6":
        print("Hasta pronto!")
    else:
        if producto=="1":
            
            if movimiento=="E":
                arroz=arroz+cantidad 
            
            if movimiento=="S" or movimiento=="B":
                if cantidad<=arroz:
                    arroz=arroz-cantidad
                else:
                    print("No hay existencias suficientes del producto")
            
    
    print("INVENTARIO")
    print(f"Arroz: {arroz}")



