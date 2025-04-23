
import sys
import random

opciones = ["piedra", "papel", "tijera"]

def comparar_jugada(j1, j2):
    if j1 == j2:
        return 0
    elif (
        (j1 == "piedra" and j2 == "tijera") or
        (j1 == "papel" and j2 == "piedra") or
        (j1 == "tijera" and j2 == "papel")
    ):
        return 1
    else:
        return -1

if len(sys.argv) != 4:
    print("Uso: python juego.py <opción1> <opción2> <opción3>")
    print("Las opciones deben ser: piedra, papel o tijera")
    sys.exit(1)

humano = [op.lower() for op in sys.argv[1:]]
for op in humano:
    if op not in opciones:
        print(f"Opción inválida: {op}. Usa solo piedra, papel o tijera.")
        sys.exit(1)

programa = [random.choice(opciones) for _ in range(3)]

print("El programa elige:", " ".join(programa))

puntos_humano = 0
puntos_programa = 0

for i in range(3):
    resultado = comparar_jugada(humano[i], programa[i])
    
    if resultado == 1:
        puntos_humano += 1
    elif resultado == -1:
        puntos_programa += 1

print(f"Punteo: {puntos_humano} – {puntos_programa}")
if puntos_humano > puntos_programa:
    print("Ganador: Humano")
elif puntos_programa > puntos_humano:
    print("Ganador: Programa")
else:
    print("Resultado: Empate")
