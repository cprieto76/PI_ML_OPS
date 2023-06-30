# PROYECTO INDIVIDUAL 1 - Machine Learning Operations

#### Carlos Prieto

###### "DATA SCIENCE"

---

Proyecto Ciencia de Datos

Objetivo: utilizar dos datasets relacionados con películas y series llamados "movies_dataset" y "credits". 

Tareas a ejecutar:
1) ETL
2) EDA
3) Machine Learning 
$) Despliegue de una aplicación con API.

## Enunciado Proyecto

> *Comenzaste a trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming. Tu primer objetivo es crear un sistema de recomendación que aún no ha sido puesto en marcha. Sin embargo, te enfrentas a un desafío: los datos son poco maduros y requieren un proceso de limpieza y transformación.*

> *El proyecto abarcará desde el tratamiento y recolección de datos (tareas de Data Engineer) hasta el entrenamiento y mantenimiento del modelo de Machine Learning a medida que lleguen nuevos datos.*

# Diccionario de Carpetas y Archivos En Repositorio

```python
project_folders = {
    "data": "En esta carpeta se guardan los archivos descomprimidos del archivo datosorigen.csv",

    "EDA": "Esta carpeta contiene un archivo en formato .ipynb que se utilizó para realizar el análisis
	exploratorio de los datos.",

    "EDA/data_a_explorar": "Contiene el archivo con el que se realizó el análisis exploratorio de los datos.",

    "ETL": "Contiene 9 carpetas que incluyen procesos de transformación y limpieza de datos, tratamiento de
	columnas anidadas, sustitución de valores nulos, revisión de tipos de datos y códigos para eliminar
	valores repetidos o con formatos distintos a los que corresponden en su columna.",

    "ETL/1-Arquitectura_Nuevos_DataSets": "Contiene un archivo en formato .ipynb en el que se realizó la
	separación del dataset original y se crearon nuevos datasets. Para más detalles, revisar el
	diccionario de datos.",

    "ETL/6-DataSets_Final_movies_dataset": "Contiene un archivo en formato .zip en el que se encuentran
	comprimidos los archivos limpios.",

    "ETL/7-Datasets_original": "Contiene los archivos originales comprimidos en un archivo .zip.",

    "ETL/9-Proceso_ETL_credits": "Contiene dos archivos en formato .ipynb donde se realiza el proceso
	ETL del archivo credits.csv.",

    "Machine_Learning/Pruebas": "Contiene un archivo en formato .ipynb en el que se desarrolló la función
	para crear un modelo de aprendizaje utilizando el método 'vecinos más cercanos'.",

    "Scripts": "Contiene archivos relacionados con el entorno virtual"

    "datosorigen.zip": "Archivo comprimido en formato .zip que contiene la data limpia.",

    "index.html": "Archivo con el código en HTML, JavaScript y CSS que se utilizó para crear el Frontend.",

    "main.py": "Archivo que contiene todo el código de la API desarrollada con FastAPI.",

    "requirements.txt": "Archivo útil para realizar el despliegue en Render."
}

```

## 1) ETL. Exploracion, Transformacion y Limpieza de Datos

Actividades

a) Desanidar campos: 
- belongs_to_collection
- production_companies
- production:countries
- genres

Se descarto trabajar con la columna spoken_languages debido al alcance del trabajo
															
b) Rellenar valores nulos de los campos revenue y budget con el número 0.															
															
c) Eliminar los valores nulos del campo release date .															
													
d) De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.															
															
e) Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.															
												
f) Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,poster_path y homepage.															

## Diccionario de datos

Se separaron los datos en conjuntos específicos, como datafinal.csv, Machine_data.csv, cast_data.csv, crew_data.csv y genres_final.csv.

El archivo Machine_data.csv se utilizo para ananalis de Machine Learning. Se utilizo algoritmo de "Vecinos más Cercanos" (K-Nearest Neighbors). 

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo data_final.csv:

```python
column_description = {
    'id': 'ID de la película',
    'title': 'Título de la película',
    'overview': 'Descripción de la película',
    'popularity': 'Popularidad de la película',
    'vote_average': 'Promedio de votos de la película',
    'vote_count': 'Número de votos de la película',
    'status': 'Estado de la película',
    'original_language': 'Idioma original de la película',
    'runtime': 'Duración de la película en minutos',
    'budget': 'Presupuesto de la película',
    'revenue': 'Ingresos generados por la película',
    'tagline': 'Lema de la película',
    'id_btc': 'ID de la película en BTC',
    'name_btc': 'Nombre de la película en BTC',
    'poster_btc': 'URL del póster de la película en BTC',
    'backdrop_btc': 'URL del fondo de la película en BTC',
    'iso_639_1': 'Código ISO 639-1 del idioma',
    'language_name': 'Nombre del idioma',
    'release_year': 'Año de lanzamiento de la película',
    'return': 'Relación entre ingresos y presupuesto de la película',
    'companies_id': 'ID de las compañías de producción',
    'companies_name': 'Nombres de las compañías de producción',
    'countries_iso': 'Códigos ISO de los países de producción',
    'countries_name': 'Nombres de los países de producción',
    'release_date': 'Fecha de lanzamiento de la película',
    'month_time': 'Mes en el que se creó la película',
    'day_time': 'Día en el que se creó la película'
}

```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo Machine_data.csv:

