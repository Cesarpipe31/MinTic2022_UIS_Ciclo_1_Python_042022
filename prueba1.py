# Se requiere hacer la conversión de Pesos Colombianos a Euros. Escriba una función llamada peso_a_euro que 
# reciba como dato de entrada el valor a convertir.

# Considerar que 1 euro equivale a la fecha a 4500 COP (Pesos colombianos).




def peso_a_euro(pesos):
    pesos_en_euro = 4500
    euro = pesos / pesos_en_euro
    return(euro)

pesos = float(input())
peso_a_euro(pesos)




