def validartarjeta(tarjetas):
    tarjetausuario=input("Por favor introduzca su tarjeta: ")
    if tarjetausuario in tarjetas:
        return True
    else:
        return False
tarjetas=['1052673675','1052425624','10267137809']
print(validartarjeta(tarjetas))