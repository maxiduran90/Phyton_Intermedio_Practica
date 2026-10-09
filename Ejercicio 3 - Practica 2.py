# Crear un diccionario con datos de ejemplo
mi_diccionario = {"nombre": "Maxi", "edad": 35}

try:
    # Intentar acceder a una clave que no existe
    valor = mi_diccionario["Phyton"]
except KeyError as e:
    # Capturar la excepción y mostrarla
    print(f"Error: La clave no existe en el diccionario. Detalle: {e}")