import mysql.connector
import csv

host = "localhost"
user = "Jose Manuel"
password = "JoseManuel"
database = "usuario"
table_name = "NomMail"
csv_file_path = "C:/Users/Jose Manuel/Desktop/UF1/mail.csv"

def getmail(nombre):
    try:
        with mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        ) as mydb:
            cursor = mydb.cursor()
            select_query = "SELECT * FROM {} WHERE nombre = %s".format(table_name)
            cursor.execute(select_query, (nombre,))
            result = cursor.fetchone()

            if result:
                print(f"Datos para el nombre {nombre}: {result}")
            else:
                print(f"No se encontraron datos para el nombre {nombre}")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

def adduser(nombre, email):
    try:
        with mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        ) as mydb:
            cursor = mydb.cursor()
            insert_query = "INSERT INTO {} (nombre, email) VALUES (%s, %s)".format(table_name)
            cursor.execute(insert_query, (nombre, email))
            mydb.commit()

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()

if __name__ == "__main__":
    try:
        nombre = input('Nombre de nombre: ')
        getmail(nombre)

        
        with mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        ) as mydb:
            cursor = mydb.cursor()
            select_query = "SELECT * FROM {} WHERE nombre = %s".format(table_name)
            cursor.execute(select_query, (nombre,))
            result = cursor.fetchone()

            if result:
                print(f"Ya existen datos para el nombre {nombre}.")
            else:
                nombre_usuario = input('Nombre de usuario: ')
                email = input('Nombre de email: ')

                
                print(f"Añadiendo usuario: {nombre_usuario}, {email}")

                adduser(nombre_usuario, email)

                
                print("Usuario añadido correctamente.")
     
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
