import sys
import csv
import os.path

def existe(nom,dic):
    if str(nom) in dic:
        print(dic.get(nom))
    else:
        print("el nombre no existe")

def cargardic(fichero,dic):        
    with open(str(fichero)) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            dic[row[0]] = row[1]


#Programa principal
diccionario = {}
if len(sys.argv) != 3:
    print("Tiene que tener dos argumentos") 
elif not os.path.isfile(sys.argv[2]):
    print("El archivo o la ruta no existe")
else:
    cargardic(sys.argv[2],diccionario)
    existe(sys.argv[1],diccionario)