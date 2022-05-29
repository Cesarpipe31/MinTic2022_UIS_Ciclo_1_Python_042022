import json

agenda = {
    '9':{'nombre':'Juan','telefonos':[3156367367,3205426633],'correo':'juan@uis.edu.co','direccion':'Calle 9 Cra 27','ciudad':'Bucaramanga'},
    '2':{'nombre':'Pedro','telefonos':[3206367367,3115426633],'correo':'pedro@uis.edu.co','direccion':'Calle 8 Cra 21','ciudad':'Bogota'},
    '7':{'nombre':'Jose','telefonos':[3226367367,3105426633],'correo':'jose@uis.edu.co','direccion':'Calle 7 Cra 22','ciudad':'Cali'},
    '8':{'nombre':'Maria','telefonos':[3506367367,3015426633],'correo':'maria@uis.edu.co','direccion':'Calle 2 Cra 17','ciudad':'Medellín'},
    '4':{'nombre':'Lucia','telefonos':[3176367367,3155426633],'correo':'lucia@uis.edu.co','direccion':'Calle 12 Cra 19','ciudad':'Barranquilla'}
    }

agenda["8"]["nombre"]="Sandra"
agenda["8"]["correo"]="sandra@uis.edu.co"

with open('contactos.json','w') as file:
    json.dump(agenda,file,indent=4)

print("________________________________________________________________________________________________________")
print("| NOMBRE \t TELEFONOS \t\t\t CORREO \t\t DIRECCION \t CIUDAD         |")
print("|_______________________________________________________________________________________________________|")

with open('contactos.json') as file:
    datos=json.load(file)
    for clave in datos.keys():
        print(f"{datos[clave]['nombre']} \t {datos[clave]['telefonos']} \t {datos[clave]['correo']} \t {datos[clave]['direccion']} \t {datos[clave]['ciudad']}")