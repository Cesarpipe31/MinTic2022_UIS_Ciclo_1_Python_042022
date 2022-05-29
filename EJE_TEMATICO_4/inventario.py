from inventariofunciones import despedida, existencias, menutipomovimiento, entradas, salidas, bajas, menugestionproductos, agregarproductos, actualizarproductos, borrarproductos
listacodigos=[546,645,241,745,321]
listaproductos=['arroz','cafe','azucar','sal','harina']
listaprecios=[3500,3500,4500,1000,600]
listacantidades=[0,0,0,0,0]
movimiento=""
while movimiento!="X":
    movimiento=menutipomovimiento()
    if movimiento=="X":
        despedida()
    elif movimiento=="P":
        opcionproductos=0
        while opcionproductos<5:
            opcionproductos=menugestionproductos()
            if opcionproductos==1:
                agregarproductos(listacodigos,listaproductos,listaprecios,listacantidades)
            if opcionproductos==2:
                actualizarproductos(listacodigos,listaproductos,listaprecios,listacantidades)  
            if opcionproductos==3:
                borrarproductos(listacodigos,listaproductos,listaprecios,listacantidades)                          
            if opcionproductos==4:
                existencias(listacodigos,listaproductos,listaprecios,listacantidades)
                input("Presione cualquier tecla para continuar...")
    elif movimiento=="I":
            existencias(listacodigos,listaproductos,listaprecios,listacantidades)
            input("Presione cualquier tecla para continuar...")    
    elif movimiento=="E":
        entradas(listacodigos,listaproductos,listaprecios,listacantidades)
    elif movimiento=="S":
        salidas(listacodigos,listaproductos,listaprecios,listacantidades)  
    elif movimiento=="B":
        bajas(listacodigos,listaproductos,listaprecios,listacantidades)     
    else:
        despedida()