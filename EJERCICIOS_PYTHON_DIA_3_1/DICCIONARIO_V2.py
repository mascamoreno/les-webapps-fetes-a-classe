def obtener_correo(diccionario, nombre):

    correo = diccionario.get(nombre, "No se encontró el nombre en la lista")
    return correo

if __name__ == "__main__":
    import sys

    
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre>")
        sys.exit(1)

    nombre_usuario = sys.argv[1]

    
    diccionario_correos = {
    
        "Mercedes": "mcast386@xtec.cat",
        "Rayane": "rayane@rayane.sa",
        "Mohamed": "moha@gmail.com",
        "Jad": "jad@gmail.com",
        "Oriol": "joam@gmail.com",
        "Elias": "hola123@gmail.com",
        "Armau": "arnau@gmail.com",
        "Asdrúbal": "asdrubal@gmail.com",
        "Adrian": "pedrosanchez@asix2.com",
        "Eric": "eric@gmail.com",
        "Emma": "pacosanz@gmail.com",
        "nishwan2": "nishwan@gmail.com",
        "Javi": "javi@gmail.com",
        "Novel": "novelferreras49@gmail.com",
        "Bruno": "elcigala@gmail.com",
        "David": "argentino@gmail.com",
        "Judit": "judit@gmail.com",
        "Joao": "joao@gmail.com",
        "Laura": "laura@gmail.com",
        "enrico": "123@gmail.com",
        "Joel": "joelcobre@gmail.com",
        "Aaron": "aaron@gmail.com",
        "Moad": "moad@gmail.com",     
      
    }

    
    correo_usuario = obtener_correo(diccionario_correos, nombre_usuario)

   
    print(f"El correo asociado a {nombre_usuario} es: {correo_usuario}")
