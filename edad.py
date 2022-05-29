import datetime

añoactual= int(datetime.date.today().year)
fechaactual= datetime.date.today()

nombre = input("Escriba su nombre: ")
añodenacimiento = int(input("Escriba su año de nacimiento: "))

edad= añoactual-añodenacimiento
#edad= 2022-añodenacimiento

print(f"Hola {nombre}, bienvenido a MisionTIC 2022, hoy es {fechaactual}, su año de nacimiento es {añodenacimiento} y su edad es {edad} años.")