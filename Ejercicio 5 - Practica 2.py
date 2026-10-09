def dividir_numeros():
    try:
        # Solicitamos los datos al usuario
        num1_str = input("Ingresa el primer número: ")
        num2_str = input("Ingresa el segundo número: ")
        
        # Intentamos convertir el primer número a float (o int)
        # Si no es un número válido, esto genera un ValueError
        num1 = float(num1_str)
        num2 = float(num2_str)
        
        # Intentamos realizar la división
        # Si num2 es cero, esto genera un ZeroDivisionError
        resultado = num1 / num2
        
        print(f"El resultado es: {resultado}")
        
    except ValueError:
        print("Error: El primer número (o el segundo) no es un valor numérico válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir un número entre cero.")

# Ejecutamos la función
dividir_numeros()