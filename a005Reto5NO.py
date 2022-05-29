#/// Manejo Listas

listaproductos1 = ["arroz", "cafe", "harina", "azucar", "sal", "azucar"]

listaproductos2 = list(("gallina","arroz", "cafe", "harina", "azucar", "sal", "azucar"))

print (type(listaproductos1))

print (type(listaproductos2))

listanumeros1 = [1,2,3,4,5,6,7,8,9,10]
listanumeros3 = [22,4,23,1,2,3,4,5,6,7,8,9,10]

print (listanumeros1)

listanumeros2 = list(range(1,11))

print (listanumeros2)

for itemactual in range(0,4):
    print(listanumeros1[itemactual])


for itemactual in range(0,4):
    print(listaproductos1[itemactual])


tamañolistanumeros=len(listanumeros1)
for itemactual in range (0,tamañolistanumeros):
    print(listanumeros1[itemactual])

tamañolistaproductos=len(listaproductos2)
for itemactual in range(0,tamañolistaproductos):
    print(listaproductos2[itemactual])

for itemactual in range (0,len(listaproductos2)):
    print (listaproductos2[itemactual])


for itemactual in range (0,len(listaproductos2)):
    print (listaproductos2[itemactual])
    if listaproductos2[itemactual] == "azucar":
        print ("El Exceso de azúcar provoca problemas de salud")


listanumeros1.append(11)
listanumeros1.append(12)
listanumeros1.append(13)
listanumeros1.append(11)
listanumeros1.append(14)

listanumeros1=list(range(0,len(listanumeros1)))

print (listanumeros1)

#Insertar un elemento en cualquier posición

listanumeros1.insert(5,"César")

print(listanumeros1)

listanumeros1.append(25)
listanumeros1.insert(3,"Rousse")
print(listanumeros1)

listanumeros1.remove(4)
print(listanumeros1)

print(dir(listanumeros1))


listanumeros1[3] = "Rousse, te amo"

print(listanumeros1)

listanumeros3.sort()



listanumeros3.sort(reverse=True)

listanumeros3.sort(reverse=False)



print(listanumeros1[-2])

print(listanumeros1[-7])


nombresclientes = []
telefonosclientes = []

numeroclientes=int(input("Escrib el numero de clientes a digitar: "))

for clientesatual in (0,numeroclientes):
    nomcliente = input("Nombre: ")
    telclientes = input ("Teléfono: ")
    nombresclientes.append(nomcliente)
    telefonosclientes.append(telclientes)

print(nombresclientes)
print(telefonosclientes)