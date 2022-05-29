from cajerofunciones import menubasico, consignar
menubasico()
saldo=int(input("Escriba el saldo actual:"))
#EJEMPLO CON while
i=0
while i<3:
    saldo=consignar(saldo)
    i=i+1
#EJEMPLO CON for
for i in range(0,3,1):
    saldo=consignar(saldo)