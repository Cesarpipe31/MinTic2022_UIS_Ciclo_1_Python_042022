sumapromedios=0
numerotripulantes=int(input("Escriba el numero de tripulantes: "))
for codigotripulante in range(1,numerotripulantes+1,1):
    nota1=float(input(f"Escriba la nota del reto 1 del tripulante codigo {codigotripulante}: "))
    nota2=float(input(f"Escriba la nota del reto 2 del tripulante codigo {codigotripulante}: "))    
    nota3=float(input(f"Escriba la nota del reto 3 del tripulante codigo {codigotripulante}: "))
    promediotripulante=(nota1+nota2+nota3)/3
    print(f"El promedio del tripulante codigo {codigotripulante} es: {promediotripulante}")
    sumapromedios=float(sumapromedios)+promediotripulante
promediogeneral=float(sumapromedios)/numerotripulantes
print(f"El promedio general del grupo es {promediogeneral}")