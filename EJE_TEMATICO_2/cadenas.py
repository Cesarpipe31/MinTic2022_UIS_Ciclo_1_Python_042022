# CADENAS

palabra = "python"

# BUSQUEDA DE CARACTERES
print(palabra[0])
print(palabra[1])
print(palabra[2])
print(palabra[3])
print(palabra[4])
print(palabra[5])
print(palabra[-3])
print(palabra[0:2])
print(palabra[1:3])

# DIRECTORIO DE OPCIONES DE CADENAS
print(dir(palabra))

# CONVERTIR A MAYUSCULA
print(palabra.upper())

# CONVERTIR A MINUSCULA
print(palabra.lower())

# LETRA CAPITAL
print(palabra.capitalize())

# REEMPLAZAR CARACTERES
print(palabra.replace('h','hh'))

# CONTAR CARACTERES
print(palabra.count('h'))

# PREGUNTAR SI INCIA CON UN CARACTER
print(palabra.startswith('p'))

# PREGUNTAR SI FINALIZA CON UN CARACTER
print(palabra.endswith('n'))

# RECORTAR UN CARACTER DE UNA CADENA
print(palabra.split('y'))

# BUSCAR UN CARACTER EN LA CADENA
print(palabra.find('y'))

# INDEXAR UN CARACTER EN LA CADENA
print(palabra.index('t'))

# SABER SI LA CADENA ES ALFANUMERICA
print(palabra.isalpha())

# SABER SI LA CADENA ES NUMERICA
print(palabra.isnumeric())

# SABER SI LA CADENA ES DECILAL
print(palabra.isdecimal())

# SABER SI LA CADENA ESTA EN MAYUSCULA
print(palabra.isupper())

# SABER SI LA CADENA ESTA EN MINUSCULA
print(palabra.islower())

# CONOCER LA LONGITUD DE LA CADENA
print(len(palabra))