def despedida():
    print("Hasta pronto!")
def existencias(arroz,cafe,azucar,sal,harina):
    print("--------------")
    print("| EXISTENCIAS |")
    print("--------------")
    print(f"Arroz: {arroz}")
    print(f"Cafe: {cafe}")   
    print(f"Azucar: {azucar}")       
    print(f"Sal: {sal}")       
    print(f"Harina: {harina}") 
    return True

def menutipomovimiento():
    print("---------------------------------------")
    print("| BIENVENIDO AL SISTEMA DE INVENTARIO |")
    print("---------------------------------------")
    print("*** Movimientos de inventario ***")
    print("E. ENTRADA")
    print("S. SALIDA")
    print("B. BAJA")
    print("X. SALIR")
    movimiento=input("Seleccione un movimiento de inventario: ")
    movimiento=movimiento.upper()
    return movimiento

def menuproducto():
    print("*** Listado de productos ***")
    print("1. Arroz")
    print("2. Cafe")
    print("3. Azucar")
    print("4. Sal")
    print("5. Harina")
    producto=input("Seleccione un producto: ")
    return producto

def procesos(movimiento,cantidad,saldoproducto):
    if movimiento=="E":
        saldoproducto=saldoproducto+cantidad 
    if movimiento=="S" or movimiento=="B":
        if cantidad<=saldoproducto:
            saldoproducto=saldoproducto-cantidad
        else:
            print("No hay existencias suficientes de este producto")
    return saldoproducto
