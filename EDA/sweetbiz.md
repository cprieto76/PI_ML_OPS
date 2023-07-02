# Libreria sweetbiz [(https://pypi.org/project/sweetviz/)]

Herramienta toma dataframes de pandas y crea un informe HTML autónomo que se puede ver solo en un navegador o integrarse en cuadernos.

Además de crear visualizaciones interesantes y hermosas con solo dos líneas de código, proporciona un análisis que llevaría mucho más tiempo generar manualmente.

## Analisis del informe sweetviz_report.html (File Size:65.1 MB)
### Primer vistazo a estado de los datos que pueden requerir transformacion para un analisis mas acertado.

### 1. Overview

#### 1.1 Aspectos a destacar

1.1.1 Columnas 27 de las cuales:
- Variables Numericas :        10
- Variables de Texto:          13
- Variables Categoricas:        4

Nota: sweetbiz no reconoce el campo released_date como date sino como texto

1.1.2 Filas duplicadas:         0

### 2. Variables

#### 2.1 Id (Id de pelicula).                           Numérico

Identificador Unico ya que presenta 45436 valores diferentes. No hay valores repetidos.

#### 2.2 title (Titulo de pelicula).                     Texto

Existen 3150 registros que aparecen mas de una vez. Entre los titulos que mas se repiten de mayor a menor son:

- Cinderella:             11
- Hamlet:                  9
- Alice in Wonderland      9
- Beauty and the Beast     8
- Les Miserables           8
- Treasure Island          7
- The Three Musketeers     7

Nota: Revisar el porque de la diferencia y si tiene algun efecto en las solicitudes de la API y en el modelo de Machine Learning

#### 2.3 overview (Resumen breve de la pelicula).        Texto

- Los valores mas repetidos son N0overviewfound(133), NoOverview(7), Nomovieoverviewavailable(3), de ahi en adelante son los registros del overview de cada pelicula.
Entre estos tres valores suman 143 que sumados a los 946 valores faltantes daria un total de 1089 registros que representan un 2,4% 

#### 2.4 popularity (Puntaje popularidad).                Numerico

- Hay un valor maximo de 547 seguramente es un outlier lo que se deduce al observar el Q1(0), la media (3),  el Q3(4) y el 95%(11).
- Hay 40 ceros y la mediana es 1.
- Corrijiendo outliers y valores en 0 podemos establecer parametros estadisticos mas reales.

#### 2.5 vote_average (Puntaje promedio de reseñas).      Numérico

- Los valores en cero (2944 - 6%) pueden estar modificando las metricas. Es el valor mas comun, que puede deberse a la ausencia del dato debido a procedimientos en la obtencion de la información.
- Nota: Se debe revisar. 
- n segundo lugar de frecuencia el puntaje 6 es el mas comun que corresponde con la media.
- El rango de la muestra esta entre 0 y 10.
- No hay valores faltantes

#### 2.6 vote_count (Votos recibidos).                    Numérico

- Valor maximo de 14.075. Media de 10 y 95% de 435.
- Revisar outliers
- Cantidad de ceros: 2846 (6%), revisar
- No hay valores faltantes

#### 2.7 status (Estado de la pelicula).                  Texto

 - El 99% de los registros son películas Released (estrenadas)

 #### 2.8 original_language (Idioma original).            Texto

- El 71% de las peliculas son en ingles.

 #### 2.9 runtime (Duración de pelicula).                 Texto

 - El promedio es 94 minutos , la mediana es 95 minutos y la moda es 90.
 - Cantidad de ceros: 1781 (4%), revisar
 - Se puede hacer un analisis de los considerados como cortometrajes (menores a 30 minutos, revisar distribucion de frecuencia y tematicas)

#### 2.10 budget (Presupuesto).                         Numerico

- Cantidad de ceros el 80% (36.470)
- Maximo 380 M y promedio 4.2 M.
- Valor 95%: 25 M
- Pocos valores por encima de los 25 M, el grueso de la peliculas esta por debajo de los 25 M
- Retirar los 0 para poder determinar las metricas mas exactas ya que promedio y 95% se ven afectados.

#### 2.11 revenue (Recaudación).                         Numerico

- Cantidad de ceros el 84% (37.949)
- Maximo 2.8 B y promedio 0 B.
- Valor 95%: 0 B
- Retirar los 0 para poder determinar las metricas mas exactas.

#### 2.12 tagline (Frase celebre).                         Texto

- Valores faltantes: 24.960 (55%)
- No hay preponderancia en la frecuencia de algun valor

#### 2.13 id_btc (id de belongs_to_collection).                         Numerico

- Identificador de la collecion
- Valores faltantes: 42.183 (93%)

#### 2.14 name_btc (name de belongs_to_collection).                         Texto

- Nombre de la collecion
- Valores faltantes: 42.183 (93%)

#### 2.15 poster_btc (imagen).                         Texto

- Parecen URL de imagenes
- Valores faltantes: 42.183 (93%)

#### 2.16 backdrop_btc (imagen).                         Texto

- Parecen URL de imagenes
- Valores faltantes: 42.183 (93%)

#### 2.17 iso_639-1 (Sigla idioma).                         Texto

- 22.366 (54%) en (Ingles)
- Valores faltantes: 3.792 (8%)

#### 2.18 language_name (Nombre idioma).                         Texto

- 22.366 (54%) solo un idioma  ingles (Ingles)
- Valores faltantes: 3.915 (9%)

#### 2.19 release_year (Año estreno).                         Texto

- Menor año: 1874
- Mayor año: 2020
- Promedio:  1992
- Mediana:  2001
- Entre 2000 y 2017 una cantidad significativa de registros
- La moda es 2014 (1973- 4.4%)

#### 2.20 return (revenue/budget).                         Numerico

- Cantidad de ceros el 88% (40.033)
- Maximo 12.4 B y promedio 0 .
- Valor 95%: 0 B
- Retirar los 0 para poder determinar las metricas mas exactas.

#### 2.21 companies_id (Id compañias productoras).            Texto

- Valores faltantes 27% (12.264)

#### 2.22 companies_name (Nombres compañias productoras).            Texto

- Valores faltantes 27% (12.264)
- Las compañias con mas peliculas: Metro-Goldwyn- Mayer MGM (742-2%), WarnerBros (540-2%)

#### 2.23 countries_iso (Sigla Pais).            Texto

- 17.836 (46%) Estados Unidos
- Valores faltantes: 6.213 (14%)

### 2.24 countries_name (Nombre Pais).            Texto

- 17.836 (46%) Estados Unidos
- Valores faltantes: 6.213 (14%)

### 2.25 release_date (Fecha estreno).            Texto

- El año con mas estrenos 2008 (136)
- El rango de años con mas estrenos : de 2001 a 2008 (842 - 1.9%)
- Valores faltantes: 6.213 (14%)

### 2.26 month_time (Mes estreno).            Texto

- El mes con mas estrenos: Enero   (5909-13%)
- El segundo mes con mas estrenos: Septiembre  (4834-11%)
- El mes con menos estrenos: Julio (2638- 6%)

El mes de Enero es un mes que genera desconfianza ya que los valores de fecha de estreno que no tenian una fecha exacta pudieron ser registrados con el primer dia del año correspondiente como se observa en los datos de released_date.

Nota: Dato no confiable

### 2.27 day_time (Dia estreno).            Texto

- El dia con mas estrenos: Viernes   (13902-31%)
- El segundo dia con mas estrenos: Jueves  (7520-17%)
- El dia con menos estrenos: Lunes (3497- 8%)

