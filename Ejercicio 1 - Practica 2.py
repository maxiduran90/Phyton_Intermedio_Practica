try:
    # Solicitamos los dos números al usuario
    num1 = float(input("Ingresa el primer número (dividendo): "))
    num2 = float(input("Ingresa el segundo número (divisor): "))

    # Intentamos realizar la división
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

except ZeroDivisionError:
    # Capturamos específicamente el error de división por cero
    print("¡Error! No se puede dividir un número entre cero.")