from claseConjuntos import Conjunto

conjuntoA = Conjunto([1, 2, 3, 4])
conjuntoB = Conjunto([3, 6, 9])
union = conjuntoA + conjuntoB
print(union)

conjuntoC = Conjunto([1,2,3,4])
conjuntoD = Conjunto([3,6,9])

print(conjuntoC - conjuntoD)

conjuntoE = Conjunto([3,2,1])
conjuntoF = Conjunto([2,1,3])

if(conjuntoE == conjuntoF):
    print("Los elementos del conjunto son iguales")


