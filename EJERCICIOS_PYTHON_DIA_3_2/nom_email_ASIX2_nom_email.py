import csv

def crear_diccionario_desde_csv(ruta_csv):
    diccionario = {}

    with open(ruta_csv, 'r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        for fila in lector_csv:
            if fila and len(fila) == 2:  # Asegúrate de que la fila tenga dos valores
                nombre, correo = map(str.strip, fila)
                diccionario[nombre] = correo

    return diccionario

if __name__ == "__main__":
    
    ruta_csv = r'C:\Users\Jose Manuel\Desktop\UF1/nom_email_ASIX2_nom_email.csv'

    diccionario_correos = crear_diccionario_desde_csv(ruta_csv)

    nombre_usuario = input("Ingrese un nombre: ")

    
    correo_usuario = diccionario_correos.get(nombre_usuario, "No se encontró el nombre en la lista")

   
    print(f"El correo asociado a {nombre_usuario} es: {correo_usuario}")
