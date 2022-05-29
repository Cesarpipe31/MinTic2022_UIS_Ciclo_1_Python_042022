nombresclientes = []
telefonosclientes = []

numeroclientes=int(input("Escriba el numero de clientes a digitar: "))

for clienteactual in (0,numeroclientes,1):
    nomcliente=input("Escriba el nombre del cliente: ")
    nombresclientes.append(nomcliente)
    telcliente=input("Escriba el telefono del cliente: ")
    telefonosclientes.append(telcliente)

print("--------------------------------")
print("*** DIRECTORIO DE CLIENTES ***")
print("--------------------------------")
for clienteactual in (0,numeroclientes,1):
    print(f"Nombre: {nombresclientes[clienteactual]}")
    print(f"Telefono: {telefonosclientes[clienteactual]}")
    print("--------------------------------")    
