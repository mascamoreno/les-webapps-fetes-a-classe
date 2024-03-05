import mysql.connector

host = "localhost"
user = "Jose Manuel"
password = "JoseManuel"
database = "usuario"
table_name = "NomMail"

def getmail(nombre):
    try:
        with mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        ) as mydb:
            cursor = mydb.cursor()
            select_query = "SELECT nombre, email FROM {} WHERE nombre = %s".format(table_name)
            cursor.execute(select_query, (nombre,))
            result = cursor.fetchone()

            if result:
                print(f"Nombre: {result[0]}, Correo electrónico: {result[1]}")
            else:
                print(f"No se encontraron datos para el nombre {nombre}")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

nombre_a_consultar = input("Introduce el nombre a consultar: ")
getmail(nombre_a_consultar)
