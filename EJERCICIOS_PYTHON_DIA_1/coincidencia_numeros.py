def main():
    try:
        lista1 = [float(input(f"Introduce el número {i + 1} para la primera lista: ")) for i in range(5)]
        lista2 = [float(input(f"Introduce el número {i + 1} para la segunda lista: ")) for i in range(5)]

        numeros_coincidentes = [num for num in lista1 if num in lista2]

        print("\nNúmeros coincidentes en ambas listas:")
        for num in numeros_coincidentes:
            print(num)
    except ValueError:
        print("Por favor, introduce números válidos.")

if __name__ == "__main__":
    main()
