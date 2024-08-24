#!/usr/bin/env python3
#-----------------------------------------------------------------------------#
# Classifier                                            by Pedro, Diego  2018 #
# Toma tweets almacenados en archivos csv desde un directorio pasado por      #
# parametros, nos lo muestra uno a uno y permite clasificar presionando solo  #
# un boton. La salida la realiza en otro archivo csv.                         #
# Version:                                                                    #
# 1.0 - Muestra tweets y da opcion de clasificar. Almacena el clasificador en #
#       una nueva columna delante.
#-----------------------------------------------------------------------------#
from pathlib import Path
import sys
import csv
VERSION = 1.0


def ls(ruta=Path.cwd()):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]


if len(sys.argv) <= 1:
    print('\nSyntax Error: ')
    print("Sintaxis: $ classifier"+str(VERSION) +
          ".py <directorio_con_tweets_en_csv>\n")
    sys.exit(0)

# ------------------------ Inicializacion de variables -------------------------
# Configuraciones
# Nombre del directorio pasado por parametro.
dir_path = sys.argv[1]
try:
    number = int(sys.argv[2])
except:
    number = 0
lista_arq = ls(dir_path)
out_name = "salida_clasificada.csv"
cantidad_procesada = 0

csvOut = open(out_name, 'a') 	# Se abre archivo de salida
csvWriter = csv.writer(csvOut)  # Se crea generador de csv

for archivo in lista_arq:
    # Se abre archivo con tweets y se lo recorre
    with open(dir_path+'/'+archivo, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in reader:

            if number == 0:
                print('\n'+str(row))
                print('-------------------------------------------------------------')
                print('Cant: ', cantidad_procesada)
                print('p(positivo) | o(neutro) | n(negativo) | s(saltear) | q(salir)')
                print('-------------------------------------------------------------')
                clasif = input('Clasificar tweet: ')
                if clasif == 'p':
                    clasif = 'Positivo'

                elif clasif == 'o':
                    clasif = 'Neutro'

                elif clasif == 'n':
                    clasif = 'Negativo'

                elif clasif == 'q':
                    rta = input('Seguro desea salir? [s,n]: ')
                    if rta == 's':
                        csvOut.close()
                        exit()

                cantidad_procesada = cantidad_procesada + 1
                if (clasif == 'Positivo') or (clasif == 'Neutro') or (clasif == 'Negativo'):
                    row.append(clasif)
                    csvWriter.writerow(row)

            elif number > cantidad_procesada:
                cantidad_procesada = cantidad_procesada + 1
                # print(number,',',cantidad_procesada)
                continue
            elif number == cantidad_procesada:
                number = 0

csvOut.close()
