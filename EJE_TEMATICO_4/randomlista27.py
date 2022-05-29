import random
listatripulantes = [
'Alejandro Monroy',
'Andres Gomez',
'Carlos Olarte',
'Daniel Bustamante',
'Diego Hernandez',
'Edgar Rodriguez',
'Edward Avila',
'Felipe Quitian',
'Francisco Rojas',
'Greis Castro',
'Jaime Polo',
'Jehison Villalo',
'Jesus Botero',
'Johan Ramirez',
'Johan Florez',
'Jose Maigual',
'Jose Galvis',
'Jose Rodriguez',
'Juan Ruiz',
'Juan Diego',
'Juli B',
'Kimberly',
'Laura',
'Manuel Espinel',
'Martha Ascencio',
'Nelson ',
'Nelson Portilla',
'Nicolas',
'Nicolas Rodriguez',
'Numan Rizcala',
'Paola Vela',
'Richard Hernandez',
'Xiomara Laguado',
'Yamileth Mercado',
'Yira Jaimes'

]
continuar = " ";
while(continuar != "N"):
    tripulantepregunta = ""
    tripulanteresponde = ""
    while(tripulantepregunta == tripulanteresponde):
        tripulantepregunta =  random.choice(listatripulantes)
        tripulanteresponde =  random.choice(listatripulantes)
    print(f"El tripulante que pregunta es {tripulantepregunta} y el que responde es {tripulanteresponde}")
    listatripulantes.remove(tripulanteresponde)
    print(len(listatripulantes))
    if len(listatripulantes)==1:
        continuar ="N"
    else:
        continuar = input("Continuar? (S/N): ").upper()