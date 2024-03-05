import random

def juego_adivinanza():
    print("Bienvenido al juego de adivinanza de números.")
    minimo = int(input("Ingresa el número mínimo del intervalo: "))
    maximo = int(input("Ingresa el número máximo del intervalo: "))

    numero_a_adivinar = random.randint(minimo, maximo)
    intentos = 0

    while True:
        intento_usuario = int(input("Intenta adivinar el número: "))
        intentos += 1

        if intento_usuario < numero_a_adivinar:
            print("El número es mayor.")
        elif intento_usuario > numero_a_adivinar:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_a_adivinar} en {intentos} intentos.")
            break

if __name__ == "__main__":
    juego_adivinanza()
