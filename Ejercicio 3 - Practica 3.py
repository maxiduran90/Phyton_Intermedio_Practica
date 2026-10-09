# Solicitar un número al usuario
numero = int(input("Ingresa un número entero: "))

# Verificar si el residuo al dividir entre 2 es cero
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")