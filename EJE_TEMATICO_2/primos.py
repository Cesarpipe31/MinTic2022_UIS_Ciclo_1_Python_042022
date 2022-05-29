num=int(input("Escriba un numero para saber si es primo: "))
primo=True
for n in range(2, num):
    if num % n == 0:
        primo=False
if(primo==True):
    print("El numero es primo")
else:
    print("El numero no es primo")
