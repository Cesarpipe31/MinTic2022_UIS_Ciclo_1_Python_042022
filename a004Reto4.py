# Reto tema 4
# Hecho: Ver Por hacer: Recibir una calificación
# Planteamiento de la situación

# Te contrataron como ingeniero de software junior para desarrollar una aplicación, para la empresa ServiPaquetes,
# que ayude con la gestión de los paquetes. Específicamente para calcular el costo de los envíos de los paquetes. 
# Para ello, tú decides que harás la aplicación de forma progresiva, semana tras semana. Es decir, el software que 
# empieces a plantear desde esta semana, igual será útil en la última semana. La empresa te indica que es fundamental 
# que sigas el orden en el que ellos te indican los datos, puesto que el sistema de ellos los arroja en un orden específico.

# Esta semana la empresa te comunica que tiene como plan cambiar el formato en el que se envían los datos a tu software, 
# pero por ahora están en fase de pruebas. No obstante, especificaron que quieren aplicar un descuento, que puede ir 
# de 0% a 100%, sobre el costo total para algunos de sus clientes.

# Tú, como buen ingeniero de software, no vas a dejar todo para última hora y decides hacer unas mejoras al programa de 
# tal forma que sea más fácil de mantener a futuro y, evidentemente, añadiendo la funcionalidad de aplicar un descuento 
# sobre el costo total.

# Tu tarea esta semana es refactorizar el código del programa, de tal forma que quede operativo mediante el uso de las 
# funciones. Decides que la mejor forma de hacerlo será separando el código en dos funciones. La primera llamada calcularCosto, 
# que reciba como parámetros el alto, ancho y profundo (en ese orden) y que retorne el costo del paquete, sin imprimir los 
# datos del paquete. La segunda función se llama costoTotal, que recibe como parámetros el número de paquetes a leer y el 
# descuento a aplicar sobre el costo total (en ese orden), que retorne el costo total con el descuento aplicado, sin imprimir 
# datos adicionales.

# Lee detenidamente el planteamiento del reto, cuando se te indique que hay que seguir un orden, es necesario que así sea. 
# Sigue atentamente los pasos de la solución del reto si tienes dificultades al resolverlo.

# Planteamiento del reto

# Con respecto a la situación planteada, tendrás que tomar el código de la semana pasada y separarlo en dos funciones: 
# calcularCosto(alto, ancho, profundo) y costoTotal(numeroPaquetes, descuento). Para esto, la primera función deberá 
# contener el código que calcula el costo de un paquete, dado su volumen, tal como se venía trabajando la semana pasada, 
# pero sin las impresiones en pantalla, la segunda función deberá solicitar los datos de cada paquete el número de veces 
# que el parámetro numeroPaquetes indique, similar a la semana pasada, pero sin las impresiones en pantalla, con el añadido 
# que esta vez hay que aplicarle un descuento proporcionado por el parámetro descuento. La función calcularCosto debe RETORNAR 
# el costo del paquete, mientras que la función costoTotal deberá RETORNAR el costo acumulado de los paquetes que ha leído, 
# con el descuento que se envíe como parámetro.

# IMPORTANTE: Cuando vayas a entregar el reto, quítale todos los textos decorativos o informativos para el usuario. Solo 
# debes dejar el código funcional. Es decir, si imprimes cosas tipo “Ingrese …”, “El valor es …”, deberás de quitarlo. 
# Solo imprime lo que te indica el planteamiento del problema y en el orden en que se solicita.

# Acciones de aprendizaje

# 1. Identifica las variables que se quieren definir.
# 2. Recordar de qué manera se pueden recolectar datos por entrada estándar para definir variables.
# 3. Recordar el uso de estructuras iterativas.
# 4. Recordar el uso de funciones.

# Solución del reto

# 1. Crea una función llamada calcularCosto que reciba los siguientes parámetros, en el orden respectivo: alto, ancho, profundo.
# a. Dentro de esta función deberás poner el código que calcula el costo de un paquete, según su volumen.
# b. Asegúrate de NO imprimir nada.
# c. Retorna el costo del paquete, una vez ha sido calculado.
# 2. Crea una función llamada costoTotal que reciba los siguientes parámetros, en el orden respectivo: numeroPaquetes, descuento.
# a. Dentro de esta función, adapta el código cíclico de la semana pasada, de tal forma que este se ejecute numeroPaquetes veces.
# b. Quita el cálculo del costo de paquete individual, ya que ahora tienes una función que lo retorna.
# c. Usa la función calcularCosto para enviarle los parámetros de alto, ancho y profundo, que se deben de solicitar previamente 
# por entrada estándar, y ve sumando lo que esta retorna en tu variable acumuladora de costo total.
# d. Asegúrate de NO imprimir nada.
# e. Calcula el descuento y aplicalo al costo total.
# f. Retorna el nuevo costo total.

# Nota: Aquí se plantea lo estrictamente necesario que se debe de hacer para solucionar el reto en CodeRunner, sin embargo, 
# te recomendamos que uses código adicional, impresiones de pantalla y demás elementos necesarios para resolverlo en tu computador. 
# A la hora de entregar el código, solo pega las dos funciones, sin ninguna impresión de pantalla.


def calcularCosto(alto, ancho, profundo):
    volumen = alto * ancho * profundo
    costo = volumen * 5
    if (alto > 30) : costo = costo + 2000
    if (costo > 10000) : costo = costo + (costo * 0.19)
    return float(costo)

def costoTotal (numeroPaquetes, descuento):
    costoTotal = 0
    for i in range(numeroPaquetes):
        alto = float(input())
        ancho = float(input())
        profundo = float(input())
        costo = calcularCosto(alto, ancho, profundo)
        costoTotal = costoTotal  + costo
    costoTotal = costoTotal - (costoTotal *  descuento / 100)
    return (costoTotal)





















