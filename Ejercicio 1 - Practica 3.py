# Solicitar los dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Aplicar el operador ternario para encontrar el mayor
mayor = num1 if num1 > num2 else num2

# Mostrar el resultado
print(f"El mayor de los dos números es: {mayor}")