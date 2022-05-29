def funcionvolumen(alto,ancho,profundidad):
    resultado=alto*ancho*profundidad
    print(f"Con un alto de {alto}, un ancho de {ancho} y una profunidad de {profundidad} tenemos un volumen de {resultado:.2f}")
    return resultado

alto=float(input("Ingrese el alto: "))
ancho=float(input("Ingrese el ancho: "))
profundidad=float(input("Ingrese la profunidad: "))
funcionvolumen(alto,ancho,profundidad)
