numerogirosmotor1=int(input("Escriba el numero de giros para el motor 1: "))
numerogirosmotor2=int(input("Escriba el numero de giros para el motor 2: "))
numerogirosmotor3=int(input("Escriba el numero de giros para el motor 3: "))
for giromotor1 in range(1,numerogirosmotor1+1,1):
    print(f"Motor 1 - Giro {giromotor1}")
    for giromotor2 in range(1,numerogirosmotor2+1,1):
        print(f"  Motor 2 - Giro {giromotor2}")
        for giromotor3 in range(1,numerogirosmotor3+1,1):
            print(f"   Motor 3 - Giro {giromotor3}")