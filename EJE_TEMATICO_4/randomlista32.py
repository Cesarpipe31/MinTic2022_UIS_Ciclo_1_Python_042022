import random
listatripulantes = [
'Felipe',
'Natalia Garzon',
'Natalia Vásquez',
'Nilson Rosales',
'Carolina',
'Cesar Moreno',
'Manuel Felipe García',
'Yudy Mancipe',
'Daniel Felipe',
'José Alfredo Martínez Valdés',
'Johanna martinez',
'Sebastian Sanabria',
'Juan Francisco Suárez Suárez',
'Luis Ariza',
'Jaime Echandia',
'Carolina',
'Marino Cajas',
'julio garcia',
'David Gomez',
'juan arboleda'
]
continuar = " ";
while(continuar != "N"):
    tripulantepregunta = ""
    tripulanteresponde = ""
    while(tripulantepregunta == tripulanteresponde):
        tripulantepregunta = random.choice(listatripulantes)
        tripulanteresponde = random.choice(listatripulantes)
    print(f"El tripulante que pregunta es {tripulantepregunta} y el que responde es {tripulanteresponde}")
    listatripulantes.remove(tripulanteresponde)
    print(len(listatripulantes))
    if len(listatripulantes)==1:
        continuar ="N"
    else:
        continuar = input("Continuar? (S/N): ").upper()