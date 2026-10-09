# Definimos los conjuntos A y B
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# Usando el método issubset()
if A.issubset(B):
    print("El conjunto A es un subconjunto de B.")
else:
    print("El conjunto A NO es un subconjunto de B.")