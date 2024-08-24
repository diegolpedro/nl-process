#!/usr/bin/env python3
#-----------------------------------------------------------------------------#
# nlprocess.py - nlprocess                              by Pedro, Diego  2018 #
# Basado en pdf NTLK                                                          #
# Version:                                                                    #
# 1.0 _ Lectura de archivos para procesamiento.                               #
# 2.0 _ Procesamiento de tokens agregado      .                               #
#-----------------------------------------------------------------------------#
VERSION=2.0
import sys
import nltk
import re
import csv

# nltk.download('punkt')

# Se verifica la existencia de argumentos
if len(sys.argv) <= 1:
    print('\nSyntax Error: ')
    print("Sintaxis: $ nlprocess_v"+str(VERSION)+".py <nombre_entrada.csv>\n")
    sys.exit(0)


#------------------------ Inicializacion de variables -------------------------
# Configuraciones
file_name=sys.argv[1]               # Nombre de archivo pasado por parametro.
stop_file="custom_stopwords.txt"    # Nombre del archivo de stopwords.


# Regex para emoticones en texto.
emoticons_str = r"""
(?:
    [:=;]               # Ojos
    [oO\-]?             # Nariz (optional)
    [D\)\]\(\]/\\OpP]   # Bocas
)"""

# Regex para tokenizar correctamente.
regex_str = [
    emoticons_str,
    r'<[^>]+>',                                           # Etiquetas HTML
    r'(?:@[\w_]+)',                                       # @Menciones
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",                     # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',                         # Numeros
    r"(?:[a-z][a-z'\-_ñáéíóú]+[a-z])",                    # Palabras con – y '
    r'(?:[\w_]+)',                                        # Otras palabras
    r'(?:\S)'                                             # Cualquier otra cosa
]

# Se arman objetos para regular expresions.
tokens_re   = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)

# Se carga archivos de STOPWORDS
with open(stop_file, newline='') as file:
    stopwords = file.read().splitlines()

# Se abre archivo con tweets y se lo recorre    
with open(file_name, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in spamreader:
        # Se normaliza texto, todo a minusculas.
        #tweet = row[2].lower()
        tweet = row[1].lower()

        # Tokenizado
        tokens = tokens_re.findall(tweet)

        # Remocion de stopwords
        tokens = [token for token in tokens if token not in stopwords] #COMENTADO

        # Quitar URLs
        tokens = [token for token in tokens if not re.findall("(?P<url>https?://[^\s]+)", token)] #COMENTADO

        # Descomentar para enviar token por token a un archivo.
        # with open("out_file.csv", 'a') as salida: 
        #     for token in tokens:        
        #         salida.write(token+'\n')

        print(tokens)

# Quitar stopwords cuando este toquenizado
# Implementado en notebooks
#for stop in stopwords:
#    tweet=tweet.replace(stop,'');
