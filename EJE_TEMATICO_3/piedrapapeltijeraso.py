#MAQUINA
import random
juegos_ganados_maquina=0
juegos_ganados_humano=0
continuar_jugando=True
while continuar_jugando==True:
    numeroaleatorio=random.randint(1, 3)
    if numeroaleatorio==1:
        respuesta_maquina="Piedra"
    if numeroaleatorio==2:
        respuesta_maquina="Papel"
    if numeroaleatorio==3:
        respuesta_maquina="Tijeras"
    #HUMANO
    print("JUEGO PIEDRA, PAPEL O TIJERAS")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    print("4. Salir")
    seleccion=int(input("Seleccione una opcion para jugar: "))
    if seleccion==1:
        respuesta_humano="Piedra"
    if seleccion==2:
        respuesta_humano="Papel"
    if seleccion==3:
        respuesta_humano="Tijeras"
    if seleccion==4:
        continuar_jugando=False
        break
    #RESULTADO DEL JUEGO
    if respuesta_maquina==respuesta_humano:    
        print(f"Usted selecciono {respuesta_humano} y la maquina selecciono {respuesta_maquina}, es un empate!")
    else:    
        if(respuesta_maquina=="Piedra" and respuesta_humano=="Tijeras"):
            ganador="la Maquina"
            juegos_ganados_maquina=juegos_ganados_maquina+1
        if(respuesta_maquina=="Papel" and respuesta_humano=="Tijeras"):
            ganador="el Humano"
            juegos_ganados_humano=juegos_ganados_humano+1
        if(respuesta_maquina=="Tijeras" and respuesta_humano=="Piedra"):
            ganador="el Humano"
            juegos_ganados_humano=juegos_ganados_humano+1
        if(respuesta_maquina=="Papel" and respuesta_humano=="Piedra"):
            ganador="la Maquina"
            juegos_ganados_maquina=juegos_ganados_maquina+1
        if(respuesta_maquina=="Tijeras" and respuesta_humano=="Papel"):
            ganador="la Maquina"
            juegos_ganados_maquina=juegos_ganados_maquina+1                   
        if(respuesta_maquina=="Piedra" and respuesta_humano=="Papel"):
            ganador="el Humano"
            juegos_ganados_humano=juegos_ganados_humano+1           
        print(f"Usted selecciono {respuesta_humano} y la Maquina selecciono {respuesta_maquina}, el ganador es {ganador}")
print("RESULTADO DEL JUEGO")
print(f"La maquina obtuvo {juegos_ganados_maquina} puntos")
print(f"Usted obtuvo {juegos_ganados_humano} puntos")
if(juegos_ganados_maquina>juegos_ganados_humano):
    print("JAJAJA TE GANE!!!")
elif(juegos_ganados_maquina<juegos_ganados_humano):
    print("MUY BIEN, LE GANASTE A LA MAQUINA!!!")
else:
    print("ES UN EMPATE!!!")