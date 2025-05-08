# logica.py

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
