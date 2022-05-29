agenda = {
    '9':{'nombre':'Juan','telefonos':[3156367367,3205426633],'correo':'juan@uis.edu.co','direccion':'Calle 9 Cra 27','ciudad':'Bucaramanga'},
    '2':{'nombre':'Pedro','telefonos':[3206367367,3115426633],'correo':'pedro@uis.edu.co','direccion':'Calle 8 Cra 21','ciudad':'Bogota'},
    '7':{'nombre':'Jose','telefonos':[3226367367,3105426633],'correo':'jose@uis.edu.co','direccion':'Calle 7 Cra 22','ciudad':'Cali'},
    '8':{'nombre':'Maria','telefonos':[3506367367,3015426633],'correo':'maria@uis.edu.co','direccion':'Calle 2 Cra 17','ciudad':'Medellín'},
    '4':{'nombre':'Lucia','telefonos':[3176367367,3155426633],'correo':'lucia@uis.edu.co','direccion':'Calle 12 Cra 19','ciudad':'Barranquilla'}
    }

# Conocer el numero de items del diccionario
print(f"El diccionario tiene {len(agenda)} elementos")
# Recorrer las claves del diccionario
for claves in agenda.keys():
    print(claves)
# Recorrer los valores del diccionario
for valores in agenda.values():
    print(valores)
# Recorrer las claves y los valores del diccionario simultaneamente
for claves,valores in agenda.items():
    print(claves,valores)
# Ubicar un valor en el diccionario
print(agenda['8']['correo'])
#Por ejemplo acceder a los telefonos de Jacinta
for telefonos in agenda["8"]["telefonos"]:
    print (f"{telefonos}")
# Actualizar un elemento
agenda['8']['correo']="jacinta2@uis.edu.co"
# Recorrer toda una columna del diccionario
for clave in agenda.keys():
    print(agenda[clave]['nombre'])
# Recorrer toda una columna del diccionario con el metodo get
for clave in agenda.keys():
    print(agenda[clave].get("nombre","No se encuentro ningun registro"))
#Usar el metodo items() para recorrer de forma simultanea claves(keys) y valores(values)
for clave,valor in agenda["2"].items():
    print(f"La clave es: {clave} y el valor es: {valor}")
# Recorrer toda la grilla por filas y columnas
for fila in agenda.keys():
    for columna in agenda[fila].keys():
        print(agenda[fila][columna])




'''
# Metodo ZIP para trabajo con diccionarios
contactos = zip(agenda.keys(), agenda.values())
print(type(contactos))
contactos = list(contactos)
print(contactos)

productos = zip(inventario["8"].keys(), inventario["8"].values()) 
print(type(productos))
productos = list(productos)
print(productos) 
'''






