inventario={
            0:{'nombre':'Arroz', 'valor':300},
            1:{'nombre':'Cafe', 'valor':400}
            }

#ACTUALIAZAR ITEM
inventario[0]['nombre']="Aceite"

#AGREGAR ITEM
inventario[2]={"nombre":"Azucar", "valor":250}
inventario[3]={"nombre":"Sal", "valor":1000}
inventario[4]={"nombre":"Harina", "valor":600}

#NUMERO DE REGISTROS
numregistros=len(inventario)
print(f"Numero de registros: {numregistros}")
#RECORRER DATOS
for i in range(0,numregistros):
    print(f"{inventario[i]['nombre']} {inventario[i]['valor']}")

#BORRAR DATOS
del(inventario[2])

def agregaritem(var_nombre,var_valor):
    print(f"Esta es la funcion agregaritem {var_nombre} : {var_valor}")

agregaritem("Chocolate", 650)

#NUMERO DE REGISTROS
numregistros=len(inventario)
print(f"Numero de registros: {numregistros}")

'''
#BORRAR DATOS
for i in range(0,numregistros):
    nom=inventario[i]['nombre']
    val=inventario[i]['valor']
    print(f"{nom} {val}")
    '''