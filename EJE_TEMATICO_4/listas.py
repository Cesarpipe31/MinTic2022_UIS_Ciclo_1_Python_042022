#SERIES DE DATOS
lista = [1, 2, 3, 8, 9]
print(lista)
print(type(lista))

tupla = (1, 4, 8, 0, 5)
print(tupla)
print(type(tupla))

conjunto = set([1, 3, 1, 4])
print(conjunto)
print(type(conjunto))

diccionario = {'a': 1, 'b': 3, 'z': 8}
print(diccionario)
print(type(diccionario))

# MANEJO DELISTAS

#DEFNIR LIST FORMA 1
listaproductos=['arroz','cafe','azucar','sal','harina','carne']
print(type(listaproductos))

#DEFINIR LISTA FORMA2
listaproductos=list(('arroz','cafe','azucar','sal','harina','carne'))
print(type(listaproductos))

#CALCULA EL NUAMERO DE ELEMENTOS DE LA LISTA
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

# DEFINICION DE UNA LISTA
colores = ['verde', 'amarillo', 'rojo', 'azul']
print(colores)

# ASIGNAR UNA LISTA
numeros = list((0,1,2,3,4,5,6,7,8,9))
print(numeros)

# DEFINIR LISTA POR RANGO
numeros = list(range(0,10))
print(numeros)

# TAMAÑO DE LA LISTA
print(len(numeros))

# DIRECTORIO DE OPCIONES PARA LA LISTA
print(dir(numeros))

# ADICIONAR ELEMENTO AL FINAL
numeros.append(10)
print(numeros)

# ADICIONAR VARIOS ELEMENTOS AL FINAL
numeros.extend([5,25])
print(numeros)

# INSERTAR UN ELEMENTO EN UNA POSICION ESPECIFICA
numeros.insert(4,99)
print(numeros)

# BORRAR UN ELEMENTO
numeros.remove(5)
print(numeros)

# REVISAR SI EXISTE UN ELEMENTO EN LA LISTA
print(numeros.count(5))

# ORDENAR
numeros.sort()
print(numeros)

# ORDENAR DESCENDENTEMENTE
numeros.sort(reverse=True)
print(numeros)

# ORDENAR DESCENDENTEMENTE
numeros.sort(reverse=False)
print(numeros)

# INDEXACION DE LISTAS
print(numeros[0])
print(numeros[-1])
print(numeros[-3:])

# REEMPLAZAR UN ELEMENTO
numeros[7:7] = [66]
print(numeros)

#REEMPLAZAR VARIOS ELEMENTOS DE LA LISTA
numeros[2:5] = [56,24,63]
print(numeros)

#EJERCICIOS

dia = 0    
semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
while dia < 7:
   print("Hoy es " + semana[dia])
   dia += 1
   
#ALMACENAMIENTO DE LISTAS

# Creamos las listas (vacías al comienzo)
nombres = []
identificaciones = []

# Definimos un tamaño para las listas
# Lo puedes cambiar si quieres
tamaño = 3

# Leemos los datos y los agregamos a la lista
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")

    nombres.append(nombre)
    identificaciones.append(identificación)

# Ahora mostremos las listas
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)

    print("Nombre:", nombres[i])
    print("Identificación:", identificaciones[i])



# ALMACENAMIENTO DE VARIABLES DE TEXTO Y BUSQUEDA DE COINCIDENCIAS
def nombres():
    
    '''Pide al usuario que ingrese el primer nombre de un estudiante en clase
    hasta que se ingrese una string vacía. Luego la función imprime el número 
    de estudiantes con cada nombre que se ingresó.
    '''
    nombre = ''
    nombres = []
    nombre = input('Enter next nombre: ')
    while nombre != '':  # Mientras que nombre no sea una string vacia
        nombres.append(nombre)
        nombre = input('Enter next nombre: ')
    
    # Creamos un diccionario con la estructura nombre:ocurrencias
    ocurrencias_nombre = {n:nombres.count(n) for n in nombres}
    
    # Iteramos a traves de las claves del diccionario
    for k in ocurrencias_nombre.keys(): 
        singular = True if ocurrencias_nombre[k] < 2 else False
        if singular:
            print('Hay {} estudiante llamado {}'.format(ocurrencias_nombre[k], k))
        else:
            print('Hay {} estudiantes llamados {}'.format(ocurrencias_nombre[k], k))
nombres()


# ENCONTRAR UN ELEMENTO DE LA LISTA Y REEMPLAZARLO
my_list=[5,10,7,5,6,8,5,15]
for index, value in enumerate(my_list):
    if value == 5:
        my_list[index] = 9
print(my_list)

# ENCONTRAR UN ELEMENTO DE LA LISTA Y REEMPLAZARLO CON EL METODO DE COMPRESION
my_list=[5,10,7,5,6,8,5,15]
[9 if value==5 else value for value in my_list]
print(my_list)

# ENCONTRAR UN ELEMENTO DE LA LISTA Y REEMPLAZARLO CON EL METODO MAP
list_1=[5,10,7]
list_2=[7,10,7,5,7,5,10]
ent = {k: i for i, k in enumerate(list_1)} 
result = list(map(ent.get, list_2))
print("list2 after replacement is:", result)
