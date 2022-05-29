numeroPaquetes = int(input())
costoTotal = 0
for i in range(1,numeroPaquetes+1,1):
    alto=float(input())
    ancho=float(input())
    profundo=float(input())
    volumen=alto*ancho*profundo
    costo=volumen*5
    if (alto>30): costo = costo + 2000
    if (costo>10000): costo = costo * (1.19)
    print(volumen)
    print(costo)
    costoTotal = costo+costoTotal
print(costoTotal)

# numeroPaquetes = int(input())
# costoTotal = 0
# for i in range(1,numeroPaquetes+1,1):
#     alto=float(input())
#     ancho=float(input())
#     profundo=float(input())
#     volumen=alto*ancho*profundo
#     costo=volumen*5
#     if (alto>30): costo = costo + 2000
#     if (costo>10000): costo = costo * (1.19)
#     volumen
#     costo
#     costoTotal = costo+costoTotal
# costoTotal
