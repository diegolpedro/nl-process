#!/usr/bin/env python3
#-----------------------------------------------------------------------------#
# twreader.py - twreader                                by Pedro, Diego  2018 #
# Basado en http://docs.tweepy.org                                            #
# Version:                                                                    #
# 1.0 _ Lectura de tweets con parametro unico y envio a archivo.              #
#-----------------------------------------------------------------------------#
import csv
import os       # Utilizada para leer variables de entorno.
import sys      # Utilizada para terminar la ejecucion.
import tweepy   # Uso de API de twitter.
VERSION = 1.0

if len(sys.argv) <= 1:
    print('\nSyntax Error: ')
    print("Sintaxis: $ twreader.py d <nombre_salida_sin.csv> <cantidad de tws>\n")
    sys.exit(0)

# ------------------------ Inicializacion de variables -------------------------
# Configuraciones
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

if len(sys.argv) <= 2:
    max_tweets = 10     # Cantidad de twits a descargar por defecto.
    print("Cantidad de tweets: \t(defecto) "+str(max_tweets))
else:
    max_tweets = int(sys.argv[2])
    print("Cantidad de tweets: \t"+str(max_tweets))

out_name = str(max_tweets)+'tws_' + sys.argv[1]+'.csv'  # Archivo de salida.
print("Nombre de salida: \t" + out_name)

# Autenticacion
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Se abre archivo de salida
csvFile = open(out_name, 'a')

# Se crea generador de csv
csvWriter = csv.writer(csvFile)

# Se obtienen solo los tweets oficiales o los nombramientos de ellos. No se
# descargan los retweets.
# --> tweet.created_at, tweet.user.screen_name, tweet.full_text <--
for tweet in tweepy.Cursor(api.search, tweet_mode='extended', q=sys.argv[1]+'-filter:retweets', lang='es').items(max_tweets):
    tweet.full_text = tweet.full_text.replace('\n', ' ')
    csvWriter.writerow(
        [tweet.created_at, tweet.user.screen_name, tweet.full_text])

csvFile.close()
