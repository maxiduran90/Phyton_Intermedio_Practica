def calcular_promedio(*args):
    # El operador ternario verifica si hay elementos en args
    return sum(args) / len(args) if args else 0

# Ejemplos de uso:
print(calcular_promedio(10, 30, 50, 70))  # Devuelve 40.0
print(calcular_promedio(20, 20))            # Devuelve 20.0
print(calcular_promedio())                # Devuelve 0 (gracias al operador ternario)