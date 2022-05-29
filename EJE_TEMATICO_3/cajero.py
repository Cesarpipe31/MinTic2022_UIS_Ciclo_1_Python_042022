from cajerofunciones import encabezado,validartarjeta,accesoerrado,error,validarclave,menu,consultarsaldo,retirar,consignar,despedida
from random import randint
saldo=randint(0,1000000)
tarjeta="1052673675"
clave="12345"
continuar=True
intentostarjeta=0
intentosclave=0
while intentostarjeta<3:
    if validartarjeta(tarjeta)==True:
        intentostarjeta=3
        while intentosclave<3:
            if validarclave(clave)==True:
                intentosclave=3
                while continuar==True:
                    encabezado()
                    opcioncliente=menu()
                    if opcioncliente=="1":
                        consultarsaldo(saldo)
                    elif opcioncliente=="2":
                        saldo=retirar(saldo)     
                    elif opcioncliente=="3":
                        saldo=consignar(saldo)
                    elif opcioncliente=="4":
                        continuar=False
                    else:
                        error()
            else:
                intentosclave=intentosclave+1 
                accesoerrado(intentosclave)           
    else:
        intentostarjeta=intentostarjeta+1
        accesoerrado(intentostarjeta)    
despedida()