arroz=1000
aceite=560
azucar=300
cafe=1200
sal=450
harina=300
panela=500
factura="-------------------\n| FACTURA DE VENTA |\n--------------------\n"
print("-----------------------")
print("BIENVENIDOS A SU TIENDA")
print("-----------------------")
print("seleccione el producto que desee")
print("1.arroz")
print("2.aceite")
print("3.azucar")
print("4.cafe")
print("5.sal")
print("6.harina")
print("7.panela")
print("8.salir")
opcion =int(input("introduzca el producto que desee: "))
while opcion<8:
    cantidad=int(input("indique la cantidad que desea: "))
    if opcion==1:
        if cantidad<=arroz:
            valor_arroz=2000
            valor_compra_arroz=cantidad*valor_arroz
            factura=factura + "su compra es de "+ str(cantidad) + "libras de arroz por valor de " + str(valor_compra_arroz) + "\n"
            arroz=arroz-cantidad
        else:
            saldo_arroz=arroz
            print(f"en el momento contamos con: {saldo_arroz}") 
    elif opcion==2:
        if cantidad<=aceite:
            valor_aceite=4500
            valor_compra_aceite=cantidad*valor_aceite
            factura=factura + "su compra es de " + str(cantidad) + "libras de arroz por valor de " + str(valor_compra_aceite) + "\n"
            aceite=aceite-cantidad
        else:
            saldo_aceite=aceite
            print(f"en el momento contamos con: {saldo_aceite}")  
    elif opcion==3:
        if cantidad<=azucar:
            valor_azucar=2500
            valor_compra_azucar=cantidad*valor_azucar
            factura=factura + "su compra es de " + str(cantidad) + "libras de arroz por valor de " + str(valor_compra_azucar) + "\n"

            azucar=azucar-cantidad
        else:
            saldo_azucar=azucar
            print(f"en el momento contamos con: {saldo_azucar}")  
    elif opcion==4:
        if cantidad<=cafe:
            valor_cafe=7550
            valor_compra_cafe=cantidad*valor_cafe
            factura=factura + "su compra es de " + str(cantidad) + "libras de arroz por valor de " + str(valor_compra_cafe) + "\n"
            cafe=cafe-cantidad
        else:
            saldo_cafe=cafe
            print(f"en el momento contamos con: {saldo_cafe}") 
    elif opcion==5:
        if cantidad<=sal:
            valor_sal=1100
            valor_compra_sal=cantidad*valor_sal
            factura=factura + "su compra es de " + str(cantidad) + "libras de arroz por valor de " + str(valor_compra_sal) + "\n"
            sal=sal-cantidad
        else:
            saldo_sal=sal
            print(f"en el momento contamos con: {saldo_sal}") 
    elif opcion==6:
        if cantidad<=harina:
            valor_harina=1500
            valor_compra_harina=cantidad*valor_harina
            factura=factura + "su compra es de " + str(cantidad) + "libras de arroz por valor de " + str(valor_compra_harina) + "\n"
            harina=harina-cantidad
        else:
            saldo_harina=harina
            print(f"en el momento contamos con: {saldo_harina}")  
    elif opcion==7:
        if cantidad<=panela:
            valor_panela=4000
            valor_compra_panela=cantidad*valor_panela
            print(f"su compra es de {cantidad} cuadros de panela por valor de {valor_compra_panela}")
            panela=panela-cantidad
        else:
            saldo_panela=panela
            print(f"en el momento contamos con: {saldo_panela}") 
    opcion = int(input("seleccione otro producto: "))
print("gracias por su compra")
print(factura)

