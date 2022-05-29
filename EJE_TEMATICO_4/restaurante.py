ORDEN_EJECUTAR = "Ejecutar"
TRANSACCION_VENDER = "V"
TRANSACCION_RETIRAR = "R"

def separar_orden_y_valor(orden):
    if orden == ORDEN_EJECUTAR:
        return (orden, 0)
    transaccion = orden[:1]
    valor = orden[1:]
    return (transaccion, float(valor))

def puede_retirar(retiro, saldo):
    return saldo >= retiro

def imprimir_resultados(ventas_realizadas, total_ventas, retiros_realizados, total_retiros, saldo):
    print(f"{ventas_realizadas} venta(s) por un total de {total_ventas} colones")
    print(f"{retiros_realizados} retiro(s) por un total de {total_retiros} colones")
    print(f"Dinero disponible: {saldo} colones")


def main():
    saldo = float(input("Ingrese saldo inicial:"))
    ventas_realizadas = 0
    total_ventas = 0
    retiros_realizados = 0
    total_retiros = 0
    orden = ""
    while orden != ORDEN_EJECUTAR:
        orden = input("Ingrese la orden: ")
        transaccion, valor = separar_orden_y_valor(orden)
        if transaccion == TRANSACCION_VENDER:
            ventas_realizadas += 1
            total_ventas += valor
            saldo += valor
        elif transaccion == TRANSACCION_RETIRAR:
            if puede_retirar(valor, saldo):
                saldo -= valor
                retiros_realizados += 1
                total_retiros += valor
    imprimir_resultados(ventas_realizadas, total_ventas,
                        retiros_realizados, total_retiros, saldo)

main()