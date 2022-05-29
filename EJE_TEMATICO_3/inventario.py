from inventariofunciones import despedida, existencias, menutipomovimiento, menuproducto, procesos

arroz=300
cafe=400
azucar=250
sal=1000
harina=600
movimiento=""

existencias(arroz,cafe,azucar,sal,harina)

while movimiento!="X":

    movimiento=menutipomovimiento()
    
    if movimiento=="X":
        despedida()
    else:
        cantidad=int(input("Escriba la cantidad de productos: "))
        if cantidad>=0:

            producto=menuproducto()
            
            if producto=="6":
                despedida()
            else:
                
                if producto=="1":
                    arroz=procesos(movimiento,cantidad,arroz)
                if producto=="2":
                    cafe=procesos(movimiento,cantidad,cafe)                
                if producto=="3":
                    azucar=procesos(movimiento,cantidad,azucar)
                if producto=="4":
                    sal=procesos(movimiento,cantidad,sal)
                if producto=="5":
                    harina=procesos(movimiento,cantidad,harina)           
            
            existencias(arroz,cafe,azucar,sal,harina)
        else:
            print("El valor ingresado no es válido!")
