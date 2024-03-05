def es_palindromo(palabra):
    return palabra == palabra[::-1]

palabra = input("Escribe una palabra: ")
if es_palindromo(palabra.lower().replace(" ", "")):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")