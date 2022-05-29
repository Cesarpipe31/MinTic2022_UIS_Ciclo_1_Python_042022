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
    
def existencias(listacodigos, listaproductos,listaprecios,listacantidades):
    limpiarpantalla()
    print("---------------------------------------")
    print("|             EXISTENCIAS              |")
    print("---------------------------------------")
    for itemactual in range(len(listacodigos)):
        print(f"{listacodigos[itemactual]}. {listaproductos[itemactual]} : {listaprecios[itemactual]} : {listacantidades[itemactual]} unidades")
    return True

def agregarproductos(listacodigos,listaproductos,listaprecios,listacantidades):
    existencias(listacodigos, listaproductos,listaprecios,listacantidades)
    continuar="S"
    while continuar=="S":
        existe=False
        codigonuevoproducto=int(input("Escriba el codigo del nuevo producto: "))
        nombrenuevoproducto=input("Escriba el nombre del nuevo producto: ")
        nombrenuevoproducto=nombrenuevoproducto.lower()    
        precionuevoproducto=int(input("Escriba el precio del nuevo producto: "))
        for itemactual in range(len(listacodigos)):
            if listacodigos[itemactual]==codigonuevoproducto:
                print("¡ ERROR El producto ya existe!")
                existe=True
        if existe==False:
            listacodigos.append(codigonuevoproducto)   
            listaproductos.append(nombrenuevoproducto)
            listaprecios.append(precionuevoproducto)
            listacantidades.append(0)
            ultimaposicion=len(listacodigos)-1
            print(f"{listacodigos[ultimaposicion]}. {listaproductos[ultimaposicion]} : {listaprecios[ultimaposicion]}")
            print("¡ El producto se agregó exitosamente !")        
        continuar=input("¿ Desea continuar agregando productos ? (S/N): ")
        continuar=continuar.upper()
    return listacodigos,listaproductos,listaprecios,listacantidades

def actualizarproductos(listacodigos,listaproductos,listaprecios,listacantidades):
    existencias(listacodigos, listaproductos,listaprecios,listacantidades)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto a actualizar: "))
    for itemactual in range(len(listacodigos)):
        if listacodigos[itemactual]==codigoproductoactualizar:
            existe=True
            nombreproductoactualizar=input(f"Nombre actual: {listaproductos[itemactual]} - Escriba el nuevo nombre del producto: ")
            nombreproductoactualizar=nombreproductoactualizar.lower()    
            precioproductoactualizar=int(input(f"Precio actual: {listaprecios[itemactual]} Escriba el nuevo precio del producto: "))
            listaproductos[itemactual]=nombreproductoactualizar
            listaprecios[itemactual]=precioproductoactualizar
            print("¡ El producto se actualizó exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return listacodigos,listaproductos,listaprecios,listacantidades

def borrarproductos(listacodigos,listaproductos,listaprecios,listacantidades):
    existencias(listacodigos, listaproductos,listaprecios,listacantidades)
    existe=False
    codigoproductoborrar=int(input("Escriba el codigo del producto a borrar: "))
    itemactual=0
    while itemactual<len(listacodigos):
        if listacodigos[itemactual]==codigoproductoborrar:
            existe=True
            confirmacion=input("¿Esta seguro de borrar el producto? (S/N): ")
            confirmacion=confirmacion.upper()
            if confirmacion=="S":
                listacodigos.pop(itemactual)
                listaproductos.pop(itemactual)
                listaprecios.pop(itemactual)
                listacantidades.pop(itemactual)                
                print("¡ El producto se borró exitosamente !")
        else:
            itemactual=itemactual+1
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return listacodigos,listaproductos,listaprecios,listacantidades

def entradas(listacodigos,listaproductos,listaprecios,listacantidades):
    existencias(listacodigos, listaproductos,listaprecios,listacantidades)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto: "))
    for itemactual in range(len(listacodigos)):
        if listacodigos[itemactual]==codigoproductoactualizar:
            existe=True
            cantidadentrada=int(input(f"Cantidad actual: {listacantidades[itemactual]} - Escriba la cantidad de Entrada: "))
            listacantidades[itemactual]=listacantidades[itemactual]+cantidadentrada
            print("¡ El proceso se ejecuto exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return listacodigos,listaproductos,listaprecios,listacantidades

def salidas(listacodigos,listaproductos,listaprecios,listacantidades):
    existencias(listacodigos, listaproductos,listaprecios,listacantidades)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto: "))
    for itemactual in range(len(listacodigos)):
        if listacodigos[itemactual]==codigoproductoactualizar:
            existe=True
            cantidadsalida=int(input(f"Cantidad actual: {listacantidades[itemactual]} - Escriba la cantidad de Entrada: "))
            if cantidadsalida<=listacantidades[itemactual]:
                listacantidades[itemactual]=listacantidades[itemactual]-cantidadsalida
            else:
                print("¡ No hay suficientes existencias !")
            print("¡ El proceso se ejecuto exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return listacodigos,listaproductos,listaprecios,listacantidades

def bajas(listacodigos,listaproductos,listaprecios,listacantidades):
    existencias(listacodigos, listaproductos,listaprecios,listacantidades)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto: "))
    for itemactual in range(len(listacodigos)):
        if listacodigos[itemactual]==codigoproductoactualizar:
            existe=True
            cantidadbaja=int(input(f"Cantidad actual: {listacantidades[itemactual]} - Escriba la cantidad de Entrada: "))
            if cantidadbaja<=listacantidades[itemactual]:
                listacantidades[itemactual]=listacantidades[itemactual]-cantidadbaja
            else:
                print("¡ No hay suficientes existencias !")
            print("¡ El proceso se ejecuto exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return listacodigos,listaproductos,listaprecios,listacantidades