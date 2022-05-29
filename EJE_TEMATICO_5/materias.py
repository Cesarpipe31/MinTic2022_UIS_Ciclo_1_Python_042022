lista = ["Inglés","Física", "Sociales", "Historia", "Programación"]
def materias(lista):
    lista_de_materias = []
    for i in range(len(lista)):
        lista_de_materias.append(lista[i])
    return lista_de_materias
print(materias(lista))
