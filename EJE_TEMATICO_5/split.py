#cadena=["item1, item2 ítem 3 ítem 4, ítem 5"]
#print(int(cadena.split(', ')[1].split(' ')[1]))

print("Esta es la clase de Python MisionTIC 2022".split())
print("Esta es la clase de Python MisionTIC 2022".split(maxsplit=1))
print("Esta, es, la, clase, de, Python, MisionTIC, 2022".split(sep=', ',maxsplit=2))

cadena="Inglés,Física,Sociales,Historia,Programación".split(sep=',')
cadena=list(cadena)
print(cadena)
print(type(cadena))

