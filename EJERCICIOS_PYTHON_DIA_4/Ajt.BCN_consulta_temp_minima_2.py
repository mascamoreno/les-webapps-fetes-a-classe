import csv

def imprimirtemp(date, code, temp):
    if code == '"D5"':
        print(date, 'Barcelona - Observatori Fabra', temp, sep=" | ")
    elif code == '"X2"':
        print(date, 'Barcelona - Zoo', temp, sep=" | ")
    elif code == '"X4"':
        print(date, '"Barcelona - el Raval', temp, sep=" | ")
    elif code == '"X8"':
        print(date, 'Barcelona - Zona Universitaria', temp, sep=" | ")

ruta_archivo_csv = "C:/Users/Jose Manuel/Desktop/UF1/2023_MeteoCat_Detall_Estacions.csv"

listaTemp = []

with open(ruta_archivo_csv, 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    for linea in lector_csv:
        for valor in linea:
            a = valor.split(",")
            if a[3] == '"TM"':
                listaTemp.append([a[-1]])

tempmin = min(listaTemp)


with open(ruta_archivo_csv, 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    for linea in lector_csv:
        for valor in linea:
            a = valor.split(",")
            if tempmin[0] == a[-1]:
                imprimirtemp(a[0],a[2],a[-1])