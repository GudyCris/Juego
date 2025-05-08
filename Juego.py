import sys
import random
from logica import comparar_jugada 


opciones = ["piedra", "papel", "tijera"]


if len(sys.argv) != 4:
    print("Debe ingresar las dos palabras siguientes seguido de sus 3 elecciones: python juego.py <eleccion1> <eleccion2> <elecion3>")
    print("Las opciones a elegir son: piedra, papel o tijera")
    sys.exit(1)

humano = [op.lower() for op in sys.argv[1:]]
for op in humano:
    if op not in opciones:
        print(f"Opcion invalida: {op}. Las unicas opciones validas son piedra, papel o tijera.")
        sys.exit(1)

programa = [random.choice(opciones) for _ in range(3)]


print("El programa elige:", " ".join(programa))

puntos_humano = 0
puntos_programa = 0

# Comparar cada jugada
for i in range(3):
    resultado = comparar_jugada(humano[i], programa[i])
    if resultado == 1:
        puntos_humano += 1
    elif resultado == -1:
        puntos_programa += 1

# Mostrar resultados
print(f"Puntos Humano: {puntos_humano}")
print(f"Puntos Programa: {puntos_programa}")

# Determinar ganador
if puntos_humano > puntos_programa:
    print("¡El usuario Gano! ")
elif puntos_humano < puntos_programa:
    print("Perdiste. Gano el programa")
else:
    print("¡Empate!")

