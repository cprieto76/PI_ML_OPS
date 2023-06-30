from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import zipfile


# uvicorn main:app --reload

app = FastAPI(title='Proyecto Machine Learning Operations', 
              description='Carlos Prieto')


# Cargar los datasets

datafinal_df = None
crew_df = None
cast_df = None
genres_df = None
Machine_df = None


@app.on_event('startup')
async def startup():
    global datafinal_df, crew_df, cast_df, genres_df, Machine_df
    
    zip_file = 'datosorigen.zip'
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('../data/')  
        # Descomprime los archivos en el directorio '../data/'
    
    datafinal_df = pd.read_csv('../data/datafinal.csv')
    crew_df = pd.read_csv('../data/crew.csv')
    cast_df = pd.read_csv('../data/cast.csv')
    genres_df = pd.read_csv('../data/genres_final.csv')
    Machine_df = pd.read_csv('../data/Machine_data.csv')


def extrae_data_zip():
    """
    Extrae y carga datos de un archivo comprimido.
    
    Returns:
        datafinal_df (DataFrame): Dataframe que contiene los datos finales.
        crew_df (DataFrame): Dataframe contiene datos de equipo de producción.
        cast_df (DataFrame): Dataframe contiene datos de reparto de películas.
        genres_df (DataFrame): Dataframe contiene géneros de películas.
        Machine_df (DataFrame): Dataframe contiene géneros y popularidad
    """
    return datafinal_df, crew_df, cast_df, genres_df, Machine_df


# Machine Learning - "Modelo Nearest K neigbhbors"


def movie_rec(movie_title):
    """
    Devuelve lista de 5 películas recomendadas

    Args:
        movie_title (str): El título de la película.

    Returns:
        list: Una lista de películas recomendadas.
            Si  no se encuentra la película, se devuelve 
            "La película no esta en la base de datos."
    """

    # Cargar el archivo CSV con los datos
    _, _, _, _, Machine_data = extrae_data_zip()
    # movie_data = pd.read_csv('Machine_data.csv')

    # Convertir el título de la película a minúsculas
    movie_title = movie_title.lower()

    # Buscar la película por título en la columna 'title'
    movie = Machine_df[Machine_df['title'].str.lower() == movie_title]

    if len(movie) == 0:
        return "La película no esta en la base de datos."

    # Obtener el género y la popularidad de la película
    movie_genre = movie['genero'].values[0]
    movie_popularity = movie['popularity'].values[0]

    # Crear una matriz de características para el modelo vecinos más cercanos
    features = Machine_df[['popularity']]
    genres = Machine_df['genero'].str.get_dummies(sep=' ')
    features = pd.concat([features, genres], axis=1)

    # Manejar valores faltantes (NaN) reemplazándolos por ceros
    features = features.fillna(0)

    # Crear el modelo de vecinos más cercanos
    nn_model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    nn_model.fit(features)

    # Encontrar las películas más similares
    _, indices = nn_model.kneighbors([[movie_popularity] + [0] 
                                      * len(genres.columns)], n_neighbors=6)

    # Obtener los títulos de las películas recomendadas
    recomendados = Machine_df.iloc[indices[0][1:]]['title']

    return recomendados


# Endpoints

# Ruta archivo index.html


@app.get("/", response_class=HTMLResponse, tags=['Index'])
async def read_index_html():
    """
    Ruta para el archivo index.html.
    """
    with open("index.html") as f:
        return f.read()
# ---------------------------------------------------


@app.get('/about/', tags=['Credits'])
async def about():
    """
    GET /about/

    Retorna un diccionario con info sobre el Proyecto individual Data Science.
    """
    return {'message': 'Proyecto Individual 1: Data Science'}

# ---------------------------------------------------


@app.get("/cantidad_filmaciones_mes/{mes}", tags=['Primera Consulta'])
async def cantidad_filmaciones_mes_endpoint(mes: str):
    """
    Endpoint para obtener la cantidad de películas estrenadas
    en un mes específico.
    
    Args:
        mes (str): Nombre del mes en formato de texto.
    
    Returns:
        dict: Diccionario con el mensaje que indica la cantidad de filmaciones 
        en el mes consultado.
    """
    # Convertir el nombre del mes a minúsculas para realizar la comparación
    mes = mes.lower()

    # Verificar si el valor del mes es válido
    meses_validos = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
                     "julio", "agosto", "septiembre", "octubre", "noviembre", 
                     "diciembre"]
    if mes not in meses_validos:
        raise HTTPException(status_code=400, 
                            detail="Mes incorrecto.")

    # Extraer los DataFrames del archivo ZIP
    datafinal_df, _, _, _, _ = extrae_data_zip()

    # Filtrar el DataFrame para obtener las filas correspondientes al mes 
    # consultado
    filmaciones_mes = datafinal_df[datafinal_df['month_time'].str.lower() == mes]

    # Obtener la cantidad de películas estrenadas en el mes consultado
    cantidad_filmaciones = len(filmaciones_mes)

    mensaje = f"La cantidad de películas estrenadas en {mes.capitalize()} es: {cantidad_filmaciones}"
    return {"mensaje": mensaje}

