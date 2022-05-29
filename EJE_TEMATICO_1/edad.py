import datetime
añoactual = int(datetime.date.today().year)
fechaactual = datetime.date.today()

nombre = input("Escriba su nombre:")
añonacimiento = int(input("Escriba su año de nacimiento:"))

edad=añoactual-añonacimiento

print(f"Hola {nombre}, bienvenido a MisionTIC 2022, hoy es {fechaactual}, su año de nacimiento es {añonacimiento} y su edad es {edad} años")
