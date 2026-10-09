import sys

# El primer argumento (sys.argv[0]) siempre es el nombre del propio archivo script.
# Si quieres exigir, por ejemplo, 5 argumentos adicionales, el total debe ser 6.
if len(sys.argv) < 3:
    print("Error: No se proporcionaron suficientes argumentos.", file=sys.stderr)
    print("Uso: python script.py <argumento1> <argumento2> <argumento3> <argumento4> <argumento5>", file=sys.stderr)
    sys.exit(1) # Finaliza el programa indicando que hubo un error

# Si se pasan los argumentos correctos, el código continúa aquí
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]
arg5 = sys.argv[5]

print(sys.argv)
print(f"Argumentos recibidos correctamente: {arg1} y {arg2} y {arg3} y {arg4} y {arg5}")