```python
column_description = {
    'id': 'ID de la película',
    'title': 'Título de la película',
    'genero': 'Género de la película',
    'popularity': 'Popularidad de la película'
}

```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo cast_data.csv:

```python
column_description = {
    'id': 'ID de la película',
    'cast': 'Elenco de la película en formato JSON'
}
```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo crew_data.csv:

```python
column_description = {
    'id': 'ID de la película',
    'crew_credit_id': 'ID de crédito del equipo de producción',
    'crew_department': 'Departamento del equipo de producción',
    'crew_gender': 'Actividad en el equipo de producción',
    'crew_id': 'ID del miembro del equipo de producción',
    'crew_job': 'Trabajo del miembro del equipo de producción',
    'crew_name': 'Nombre del miembro del equipo de producción',
    'crew_profile_path': 'Ruta del perfil del miembro del equipo de producción'
}

```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo genres_final.csv:

```python
column_description = {
    'id': 'ID de la película',
    'id_genres': 'ID de géneros asociados a la película',
    'genero': 'Géneros de la película'
}

```

## 2) EDA. Análisis Exploratorio de Datos

Análisis exploratorio con técnicas estadísticas y visualizaciones. El archivo donde se llevó a cabo este análisis se encuentra en la carpeta "dataEDA", contiene las gráficas de análisis.

Durante el análisis exploratorio, utilicé las siguientes librerías: pandas, numpy, matplotlib.pyplot y seaborn. Estas herramientas me permitieron realizar diversas actividades, como calcular el porcentaje de valores faltantes en cada columna, filtrar las columnas con valores faltantes y examinar variables numéricas como "popularity", "vote_average", "vote_count", "runtime", "budget", "revenue" y "return".

También realicé cálculos de estadísticas descriptivas, como la media, mediana, desviación estándar y percentiles, para comprender la distribución de los datos. Generé histogramas y gráficos de caja para visualizar las variables numéricas, así como un gráfico de dispersión para analizar la relación entre los ingresos y presupuestos de las películas.

Además, realicé diversas visualizaciones para explorar la distribución de películas por mes y año de lanzamiento, los países con mayor producción cinematográfica, los géneros más populares a lo largo del tiempo, entre otros análisis. También generé un mapa de calor para examinar las relaciones entre las variables.

Este análisis exploratorio de datos fue fundamental para obtener conocimientos valiosos que nos ayudaron a comprender mejor el conjunto de datos y a tomar decisiones informadas en etapas posteriores del proyecto. Nos permitió descubrir patrones, identificar outliers y obtener una comprensión más profunda de las características de las películas y su éxito financiero.

# Sistema de Recomendación

## 3) Desarrollo de Modelos de Machine Learning

Además del análisis exploratorio de datos, implemente un modelo de Machine Learning para resolver el siguiente desafío:

* Sistema de recomendación: Utilizamos técnicas de filtrado colaborativo y/o basado en contenido para construir un sistema de recomendación de películas personalizadas.
* Esto permitió a los usuarios descubrir nuevas películas en función de sus preferencias. Mediante la API, los usuarios pueden ingresar el nombre de una película y el endpoint correspondiente les proporcionará 5 recomendaciones basadas en sus características y en las preferencias de otros usuarios con gustos similares. Esto mejora la experiencia del usuario al ofrecer sugerencias relevantes y personalizadas para su disfrute cinematográfico.

## Análisis "k vecinos más cercanos"

Para el desarrollo del sistema de recomendación, se nos proporcionó un enunciado. Cito fracción textual del enunciado: "Este consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas". El enunciado me pide que encuentre la similitud de puntuación entre una película y las demás películas.
Utilicé el método "k vecinos más cercanos" (KNN) para construir mi modelo. KNN es un algoritmo de aprendizaje automático supervisado que se utiliza para clasificación y regresión. Funciona encontrando los "k" puntos de datos más cercanos en función de una medida de distancia (por ejemplo, distancia euclidiana) y tomando una decisión basada en las etiquetas de clase o los valores de los vecinos más cercanos.

KNN funciona bien con datos estructurados y numéricos, lo cual puede ser adecuado para tu conjunto de datos si tienes columnas como valoración numérica y no numerica. Además, las medidas de distancia utilizadas en KNN se basan en la proximidad espacial de los puntos de datos, lo que puede ser más apropiado para conjuntos de datos numéricos.

KNN es especialmente útil cuando se espera que los puntos de datos similares estén cerca en el espacio de características. En el caso de datos numéricos, KNN tiene en cuenta la proximidad espacial de los puntos de datos y puede ser una opción adecuada para encontrar películas similares basándose en sus vecinos más cercanos. Esto significa que si una película tiene características numéricas, como la puntuación de los usuarios, KNN puede ser útil para encontrar películas con puntuaciones similares.

