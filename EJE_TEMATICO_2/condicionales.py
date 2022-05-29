clima="lluvia"
tipolluvia="suave"

if clima=="lluvia":
    print("hoy es un dia lluvioso")
    if tipolluvia=="fuerte":
        print ("y esta lloviendo fuerte")
    elif tipolluvia=="suave":
        print ("y esta lloviendo suave")
    else:
        print ("esta cesando la lluvia")

elif clima=="soleado":
    print("hoy es una dia soleado")

elif clima=="frio":
    print("hoy es una dia frio")   

else:
    print("hoy es una dia normal")
        