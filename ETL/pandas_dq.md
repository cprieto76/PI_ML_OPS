# Libreria pandas_dq (https:/(https://pypi.org/project/pandas-dq/1.1/)

- Herramienta para analizar y limpiar sus datos en una sola línea de código con un transformador compatible con Scikit-Learn.

- **pandas_dq** es una nueva biblioteca de python para limpiar automáticamente su conjunto de datos sucios utilizando las funciones pandas scikit_learn. Puede analizar su conjunto de datos y corregirlos, ¡todo en una sola línea de código!

- pandas_dq has two important modules: find_dq and Fix_DQ.

  - 1. find_dq function

## Analisis del informe report.html (Duración Analisis: 1 minuto 15 segundos)
### Primer vistazo a estado de los datos que pueden requerir transformacion para un analisis mas acertado.

### 1. Overview

#### 1.1 Aspectos a destacar

1.1.1 Gran cantidad de valores faltantes (missing values) 19.6 %

1.1.2 Columnas 27 de las cuales:
- Variables Numericas :        10
- Variables de Texto:          13
- Variables Categoricas:        3
- Variables de Fecha:           1

1.1.3 Filas duplicadas:         0

#### 1.2 Acciones a desarrollar

### 2. Alertas

#### 2.1 Correlacion Alta

- popularity vs vote_count
- vote_count vs revenue
- budget vs revenue
- budget vs return

Nota: Revisar si los ceros y valores faltantes puede afetar este analisis

#### 2.2 Desbalances

El status nos muestra el 97% de las peliculas con categoria released lo cual indica que el analisis total se va a hacer sobre peliculas estrenadas

#### 2.3 Valores faltantes

Los siguientes features, y la cantidad y porcentaje de valores faltantes:

- overview:         946 (2.1%) 
- tagline:        24960 (55.0%)
- id_btc:         42183 (93.0%) 
- name_btc:       42183 (93.0%) 
- poster_btc:     42183 (93.0%) 
- backdrop_btc:   42183 (93.0%) 
- iso_639_1:       3792 (8.4%) 
- language_name:   3915 (8.6%) 
- companies_id:   12264 (27.0%) 
- companies_name: 12264 (27.0%) 
- countries_iso:   6213 (13.7%) 
- countries_name:  6213 (13.7%)

Se define el origen de esos valores faltantes y la manera de tratarlos (Revisar documento **Valores_Faltantes** en carpeta **EDA/**)

#### 2.4 Sesgo (Skewness)

- **popularity**: altamente sesgada con un valor gamma γ1 = 29.21, lo cual indica la asimetria en la distribucion de probabilidad.
  Los valores estan concentrados hacia la izquierda.
  Hay 40 registros con valor 0 y y el maximo de esa distribucion es 543 . Posible outlier.
  Hacer revision en detalle para descartar outliers ya que pueden ser causantes de sesgo. Al presentar un valor muy alto erroneo puede interpretar un sesgo equivocado.

- **return**: altamente sesgada con un valor gamma γ1 = 138.28, lo cual indica la asimetria en la distribucion de probabilidad. Los valores estan concentrados hacia la izquierda.
  Hay 40033 registros (83.3%) con valor 0 y y el maximo de esa distribucion es 12396383 . Posible outlier.
  Hacer revision en detalle

#### 2.5 Ceros

Cantidad alta de registros con valor cero

- vote_average:    2944 (6.5%) 
- vote_count:      2846 (6.3%) 
- runtime:         1781 (3.9%) 
- budget:         36470 (80.4%) 
- revenue:        37949 (83.7%) 
- return:         40033 (88.3%)

Para los análisis basados en los features (columnas): budget, revenue y return no se debe tener en cuenta los valores iguales a 0 y mirar si los registros que quedan que son aproximadamente entre 5000 y 8000 (20%) son representativos para las conclusiones o para el modelo que se intenta implementar.

### 2. Interactions

En esta seccion del informe se observa como estan relacionadas las variables o features numericas entre si. 

Las variables numericas son: 

- id
- popularity
- vote_average
- vote_count
- runtime
- budget
- revenue
- id_btc
- release_year
- return
 
Nota: Estas interacciones se ven afectadas por las alertas presentadas referentes a Ceros y Valores Faltantes por lo cual es necesario corregir primero esas Alertas para luego pasar a interpretar o no estas Interactions entre variables numericas

### 3. Correlaciones

Los aspectos a tener en cuenta fueron detectados en las Alertas