# ----------------------------------------------------


@app.get("/cantidad_filmaciones_dia/{dia}", tags=['Segunda Consulta'])
async def cantidad_filmaciones_dia_endpoint(dia: str):
    """
    Endpoint para obtener cantidad de películas estrenadas en un día específico.
    
    Args:
        dia (str): Nombre del día en formato de texto.
    
    Returns:
        dict: Diccionario con el mensaje que indica la cantidad de peliculas en el día consultado.
    """
    # Convertir el nombre del día a minúsculas para realizar la comparación
    dia = dia.lower()

    # Verificar si el valor del día es válido
    dias_validos = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    if dia not in dias_validos:
        raise HTTPException(status_code=400, detail="El valor del día es incorrecto.")

    # Extraer los DataFrames del archivo ZIP
    datafinal_df, _, _, _, _ = extrae_data_zip()

    # Filtrar el DataFrame para obtener las filas correspondientes al día consultado
    filmaciones_dia = datafinal_df[datafinal_df['day_time'].str.lower() == dia]

    # Obtener la cantidad de películas estrenadas en el día consultado
    cantidad_filmaciones = len(filmaciones_dia)

    mensaje = f"La cantidad de películas estrenadas en {dia.capitalize()} es: {cantidad_filmaciones}"
    return {"mensaje": mensaje}

# ----------------------------------------------------
@app.get("/score_titulo/{titulo}", tags=['Tercera Consulta'])
async def titulo_de_la_filmacion_endpoint(titulo: str):
    """
    Endpoint para obtener información de una filmación a partir de su título.
    
    Args:
        titulo (str): Título de la filmación en formato de texto.
    
    Returns:
        dict: Diccionario con el mensaje que contiene el título, año de estreno y score/popularidad de la filmación.
              En caso de no encontrar la filmación, se devuelve un mensaje de error.
    """
    # Convertir el título de la filmación a minúsculas para realizar la comparación
    titulo = titulo.lower()

    # Extraer los DataFrames del archivo ZIP
    datafinal_df, _, _, _, _ = extrae_data_zip()

    # Filtrar el DataFrame para obtener la fila correspondiente al título de la filmación
    filmacion = datafinal_df[datafinal_df['title'].str.lower() == titulo]

    if filmacion.empty:
        return {"mensaje": f"No se encontró la filmación con el título: {titulo}"}

    # Obtener el título, año de estreno y score de la filmación
    titulo_filmacion = filmacion['title'].iloc[0]
    año_estreno = filmacion['release_year'].iloc[0]
    score = round(filmacion['popularity'].iloc[0], 2)

    mensaje = f"La película '{titulo_filmacion}' fue estrenada en el año {año_estreno} con un score/popularidad de {score}"
    return {"mensaje": mensaje}

# ----------------------------------------------------
@app.get("/votos_titulo/{titulo}", tags=['Cuarta Consulta'])
async def votos_valor_de_la_filmacion_endpoint(titulo: str):
    """
    Endpoint para obtener información sobre los votos y valoraciones de una filmación a partir de su título.
    
    Args:
        titulo (str): Título de la filmación en formato de texto.
    
    Returns:
        dict: Diccionario con el mensaje que contiene el título, año de estreno, cantidad de votos y promedio de votaciones de la filmación.
              En caso de no encontrar la filmación o no cumplir con la cantidad mínima de votos, se devuelve un mensaje de error.
    """
    # Convertir el título de la filmación a minúsculas para realizar la comparación
    titulo = titulo.lower()

    # Extraer los DataFrames del archivo ZIP
    datafinal_df, _, _, _, _ = extrae_data_zip()

    # Filtrar el DataFrame para obtener la fila correspondiente al título de la filmación
    filmacion = datafinal_df[datafinal_df['title'].str.lower() == titulo]

    if filmacion.empty:
        return {"mensaje": f"No se encontró la filmación con el título: {titulo}"}

    # Obtener el título, año de estreno, cantidad de votos y promedio de votaciones de la filmación
    titulo_filmacion = filmacion['title'].iloc[0]
    año_estreno = filmacion['release_year'].iloc[0]
    cantidad_votos = round(filmacion['vote_count'].iloc[0])
    promedio_votaciones = filmacion['vote_average'].iloc[0]

    if cantidad_votos < 2000:
        return {"mensaje": f"La filmación '{titulo_filmacion}' no cumple con la condición de tener al menos 2000 votos"}

    mensaje = f"La película '{titulo_filmacion}' fue estrenada en el año {año_estreno}. La misma cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {promedio_votaciones}"

    return {"mensaje": mensaje}

