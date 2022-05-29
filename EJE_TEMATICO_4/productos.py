'''
#DEFNIR LISTA FORMA 1
listaproductos=['arroz','cafe','azucar','sal','harina','carne']
print(type(listaproductos))

#DEFINIR LISTA FORMA2
listaproductos=list(('arroz','cafe','azucar','sal','harina','carne'))
print(type(listaproductos))

#CALCULA EL NUMERO DE ELEMENTOS DE LA LISTA
numeroitems=len(listaproductos)
print(f"El numero de elementos de la lista es: {numeroitems}")

#RECORRE LOS ELEMENTOS DE LA LISTA UNO POR UNO
for itemactual in range(0,numeroitems,1):
    print(listaproductos[itemactual])
    if listaproductos[itemactual]=="azucar":
        print("<El exceso de azucar daña tu salud>")

#IMPRIME LOS ELEMENTOS DE LA LISTA
for datos in listaproductos:
    print(datos)

numeros=[1,2,3,4,5,6,7,8,9,10,11,12]
for datos in numeros:
    print(datos)
    
numeros=list(range(1,5))
for datos in numeros:
    print(datos)

print(dir(numeros))
'''
numeros=[1,2,3,4,5,6,7,8,9,10,11,12]

#AGREGAR UN ELEMENTO A LA LISTA
numeros.append(4)
print(numeros)

#INSERTAR UN ELEMENTO EN LA LISTA, EN UNA POSICIÓN ESPECÍFICA
numeros.insert(3,44)
print(numeros)

#BORRAR UN ELEMENTO DE LA LISTA
numeros.remove(3)
print(numeros)

#ORDENAR ASCENDENTEMENTE
numeros.sort(reverse=False)
print(numeros)

#ORDENAR DESCENDENTEMENTE
numeros.sort(reverse=True)
print(numeros)

#SABER SI EXISTE UN ELEMENTO EN LA LISTA
print(numeros.count(4))