Sin embargo, lo interesante de KNN es que también puede aplicarse a conjuntos de datos que contienen información no numérica, como la columna de géneros en el caso de las películas. Aunque el algoritmo se basa en la distancia entre puntos de datos, la representación de los datos en un espacio de características adecuado puede permitir que KNN capture similitudes entre películas con géneros similares.

En conclusión, KNN es una buena opción cuando se trabaja con datos numéricos, pero también puede ser utilizado de manera efectiva en conjuntos de datos que contengan información no numérica, como los géneros de las películas. Esto permite construir un sistema de recomendación más completo al considerar tanto las puntuaciones como otros factores relevantes, proporcionando recomendaciones más precisas y personalizadas.

5) API con fastAPI

## Desarrollo de la API

La API se desarrolló utilizando FastAPI, un framework web de Python que nos permite crear servicios web de manera rápida y eficiente. A continuación, se mencionan las librerías y frameworks utilizados en la creación de la API, junto con una breve descripción de su función y uso en el proyecto:

- `FastAPI`: FastAPI es un framework web de alto rendimiento basado en Python. Se utilizó para crear y gestionar la API, proporcionando rutas y controladores para las diferentes funciones y endpoints.
- `pandas`: pandas es una librería de Python ampliamente utilizada para la manipulación y análisis de datos. Se utilizó para cargar y procesar los conjuntos de datos, permitiendo realizar consultas y realizar operaciones sobre ellos.
- `zipfile`: zipfile es una librería de Python que permite trabajar con archivos comprimidos en formato ZIP. Se utilizó para descomprimir archivos ZIP que contenían los conjuntos de datos necesarios para la API.
- `sklearn.neighbors`: sklearn.neighbors es un módulo de la librería scikit-learn que contiene algoritmos de vecinos más cercanos (K-Nearest Neighbors). Se utilizó para implementar funcionalidades relacionadas con el sistema de recomendación, como encontrar vecinos más cercanos basados en características similares.

Cada una de estas librerías y frameworks desempeñó un papel crucial en el desarrollo de la API y permitió implementar diferentes funcionalidades, desde el procesamiento de datos hasta la creación de modelos de Machine Learning para el sistema de recomendación. Su uso combinado proporcionó las herramientas necesarias para construir una API robusta y funcional.

Para instalar las librerías y frameworks mencionados, puedes utilizar los siguientes comandos:

a) . FastAPI:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install fastapi
</code></div></div></pre>

b) . pandas:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install pandas
</code></div></div></pre>

.c) zipfile:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>css</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-css">No es necesario instalar esta librería, ya que es parte de la biblioteca estándar de Python y viene incluida por defecto.
</code></div></div></pre>

d). scikit-learn:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install scikit-learn
</code></div></div></pre>

Una vez que hayas ejecutado estos comandos, tendrás instaladas las librerías y frameworks necesarios para ejecutar la API y utilizar sus funcionalidades. Es recomendable utilizar un entorno virtual para mantener un ambiente de desarrollo aislado y evitar conflictos entre las dependencias de diferentes proyectos.

Para crear y activar un entorno virtual con Virtualenv, puedes utilizar los siguientes comandos:

1. Instalación de Virtualenv:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install virtualenv
</code></div></div></pre>

2. Creación de un nuevo entorno virtual:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">virtualenv nombre_del_entorno
</code></div></div></pre>

3. Activación del entorno virtual:

* En Windows:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">nombre_del_entorno\Scripts\activate
</code></div></div></pre>

*Una vez que hayas activado el entorno virtual, puedes proceder a instalar las librerías y frameworks mencionados utilizando los comandos que proporcioné anteriormente. Esto asegurará que las dependencias se instalen dentro del entorno virtual y no afecten a tu entorno de desarrollo principal.

Recuerda que, para desactivar el entorno virtual, simplemente ejecuta el comando `deactivate`.

# Deployment

## Despliegue (Deployment)

Para el despliegue de la API en Render, se creó un archivo llamado `requirements.txt`. Este archivo es utilizado para especificar las dependencias y las versiones exactas de las librerías que son necesarias para que la API funcione correctamente.

Render utiliza el archivo `requirements.txt` para instalar automáticamente las dependencias especificadas en el entorno de ejecución de la aplicación. Al incluir las dependencias y las versiones adecuadas en este archivo, se asegura que la API pueda ejecutarse sin problemas en Render, con todas las bibliotecas necesarias correctamente instaladas.

El contenido del archivo `requirements.txt` sigue el siguiente formato:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>makefile</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-makefile">libreria1==version1
libreria2==version2
...
</code></div></div></pre>

Cada línea del archivo especifica el nombre de una librería seguido de `==` y la versión requerida. Pueden incluirse tantas líneas como sean necesarias para todas las dependencias de la API.

Una vez que el archivo `requirements.txt` está correctamente configurado, Render utilizará esta información para instalar automáticamente las librerías necesarias durante el proceso de despliegue de la API. Esto asegura que todas las dependencias estén disponibles en el entorno de ejecución de la aplicación en Render.


