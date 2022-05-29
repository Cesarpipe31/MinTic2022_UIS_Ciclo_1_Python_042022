# Operaciones con conjuntos
A = set(["verde", "azul", "amarillo", "naranja", "negro", "rojo"])
print(A)
B = set(["amarillo", "azul", "rojo", "gris", "marrón", "violeta"])
print(B)
C = set(["verde", "marrón", "amarillo", "violeta", "naranja", "rojo"])
print(C)

U = A.union(B).union(C)
print(U)

AnB = A.intersection(B)
print(AnB)

AnC = A.intersection(C)
print(AnC)

BnC = B.intersection(C)
print(BnC)

AnBnC = A.intersection(B).intersection(C)
print(AnBnC)

for color in U:
    colores = []
    for letra, conjunto in zip('ABC', [A, B, C]):
        if color in conjunto:
            colores.append(letra)
    colores_str = "-".join(colores)
    plural = "s" if len(colores) > 1 else ""''""
    print(f"{color} en conjunto{plural}: {colores_str}")

AuB=A.union(B)
print(AuB)
AdB=A.difference(B)
print(AdB)
AidjB=A.isdisjoint(B)
print(AidjB)
Aidj=A.isdisjoint({1, 2})
print(Aidj)
AissB=A.issubset(B)
print(AissB)
Aiss=A.issubset({'verde'})
print(Aiss)
AissA=A.issubset(A)
print(AissA)
AissA=A.issuperset(A)
print(AissA)
AissB=A.issuperset(B)
print(AissB)
Aiss=A.issuperset({'verde'})
print(Aiss)
AsdB=A.symmetric_difference(B)
print(AsdB)


tamañoA=len(A)

A.add('magenta')
print(A)
A.remove('naranja')
print(A)
A.pop()
print(A)
A.remove('azul')
print(A)
A.discard('negro')
print(A)
print(A > B)
AoB=A or B
print(AoB)
AyB=A and B
print(AyB)
AyB=A,B
print(AyB)

D=frozenset(range(5))

D.add(9)