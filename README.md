# nl-process   [TFI](http://ri.itba.edu.ar/handle/123456789/1836)

![PyPI pyversions](https://img.shields.io/badge/python-3+-green.svg?style=flat)
![scikit-learn](https://img.shields.io/badge/scikit--learn-blue)
![NumPy](https://img.shields.io/badge/nltk-blue)

## Descripción
Trabajo realizado para TFI de especialización. Se enfoca en la generación de un modelo Machine Learning utilizando Python, Nltk y Sklearn para clasificación de  mensajes de redes sociales.

## Objetivo
Obtener tendencias de opinión pública sobre un producto de una empresa, mediante la implementación de técnicas de análisis de sentimientos sobre mensajes de clientes en redes sociales.

## Objetivos específicos
- Crear dataset obteniendo una cantidad sustancial de tweets relacionados con seguidores de la empresa y “nombradores” de la misma.
- Analizar y seleccionar técnica de preparación de los datos.
- Analizar y seleccionar técnica de análisis de sentimientos para clasificación de polaridad de textos cortos.
- Aplicar técnicas seleccionadas.
- Visualizar e interpretar resultados obtenidos.

## Datos (2018)
La obtención de tweets puede ser realizada mediante la API ofrecida por Twitter. La conexión con la misma ofrece solo el acceso a datos públicos de la plataforma. Cuentas y Usuarios, Tweets y Respuestas, Mensajes Directos o Anuncios, son algunos de los módulos disponibles para desarrolladores. Las consultas realizadas tienen la posibilidad de ser configuradas con parámetros que permiten adaptar la consulta a cada necesidad. Las respuestas recibidas son objetos JSON, que incluyen datos ofrecidos según el tipo de consulta realizada.

## Implementación

Puede dividirse en tres partes: 
- Adquisición de datos y análisis exploratorio.
- Pre proceso de los datos.
- Entrenamiento y testeo.

Tanto la etapa de adquisición de datos, como la de almacenamiento, fueron automatizadas mediante utilización de scripts en python, aprovechando las ventajas de la biblioteca tweepy para el uso de la API.
Para la exploración de datos se utilizaron varias herramientas, comandos de shell de Linux, desde LibreOffice Calc, Orange3 y Python.
Finalmente, para el modelado y testeo se utilizó la herramienta Orange3, aunque más tarde se implementó cien por ciento en Python con la librería sklearn y Matplotlib.

## Archivos

#### Preprocess_GridSearch_NegPos
Notebook principal con pipeline completo.

#### Makefile
Automatiza la descarga mediante el uso de parámetros configurables. Provee la capacidad de rehacer las descargas en lote.

#### Classifier
Toma tweets almacenados en archivos CSV desde un directorio pasado por parámetros, nos lo muestra uno a uno y permite clasificar presionando solo un botón. La salida la realiza en otro archivo CSV. 
La versión 1, muestra tweets y da opción de clasificar. El clasificador es almacenado en una nueva columna delante.

#### Twreader
Descarga propiamente los tweets a procesar. Se debe configurar la API de Twitter.
```bash
# Configuraciones
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'
```

#### 0_500_union_salida_clasificada.csv
Archivo con 500 tweets clasificados.
#### custom_stopwords.txt
Archivo con stopwords utilizadas para este trabajo.
#### CSV
Contiene todos los CSV utilizados para exploración, entrenamiento y testeo.
#### NBOOKS
Contiene notebooks utilizados para exploración, entrenamiento y testeo.