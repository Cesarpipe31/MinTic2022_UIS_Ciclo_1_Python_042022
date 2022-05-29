factura="********************\n| FACTURA DE VENTA |\n********************\n"

contador=1
while contador<=3:
    #print(f"Este es el ciclo numero: {contador}")
    factura=factura+"Producto "+str(contador)+"\n"
    contador=contador+1

factura=factura+"********************\n"
print(factura)

