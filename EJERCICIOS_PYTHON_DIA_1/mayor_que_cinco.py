def main():
    numeros_mayores_que_5 = []

    for _ in range(10):
        try:
            numero = float(input("Ingrese un número: "))
            if numero > 5:
                numeros_mayores_que_5.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print("\nNúmeros mayores que 5:")
    for num in numeros_mayores_que_5:
        print(num)

if __name__ == "__main__":
    main()