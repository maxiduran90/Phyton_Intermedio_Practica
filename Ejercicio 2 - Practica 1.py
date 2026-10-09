# Definimos dos conjuntos A y B
A = {1, 7, 14, 19, 23}
B = {11, 19, 21, 23, 28}

# Encontramos los elementos que están en ambos conjuntos
# Usando el operador &
comunes = A & B

# O usando el método .intersection():
# comunes = A.intersection(B)

# Imprimimos el resultado
print("Elementos en A y en B:", comunes)