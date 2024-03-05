import random

def obtener_tirada_jugador():
    tirada = input("Elige tu tirada (piedra, papel o tijera): ").lower()
    while tirada not in ["piedra", "papel", "tijera"]:
        print("Tirada no válida. Inténtalo de nuevo.")
        tirada = input("Elige tu tirada (piedra, papel o tijera): ").lower()
    return tirada

def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        return "Jugador 1"
    else:
        return "Jugador 2"

def main():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    jugador1 = input("Nombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")

    while True:
        print("\nTurno de:", jugador1)
        tirada_jugador1 = obtener_tirada_jugador()

        print("\nTurno de:", jugador2)
        tirada_jugador2 = obtener_tirada_jugador()

        ganador = determinar_ganador(tirada_jugador1, tirada_jugador2)

        print("\nResultado:", ganador, "gana esta ronda.")

        jugar_nuevamente = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_nuevamente != 's':
            break

    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    main()
