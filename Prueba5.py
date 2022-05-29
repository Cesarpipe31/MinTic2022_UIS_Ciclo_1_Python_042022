# Escriba una función llamada materias que, a partir de una cadena de texto con el siguiente 
# formato: “materia1,materia2,materia3” (Ej: “Inglés,Física,Sociales,Historia,Programación”), 
# separe las materias y las guarde en una lista. La función debe retornar la lista de materias 
# en el orden en el que iban en la cadena de texto. 





# Haga una función llamada listaFrutas que tome como parámetro una lista que contendrá cadenas 
# de texto con nombres de frutas (Ej: [“Manzana”, “Pera”, “Uva”]). La función deberá imprimir 
# en pantalla el nombre de cada fruta dentro de la lista, en el orden en que ahí van.




# Haga una función llamada multiplicarNumeros que tome como parámetro una lista que contendrá 
# números enteros. La función deberá retornar el resultado de la multiplicación de los números 
# en la lista. Ejemplo:
# [2,3,5] -> 2*3*5 = 30


# lista = [1, 2.5, "DevCode", [5,6], 4]


# print (lista [1:6])

# print (lista [1:6:2])

# print(lista[::-1])

# for i in lista:
#     print(i)
# print("-----------------------")
# l = [5, 10, 15, 25]
# n=len(l)
# l.insert(n,30)
# print(l)

# print("XXXXXXXXXXXXXXXXXX")

# conjunto=set([1,2,3,2])
# print(conjunto)

# print("MMMMMMMMMMMMMMMMMMMM")

# x=list(range(16, 0, -2))
# print(x)

# print("ZZZZZZZZZZZZZZZZZ")

# print("XXXXXXXXXXXXXXXXXXXXX")
# my_list=[2, 5, "Cima", 12]
# my_list.extend([10, 20])
# print (my_list)


"""

lista = ("Inglés","Fisica","Sociales","Historia","Programación")

def materias("Inglés","Fisica","Sociales","Historia","Programación"):
    lista_de_materias = []
    for i in range (len(lista)):
        lista_de_materias.append(lista[i])   
    return lista_de_materias
print(materias(lista))

"""

"""
print(lista)
print(len(lista))
"""


"""
lista = ["Manzana", "Pera", "Uva"]

def listaFrutas(lista):
    for i in range (len(lista)):
        print (lista[i])

print(listaFrutas(lista))

"""
 
"""
lista = [2,3,5]
lista1 = [2,2,2]

def multiplicarNumeros(lista):
    resultado = 1
    for i in range(len(lista)):
        resultado = resultado * lista[i]
    return resultado

print (multiplicarNumeros(lista))

print(multiplicarNumeros(lista1))

"""




lista = "Inglés,Fisica,Sociales,Historia,Programación"

def materias(lista):
    lista = lista.split(",")
    return lista

print(lista)

print(materias(lista))


