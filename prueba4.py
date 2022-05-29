#peso < 2 Kg 
#volumen < 0.027 m^3

def procesar_dato (peso,volumen):
    if (peso < 2 and volumen < 0.027):
        return ("True")
    else:
        return ("False")

peso=float(input())
volumen=float(input())

procesar_dato(peso, volumen)






