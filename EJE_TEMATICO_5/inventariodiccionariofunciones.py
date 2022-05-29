def limpiarpantalla():
    import os
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def despedida():
    limpiarpantalla()
    print("---------------------------------------")
    print("|       ¡¡¡  HASTA PRONTO  !!!         |")
    print("---------------------------------------")

def menutipomovimiento():
    limpiarpantalla()
    print("---------------------------------------")
    print("| BIENVENIDO AL SISTEMA DE INVENTARIO |")
    print("---------------------------------------")
    print("*** Movimientos de inventario ***")
    print("E. ENTRADA")
    print("S. SALIDA")
    print("B. BAJA")
    print("I. INFORME EXISTENCIAS")
    print("P. GESTION DE PRODUCTOS >>")      
    print("X. SALIR")
    movimiento=input("Seleccione un movimiento de inventario: ")
    movimiento=movimiento.upper()
    return movimiento

def menugestionproductos():
    limpiarpantalla()
    print("---------------------------------------")
    print("|        GESTION DE PRODUCTOS          |")
    print("---------------------------------------")    
    print("1. Agregar un nuevo producto")
    print("2. Actualizar un producto")
    print("3. Borrar un producto")
    print("4. Listar productos")    
    print("5. << Regresar")     
    opcionmenugestion=int(input("Seleccione una opcion: "))
    return opcionmenugestion
    
def existencias(inventario):
    limpiarpantalla()
    print("---------------------------------------")
    print("|             EXISTENCIAS              |")
    print("---------------------------------------")
    for itemactual in inventario.keys():
        print(f"{inventario[itemactual]['codigo']} : {inventario[itemactual]['nombre']} : {inventario[itemactual]['precio']} : {inventario[itemactual]['cantidad']} unidades")
    return True

def agregarproductos(inventario):
    existencias(inventario)
    continuar="S"
    while continuar=="S":
        existe=False
        codigonuevoproducto=int(input("Escriba el codigo del nuevo producto: "))
        nombrenuevoproducto=input("Escriba el nombre del nuevo producto: ")
        nombrenuevoproducto=nombrenuevoproducto.lower()    
        precionuevoproducto=int(input("Escriba el precio del nuevo producto: "))
        for itemactual in inventario.keys():
            if inventario[itemactual]["codigo"]==codigonuevoproducto:
                print("¡ ERROR El producto ya existe!")
                existe=True
        if existe==False:
            tamañodiccionario=len(inventario)
            inventario[tamañodiccionario]["codigo"] = codigonuevoproducto
            inventario[tamañodiccionario]["nombre"] = nombrenuevoproducto
            inventario[tamañodiccionario]["precio"] = precionuevoproducto
            print(f"{inventario[tamañodiccionario]['codigo']} : {inventario[tamañodiccionario]['nombre']} : {inventario[tamañodiccionario]['precio']} : {inventario[tamañodiccionario]['cantidad']} unidades")
            print("¡ El producto se agregó exitosamente !")        
        continuar=input("¿ Desea continuar agregando productos ? (S/N): ")
        continuar=continuar.upper()
    return inventario

def actualizarproductos(inventario):
    existencias(inventario)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto a actualizar: "))
    for itemactual in inventario.items():
        if itemactual[0]==codigoproductoactualizar:
            existe=True
            nombreproductoactualizar=input(f"Nombre actual: {itemactual[1]} - Escriba el nuevo nombre del producto: ")
            nombreproductoactualizar=nombreproductoactualizar.lower()    
            precioproductoactualizar=int(input(f"Precio actual: {itemactual[2]} Escriba el nuevo precio del producto: "))
            #####################
            indice=3
            inventario[indice] = {'codigo':codigoproductoactualizar,'nombre':nombreproductoactualizar,'precio':precioproductoactualizar}
            #####################            
            print("¡ El producto se actualizó exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return inventario

def borrarproductos(inventario):
    existencias(inventario)
    existe=False
    codigoproductoborrar=int(input("Escriba el codigo del producto a borrar: "))
    itemactual=0
    while itemactual<len(inventario):
        if itemactual[0]==codigoproductoborrar:
            existe=True
            confirmacion=input("¿Esta seguro de borrar el producto? (S/N): ")
            confirmacion=confirmacion.upper()
            if confirmacion=="S":
                indice=3
                del(inventario[indice])               
                print("¡ El producto se borró exitosamente !")
        else:
            itemactual=itemactual+1
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return inventario

def entradas(inventario):
    existencias(inventario)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto: "))
    for itemactual in range(len(inventario)):
        if itemactual[0]==codigoproductoactualizar:
            existe=True
            cantidadentrada=int(input(f"Cantidad actual: {itemactual[3]} - Escriba la cantidad de Entrada: "))
            itemactual[3]=itemactual[3]+cantidadentrada
            print("¡ El proceso se ejecuto exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return inventario

def salidas(inventario):
    existencias(inventario)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto: "))
    for itemactual in range(len(inventario)):
        if itemactual[0]==codigoproductoactualizar:
            existe=True
            cantidadsalida=int(input(f"Cantidad actual: {itemactual[3]} - Escriba la cantidad de Salida: "))
            if cantidadsalida<=itemactual[3]:
                itemactual[3]=itemactual[3]-cantidadsalida
            else:
                print("¡ No hay suficientes existencias !")
            print("¡ El proceso se ejecuto exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return inventario

def bajas(inventario):
    existencias(inventario)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto: "))
    for itemactual in range(len(inventario)):
        if itemactual[0]==codigoproductoactualizar:
            existe=True
            cantidadsalida=int(input(f"Cantidad actual: {itemactual[3]} - Escriba la cantidad a dar de bja: "))
            if cantidadsalida<=itemactual[3]:
                itemactual[3]=itemactual[3]-cantidadsalida
            else:
                print("¡ No hay suficientes existencias !")
            print("¡ El proceso se ejecuto exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return inventario