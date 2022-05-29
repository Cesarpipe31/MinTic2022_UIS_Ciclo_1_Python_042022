'''
diccionarioproductos=dict([('nombre','arroz'),('valor','300'),('nombre','café'),('valor','400'),('nombre','harina'),('valor','250'),('nombre','azucar'),('valor','1000'),('nombre','sal'),('valor','600')])
print(diccionarioproductos)
print(diccionarioproductos['nombre'])
for itemactual in diccionarioproductos:
    print(f"Item {itemactual}: {diccionarioproductos[itemactual]}")
'''


inventario=dict([('nombre', 'Arroz'),('valor', 300),('nombre', 'Cafe'),('valor', 400)])

print(inventario)

print(inventario['nombre'])

print(inventario.get('nombre'))
print(inventario.get('valor'))

inventario['nombre']="Pastas"
print(inventario['nombre'])
print(inventario)

for i in inventario:
    print(f"{i}: {inventario[i]}")


print(inventario['nombre'])
print(inventario['valor'])
print(inventario['proveedores'])
print(inventario['proveedores'][0])
print(inventario['proveedores'][1])
print(inventario['proveedores'][2])

for columnas in inventario:
    print(f"{columnas} {inventario[columnas]}")
    nom_producto = inventario.get('nombre')
    valor_producto = inventario.get('valor')
    print(f"El valor del {nom_producto} es: {valor_producto}")
    if columnas=="proveedores":
        #numeroitems=inventario[columnas].count()
        for i in range(0,3):
            print(f"{inventario[columnas][i]}")
