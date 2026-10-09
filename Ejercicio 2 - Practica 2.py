try:
    # Intentamos sumar un número entero y una cadena de texto
    resultado = 20 + "cinco"
except TypeError as error:
    # Capturamos el error de tipo y mostramos un mensaje personalizado
    print("❌ Error de tipo: No se puede sumar un número y una cadena de texto.")
    print(f"Detalle del error: {error}")