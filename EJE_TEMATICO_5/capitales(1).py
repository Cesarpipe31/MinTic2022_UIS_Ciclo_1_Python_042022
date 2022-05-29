'''
diccionario = {"Colombia":["Bogota","Cali","Medellín","Barranquilla","Bucaramanga"],"Perú":"Lima","Ecuador":"Quito","Venezuela":"Caracas"}
print(diccionario["Colombia"])
print(diccionario["Perú"])

for clave in diccionario.keys():
    print(clave)

for valor in diccionario.values():
    print(valor)
    
for clave,valor in diccionario.items():
    print(clave, "-" ,valor)
'''

diccionario = {
                "Colombia":{"Capital 1":"Bucaramanga","Capital 2":"Medellín","Capital 3":"Ibagué"},
                "Perú":{"Capital 1":"San Martin","Capital 2":"Huanuco","Capital 3":"La Libertad"},
                "Ecuador":{"Capital 1":"Galápagos","Capital 2":"Guayaquil","Capital 3":"Napo"},
                "Venezuela":{"Capital 1":"Puerto Ayacucho","Capital 2":"San Cristobal","Capital 3":"Maracaibo"}
            }

#for clave in diccionario.keys():
#    print(diccionario[clave]["Capital 1"])

for fila in diccionario.keys():
    for columna in diccionario[fila].keys():
        print(diccionario[fila][columna])