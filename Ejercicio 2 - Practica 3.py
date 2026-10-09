# Definimos la función que acepta la palabra y la lista mediante *args
def buscar_palabra(palabra_a_buscar, *lista_palabras):
    # Usamos un operador ternario para definir el resultado
    resultado = "Encontrada" if palabra_a_buscar in lista_palabras else "No encontrada"
    return resultado

# 1. Pedimos al usuario la palabra que desea buscar
busqueda = input("Introduce la palabra a buscar: ").strip()

# 2. Pedimos la lista de palabras separadas por espacios y las convertimos en una lista real
entrada_usuario = input("Introduce la lista de palabras separadas por espacios: ")
lista_ingresada = entrada_usuario.split()

# 3. Llamamos a la función "desempaquetando" la lista con asterisco (*) para pasarla como *args
estado = buscar_palabra(busqueda, *lista_ingresada)

# 4. Mostramos el resultado
print(f"Resultado: La palabra '{busqueda}' fue {estado.lower()}.")