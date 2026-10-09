nombre_archivo = "archivo_inexistente.txt"

try:
    # Intenta abrir el archivo en modo lectura ('r')
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    # Muestra el mensaje de error al usuario
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
    
    # Intenta crear el archivo si no existe (usando el modo 'w')
    print("Intentando crear el archivo...")
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Este es un archivo creado automáticamente.")
    print(f"¡El archivo '{nombre_archivo}' ha sido creado con éxito!")