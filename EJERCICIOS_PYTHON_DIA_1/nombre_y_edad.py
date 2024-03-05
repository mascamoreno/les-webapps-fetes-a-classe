import datetime

def calcular_anio_100(nombre, edad_actual):
    anio_actual = datetime.datetime.now().year
    anio_cumplir_100 = anio_actual + (100 - edad_actual)
    return anio_cumplir_100

def main():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    anio_100 = calcular_anio_100(nombre, edad)

    print(f"Hola {nombre}! Cumplirás 100 años en el año {anio_100}.")

if __name__ == "__main__":
    main()