# ----------------------------------------------------
@app.get("/get_actor/{nombre}", tags=['Quinta Consulta'])
def nombre_actor(nombre: str):
    """
    Endpoint para obtener información sobre un actor a partir de su nombre.
    
    Args:
        nombre (str): Nombre del actor en formato de texto.
    
    Returns:
        dict: Diccionario con el nombre del actor, la cantidad de películas en las que ha participado, el promedio de retorno monetario de las películas
              y una lista de diccionarios con los títulos y retornos monetarios de las películas en las que ha participado.
    """
    datafinal_df, _, cast_df, _, _ = extrae_data_zip()

    # Filtrar las filas en las que el actor aparece en la columna "cast"
    actor_movies = cast_df[cast_df['cast'].str.contains(nombre, case=False)]
    
    # Verificar si se encontraron películas del actor
    if actor_movies.empty:
        return {"mensaje": f"No se encontró al actor {nombre} en la base de datos."}
        
    # Obtener los ID de las películas en las que el actor ha participado
    movie_ids = actor_movies['id'].tolist()
    
    # Filtrar el dataset "datafinal_df" para obtener los nombres y retornos monetarios de las películas correspondientes
    movies = datafinal_df[datafinal_df['id'].isin(movie_ids)]
    
    # Obtener la cantidad de películas en las que el actor ha participado
    movie_count = len(movies)
    
    # Obtener el promedio de retorno monetario de las películas
    average_revenue = round(movies['revenue'].mean(), 2)

    
    # Crear una lista de diccionarios con los nombres y retornos monetarios de las películas
    movie_info = []
    for _, row in movies.iterrows():
        movie_info.append({
            "titulo": row['title'],
            "retorno_monetario": row['revenue']
        })
    
    return {
        "nombre_actor": nombre,
        "cantidad_peliculas": movie_count,
        "promedio_retorno_monetario": average_revenue,
        "peliculas": movie_info
    }

# ----------------------------------------------------
@app.get("/get_director/{nombre}", tags=['Consulta 6'])
def nombre_director(nombre: str):
    """
    Endpoint para obtener información sobre un director a partir de su nombre.
    
    Args:
        nombre (str): Nombre del director en formato de texto.
    
    Returns:
        dict: Diccionario con el nombre del director, las ganancias totales de las películas que ha dirigido y una lista de diccionarios
              con los ID, títulos, años, presupuestos, ingresos y relaciones de las películas dirigidas por el director.
    """
    datafinal_df, crew_df, _, _, _ = extrae_data_zip()

    # Filtrar las filas en las que el director aparece en la columna "crew_name" y "crew_job" contiene "Director"
    director_movies = crew_df[(crew_df['crew_name'].str.contains(nombre, case=False)) & (crew_df['crew_job'].str.contains("Director"))]
    
    # Verificar si se encontraron películas del director
    if director_movies.empty:
        return {"mensaje": f"No se encontró al director {nombre} en la base de datos."}
    
    # Obtener los ID de las películas en las que el director ha trabajado
    movie_ids = director_movies['id'].tolist()
    
    # Filtrar el dataset "datafinal_df" para obtener los nombres, años, presupuestos, ingresos y relación de las películas correspondientes
    movies = datafinal_df[datafinal_df['id'].isin(movie_ids)]
    
    # Calcular las ganancias sumando todas las relaciones de las películas
    ganancias = round(movies['return'].sum(), 2)
    
    # Crear una lista de diccionarios con los ID, nombres, años, presupuestos, ingresos y relación de las películas
    movie_info = []
    for _, row in movies.iterrows():
        movie_info.append({
            "id": row['id'],
            "titulo": row['title'],
            "anio": row['release_year'],
            "presupuesto": row['budget'],
            "ingresos": row['revenue'],
            "relacion": row['return']
        })
    
    return {
        "nombre_director": nombre,
        "ganancias": ganancias,
        "peliculas": movie_info
    }

# Endpoint para la recomendación de películas
# ----------------------------------------------------
@app.get("/recomendacion/{movie_title}", tags=['Machine Learning'])
def recomendar_pelicula(movie_title: str):
    """
    Devuelve una lista de las 5 películas recomendadas basadas en una película dada.

    Args:
        movie_title (str): El título de la película.

    Returns:
        dict: Un diccionario con las películas recomendadas como una lista.
    """

    Peliculas_recomendadas = movie_rec(movie_title)
    return {"Peliculas Recomendadas": Peliculas_recomendadas.tolist()}


# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)