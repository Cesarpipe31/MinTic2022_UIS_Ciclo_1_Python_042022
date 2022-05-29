# Planteamiento de la situación

# Te contrataron como ingeniero de software junior para desarrollar una aplicación, para la empresa ServiPaquetes, 
# que ayude con la gestión de los paquetes. Específicamente para calcular el costo de los envíos de los paquetes. 
# Para ello, tú decides que harás la aplicación de forma progresiva, semana tras semana. Es decir, el software que 
# empieces a plantear desde esta semana, igual será útil en la última semana. La empresa te indica que es fundamental 
# que sigas el orden en el que ellos te indican los datos, puesto que el sistema de ellos los arroja en un orden específico.

# La empresa te dice que ahora el sistema de ellos es capaz de arrojar más de un dato de paquetes por vez, mediante el 
# ingreso del número de paquetes a calcular. Ellos desean saber, además de los datos que tu software ya imprime, el costo 
# total de todos paquetes que su sistema ingrese a tu software. Por ejemplo, el sistema ingresará a tu software el número 3, 
# indicando que se deberán leer los datos de 3 paquetes, entonces tu software deberá repetir el proceso de la semana anterior, 
# 3 veces, luego deberá imprimir el acumulado de los costos.

# Tu tarea esta semana es hacer que el software de la semana pasada lea una nueva variable que sea el número de paquetes a calcular. 
# Luego, que aplique el mismo algoritmo de cálculo de costo el número de veces que se haya indicado en la nueva variable, 
# imprimiendo los valores de volumen y costo. Al finalizar, el programa también deberá imprimir el valor de costo total.

# Lee detenidamente el planteamiento del reto, cuando se te indique que hay que seguir un orden, es necesario que así sea. 
# Sigue atentamente los pasos de la solución del reto si tienes dificultades al resolverlo.

# Planteamiento del reto

# Con respecto a la situación planteada, adapta el código de la semana pasada, de tal forma que se repita tantas veces como se 
# le indique al programa, también deberás llevar el conteo acumulado de los costos de cada paquete. Para esto, usa una variable 
# que lea un valor entero N y otra que esté destinada a acumular el valor de los costos. Usa un ciclo para repetir el algoritmo 
# de la semana anterior esas N veces, imprimiendo el volumen y costo de cada paquete y sumando el costo a la variable acumuladora. 
# Finalmente, imprime el costo total de los paquetes, cuando finalice el ciclo. 

# IMPORTANTE: Cuando vayas a entregar el reto, quítale todos los textos decorativos o informativos para el usuario. 
# Solo debes dejar el código funcional. Es decir, si imprimes cosas tipo “Ingrese …”, “El valor es …”, deberás de quitarlo. 
# Solo imprime lo que te indica el planteamiento del problema y en el orden en que se solicita.

# Acciones de aprendizaje

# Identifica las variables que se quieren definir.
# Recordar de qué manera se pueden recolectar datos por entrada estándar para definir variables.
# Recordar el uso de estructuras iterativas.

# Solución del reto

# Crea una variable llamada numeroPaquetes y haz que esta lea un número entero.
# Crea una variable llamada costoTotal y asígnale como valor inicial cero.
# Haz un ciclo for que se repita hasta numeroPaquetes.
# Dentro del ciclo, pon el código del reto anterior.
# A la variable costoTotal súmale el costo del paquete de la iteración.
# Imprime la variable costoTotal.


numeroPaquetes = input()
numeroPaquetes = int(numeroPaquetes)
costoTotal = 0
for i in range(numeroPaquetes):
    alto = input()
    alto = float(alto)
    ancho = input()
    ancho = float(ancho)
    profundo = input()
    profundo = float(profundo)
    volumen = alto * ancho * profundo
    costo = volumen * 5
    if (alto > 30) : costo = costo + 2000
    if (costo > 10000) : costo = costo + (costo * 0.19)
    costoTotal = costoTotal  + costo
    print(volumen)
    print(costo)
   
print(costoTotal)