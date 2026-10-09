# Definición de los conjuntos de prueba
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

# Opción 1: Usando el operador ^
resultado = conjunto_A ^ conjunto_B

# Opción 2: Usando el método symmetric_difference()
# resultado = conjunto_A.symmetric_difference(conjunto_B)

# Imprimir el resultado
print("Elementos en A o B, pero no en ambos:", resultado)